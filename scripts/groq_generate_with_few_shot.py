from groq import Groq
import csv

api_key = "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"

client = Groq(api_key=api_key)

# Load few-shot system prompt
with open("data/few_shot_prompt.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()

# Collect user prompts
user_prompts = []
print("Enter your prompts (type 'exit' to finish):")
while True:
    prompt = input("> ")
    if prompt.strip().lower() == "exit":
        break
    if prompt.strip():
        user_prompts.append(prompt.strip())

if not user_prompts:
    print("No prompts entered. Exiting.")
    exit()

with open("results/red_team_outputs.csv", mode="w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Prompt", "Response"])

    for prompt in user_prompts:
        print(f"\n🧠 Prompt: {prompt}")
        completion = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=2,
            max_tokens=400,
            top_p=1
        )
        reply = completion.choices[0].message.content.strip()
        print(f"💬 Response:\n{reply}\n")
        writer.writerow([prompt, reply])
