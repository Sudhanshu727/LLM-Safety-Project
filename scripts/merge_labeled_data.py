import pandas as pd


original = pd.read_csv("data/labeled_responses.csv")
new_data = pd.read_csv("data/evaluated_red_team_results.csv")


merged = pd.concat([original, new_data], ignore_index=True)


merged = merged.drop_duplicates(subset=["Prompt"], keep="last")


merged.to_csv("data/labeled_responses.csv", index=False)
print(" Merged dataset saved to data/labeled_responses.csv")
