# ==============================================================================
# MODULE: src/model.py
# LightGBM LambdaRank Training & Optuna Hyperparameter Optimisation Engine
# Zetheta Algorithms Private Limited (CIN: U62012MH2023PTC410415)
# ==============================================================================

import lightgbm as lgb
import numpy as np
import optuna
from scipy.stats import spearmanr

def train_lambdarank_model(X_tr, y_tr, grp_tr, X_va, y_va, grp_va, params=None):
    """
    Trains a LightGBM LambdaRank model optimized for NDCG@K.
    """
    if params is None:
        params = {
            'objective': 'lambdarank',
            'metric': 'ndcg',
            'ndcg_eval_at': [10, 20],
            'learning_rate': 0.03,
            'num_leaves': 31,
            'verbose': -1
        }
    
    train_set = lgb.Dataset(X_tr, label=y_tr, group=grp_tr)
    valid_set = lgb.Dataset(X_va, label=y_va, group=grp_va, reference=train_set)
    
    model = lgb.train(
        params,
        train_set,
        num_boost_round=300,
        valid_sets=[valid_set],
        callbacks=[lgb.early_stopping(30, verbose=False)]
    )
    return model

def optimize_hyperparameters(X_tr, y_tr, grp_tr, X_va, y_va, valid_df, n_trials=10):
    """
    Runs Optuna Bayesian hyperparameter search maximizing Rank IC.
    """
    optuna.logging.set_verbosity(optuna.logging.WARNING)
    
    def objective_trial(trial):
        params_trial = {
            'objective': 'lambdarank',
            'metric': 'ndcg',
            'learning_rate': trial.suggest_float('lr', 0.01, 0.05, log=True),
            'num_leaves': trial.suggest_int('num_leaves', 15, 63),
            'min_data_in_leaf': trial.suggest_int('min_leaf', 50, 300),
            'feature_fraction': trial.suggest_float('ff', 0.6, 1.0),
            'verbose': -1
        }
        
        dtr = lgb.Dataset(X_tr, label=y_tr, group=grp_tr)
        dva = lgb.Dataset(X_va, label=y_va, group=grp_va, reference=dtr)
        
        m_trial = lgb.train(params_trial, dtr, num_boost_round=100, valid_sets=[dva], callbacks=[lgb.early_stopping(20, verbose=False)])
        preds = m_trial.predict(X_va)
        
        temp_df = valid_df.copy()
        temp_df['trial_score'] = preds
        ic_vals = temp_df.groupby('date').apply(lambda g: spearmanr(g['trial_score'], g['fwd_ret']).correlation).mean()
        return ic_vals if not np.isnan(ic_vals) else -1.0

    study = optuna.create_study(direction='maximize')
    study.optimize(objective_trial, n_trials=n_trials)
    return study.best_params
