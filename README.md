# Safer LLMs – AIMS-DTU Research Intern Project

## 🧠 Project Overview
This project explores how large language models (LLMs) can produce harmful, biased, or unsafe outputs, and implements methods to detect and mitigate such behavior.

## 📋 Objectives
- Generate adversarial prompts and collect LLM outputs
- Classify responses as Safe / Biased / Unsafe
- Train a transformer-based classifier for safety detection
- Implement a mitigation method to reduce unsafe output

## 🛠️ Tools & Libraries
- Model: LLaMA-2 Chat (via Hugging Face)
- Libraries: `transformers`, `huggingface_hub`, `scikit-learn`, `pandas`, `matplotlib`

## 📁 Project Structure
├── data/ # Collected prompts and responses
├── models/ # Saved classifier models
├── scripts/ # Scripts for generation, classification, mitigation
├── notebooks/ # Jupyter notebooks for testing or analysis
├── results/ # Graphs, evaluation results
├── docs/ # Report or supporting documents
└── README.md # Project description