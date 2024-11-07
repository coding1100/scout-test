import pandas as pd
import os

def integrate_transactions():
    # File paths
    agents_file = os.path.join("data", "processed", "unified_agents.csv")
    transactions_file = os.path.join("data", "raw", "transactions.csv")
    output_file = os.path.join("data", "processed", "unified_data.csv")

    # Load unified agents data
    agents = pd.read_csv(agents_file)

    # Load and process transactions in chunks
    chunks = []
    for chunk in pd.read_csv(transactions_file, chunksize=10000):
        # Join chunk with agents on normalized name
        merged_chunk = pd.merge(
            chunk, 
            agents, 
            how='left', 
            left_on='agent_name', 
            right_on='name'
        )
        chunks.append(merged_chunk)

    # Concatenate all processed chunks
    final_data = pd.concat(chunks, ignore_index=True)

    # Save final integrated data
    final_data.to_csv(output_file, index=False)

if __name__ == "__main__":
    integrate_transactions()