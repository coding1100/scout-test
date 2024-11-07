import os
from scripts.match_agents import fuzzy_match_agents
from scripts.integrate_transactions import integrate_transactions

def run_pipeline():
    print("Starting ETL Pipeline...")
    try:
        print("Step 1: Fuzzy matching agents...")
        fuzzy_match_agents()
        print("Step 1 Completed!")

        print("Step 2: Integrating transactions...")
        integrate_transactions()
        print("Step 2 Completed!")

        print("ETL Pipeline Complete!")
    except Exception as e:
        print(f"Pipeline failed: {e}")

if __name__ == "__main__":
    run_pipeline()