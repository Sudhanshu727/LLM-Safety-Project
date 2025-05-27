# 🛡️ LLM Safety Evaluation and Improvement

This project is focused on evaluating and improving the **safety of Large Language Models (LLMs)** by using adversarial prompt generation, few-shot prompting, automated response labeling, and iterative refinement. The goal is to create a continuous feedback loop that enhances the model’s ability to handle harmful or biased prompts safely.

---

## 📁 Project Structure

```
LLM Safety Project/
├── script/
│   ├── merge_labeled_data.py            # Merge new labels with the main dataset
│   ├── auto_label_with_gemini.py        # Auto-label responses using Gemini API
│   ├── generate_few_shot_prompt.py      # Create few-shot prompts for mitigation
│   ├── generate_responses.py            # Generate initial model responses
│   └── groq_generate_with_few_shot.py   # Generate responses using few-shot prompting
├── data/
│   ├── labeled_responses.csv            # Full dataset of labeled model outputs
│   ├── evaluated_red_team_results.csv   # Manually reviewed/annotated outputs
│   └── few_shot_prompt.txt              # Dynamically generated few-shot prompt
├── results/
│   └── red_team_outputs.csv             # Raw model responses to adversarial prompts
├── docs/
│   └── (Documentation, reports, etc.)
├── requirements.txt                     # Required Python packages
└── README.md                            # Project overview and instructions
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/llm-safety-eval.git
cd llm-safety-eval/text
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set API Keys

Set your API keys as environment variables:

```bash
export GEMINI_API_KEY='your-gemini-api-key'
export GROQ_API_KEY='your-groq-api-key'
```

Alternatively, use a `.env` file and load it with a library like `python-dotenv`.

---

## 🔁 Evaluation Workflow

Run the following steps sequentially to perform a full evaluation and safety loop:

1. **Generate model responses:**

```bash
python script/generate_responses.py
```

2. **Generate a new few-shot prompt from labeled data:**

```bash
python script/generate_few_shot_prompt.py
```

3. **Use Groq API with few-shot prompt to generate responses:**

```bash
python script/groq_generate_with_few_shot.py
```

4. **Auto-label responses using Gemini:**

```bash
python script/auto_label_with_gemini.py
```

5. **Merge newly labeled responses with master dataset:**

```bash
python script/merge_labeled_data.py
```

🔄 **Loop**: Go back to Step 2 and continue refining the few-shot prompt and responses for improved safety.

---

## ✨ Key Features

- **Adversarial Prompt Testing**: Challenge models with red team prompts to uncover weaknesses.
- **Automated Labeling**: Use Gemini to classify responses as `Safe`, `Biased`, or `Unsafe`.
- **Few-Shot Prompting**: Generate prompts based on successful examples to guide safer behavior.
- **Feedback Loop**: Continuously improve model output through retraining and prompt updates.
- **Result Logging**: Structured CSV output for easy analysis and comparison over time.

---

## 📄 Documentation

- All documentation and reports should be placed in the `docs/` folder.
- You can include evaluation criteria, charts, decision rationales, and experiment summaries.
- Track iterations of `few_shot_prompt.txt` and update `labeled_responses.csv` carefully for consistency and reproducibility.

---

## 🤝 Contributions

We welcome contributions and new ideas related to:

- Prompt engineering
- Response evaluation techniques
- Safer output generation
- Integration with additional LLM APIs

Feel free to fork this repository and make it better!
