# ==============================================================================
# TEST SUITE: tests/test_pipeline.py
# Unit Tests for Pipeline Ingestion and Hash-Chain Integrity
# Zetheta Algorithms Private Limited (CIN: U62012MH2023PTC410415)
# ==============================================================================

import unittest
import pandas as pd
import numpy as np
from src.audit import append_audit_record, verify_audit_chain
from src.pipeline import ZethetaQuantPipeline

class TestZethetaPipeline(unittest.TestCase):
    
    def setUp(self):
        self.pipeline = ZethetaQuantPipeline(execution_date="2026-03-31")

    def test_s3_ingestion(self):
        """Validates that simulated S3 ingestion returns correct shape and schema."""
        df = self.pipeline.simulate_s3_ingestion()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 300)
        self.assertIn('val_z', df.columns)
        self.assertIn('mom_z', df.columns)

    def test_audit_chain_integrity(self):
        """Validates tamper-evident hash-chain verification logic."""
        r1 = append_audit_record(None, "DataAgent", "s3_ingest", {"date": "2026-03-31"}, {"status": "SUCCESS"})
        r2 = append_audit_record(r1['block_hash'], "ModelAgent", "train_rank", {"ic": 0.0111}, {"status": "SUCCESS"})
        audit_log = [r1, r2]
        
        self.assertTrue(verify_audit_chain(audit_log))

if __name__ == '__main__':
    unittest.main()
