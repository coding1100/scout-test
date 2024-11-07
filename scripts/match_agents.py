from rapidfuzz import process, fuzz
import pandas as pd
import os

def fuzzy_match_agents():
    # File paths
    file1 = os.path.join("data", "processed", "cleaned_agents.csv")
    file2 = os.path.join("data", "raw", "agents_2.csv")
    output_file = os.path.join("data", "processed", "unified_agents.csv")

    # Load datasets
    agents1 = pd.read_csv(file1)
    agents2 = pd.read_csv(file2)

    # Check for 'full_name' column in cleaned_agents.csv (previously 'agent_name')
    if 'full_name' not in agents1.columns:
        print(f"Error: 'full_name' column not found in {file1}. Available columns: {list(agents1.columns)}")
        return

    # Normalize names and handle non-string values
    agents1['normalized_name'] = agents1['full_name'].fillna("").astype(str).str.lower().str.strip()
    agents2['normalized_name'] = agents2['agentdetails__mlsagentfullname'].fillna("").astype(str).str.lower().str.strip()

    # Fuzzy match and merge in chunks
    matches = []
    for name in agents1['normalized_name']:
        best_match = process.extractOne(name, agents2['normalized_name'], scorer=fuzz.ratio)
        if best_match and best_match[1] > 85:  # Adjust threshold as needed
            matches.append({'name': name, 'matched_name': best_match[0], 'score': best_match[1]})

    # Convert matches to a DataFrame
    matches_df = pd.DataFrame(matches)
    
    # Save unified agents
    matches_df.to_csv(output_file, index=False)
    print(f"Unified agents saved to {output_file}")

if __name__ == "__main__":
    fuzzy_match_agents()