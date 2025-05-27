import pandas as pd

# Load both datasets
original = pd.read_csv("data/labeled_responses.csv")
new_data = pd.read_csv("data/evaluated_red_team_results.csv")

# Combine them
merged = pd.concat([original, new_data], ignore_index=True)

# Drop duplicates (based on Prompt only)
merged = merged.drop_duplicates(subset=["Prompt"], keep="last")


merged.to_csv("data/labeled_responses.csv", index=False)
print("✅ Merged dataset saved to data/labeled_responses.csv")
