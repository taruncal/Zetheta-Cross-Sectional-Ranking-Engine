# ==============================================================================
# MODULE: src/audit.py
# Immutable Hash-Chain Audit Logger for SEBI Compliance & Lineage
# Zetheta Algorithms Private Limited (CIN: U62012MH2023PTC410415)
# ==============================================================================

import hashlib
import json
import time

def append_audit_record(prev_hash: str, agent_name: str, tool_name: str, args: dict, result_summary: dict) -> dict:
    """
    Appends a tamper-evident record linking to the previous block's hash.
    Ensures reproducibility and satisfies institutional audit trail mandates.
    """
    timestamp = time.time()
    result_str = json.dumps(result_summary, default=str, sort_keys=True)
    result_hash = hashlib.sha256(result_str.encode()).hexdigest()
    
    record = {
        'timestamp': timestamp,
        'agent': agent_name,
        'tool': tool_name,
        'arguments': args,
        'result_hash': result_hash,
        'previous_hash': prev_hash if prev_hash else "ROOT_GENESIS_BLOCK"
    }
    
    # Compute block hash
    block_str = json.dumps(record, sort_keys=True)
    record['block_hash'] = hashlib.sha256(block_str.encode()).hexdigest()
    
    return record

def verify_audit_chain(audit_log: list) -> bool:
    """
    Verifies the cryptographic integrity of the entire audit hash-chain.
    """
    for i, block in enumerate(audit_log):
        # Re-verify block hash
        temp_block = block.copy()
        current_block_hash = temp_block.pop('block_hash')
        
        block_str = json.dumps(temp_block, sort_keys=True)
        calculated_hash = hashlib.sha256(block_str.encode()).hexdigest()
        
        if calculated_hash != current_block_hash:
            print(f"-> Integrity failure at block index {i} (Block Hash Mismatch)")
            return False
            
        # Verify chain linkage
        if i > 0:
            if block['previous_hash'] != audit_log[i-1]['block_hash']:
                print(f"-> Chain linkage broken at block index {i}")
                return False
                
    print("-> Audit hash-chain cryptographic integrity verified successfully.")
    return True
