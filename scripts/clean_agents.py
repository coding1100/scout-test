import pandas as pd
import os

def normalize_name(name):
    if pd.isna(name):
        return None
    return name.strip().lower()

def clean_agents():
    input_file = os.path.join("data", "raw", "agents.xlsx")
    output_file = os.path.join("data", "processed", "cleaned_agents.csv")
    
    # Load data
    agents = pd.read_excel(input_file)
    
    # Normalize agent names
    agents['normalized_name'] = agents['full_name'].apply(normalize_name)
    
    # Deduplicate agents
    agents.drop_duplicates(subset='normalized_name', inplace=True)
    
    # Save cleaned dataset
    agents.to_csv(output_file, index=False)

if __name__ == "__main__":
    clean_agents()
