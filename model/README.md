# Trained Models for Mental Health Text Classification

---
## !! The google drive folder for the stored model can be accessed through this link:
[models_link](https://drive.google.com/drive/folders/1-_lgZsWNAplRe4scNaO6M1VHPd1mWBHp?usp=sharing)
---


This folder contains the **fine-tuned Transformer models** used in the final project:

🔹 **DistilBERT** — `/distilbert_trained`  
🔹 **BERT-base** — `/bert_trained`  
🔹 **RoBERTa-base** — `/roberta_trained`

All models were fine-tuned using the *mental_health_dataset_augmented.csv* dataset for **7-class mental health classification**:

| Label ID | Mental Health Category   |
|---------|---------------------------|
|    0    | Depression                |
|    1    | Anxiety                   |
|    2    | Stress                    |
|    3    | Loneliness                |
|    4    | Suicidal Ideation         |
|    5    | Well-being Low            |
|    6    | Normal                    |

---

## 📦 Folder Structure

Each folder contains:

**DistilBERT**

```
distilbert_trained/
│── config.json
│── tokenizer.json
│── tokenizer_config.json
│── vocab.txt
│── special_tokens_map.json
│── model.safetensors

```

**BERT**

```
bert_trained/
│── config.json
│── tokenizer.json
│── tokenizer_config.json
│── vocab.txt
│── special_tokens_map.json
│── model.safetensors

```

**RoBERTA**

```
roberta_trained/
│── config.json
│── tokenizer.json
│── tokenizer_config.json
│── vocab.txt
│── special_tokens_map.json
│── model.safetensors

```

## > How to Load These Models

All models can be loaded using HuggingFace `AutoTokenizer` and `AutoModelForSequenceClassification`.

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_path = "/content/drive/MyDrive/FINPRO_DEEPLEARNING/model/distilbert_trained"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

model.eval()
```

```
## ⚠️ Notes

- These models were **fine-tuned on Colab** and saved into Google Drive.
- Works with both **CPU** and **GPU**.
- These model were fully run in google colab

---

## 📘 Citation / References

These models are fine-tuned versions of:

- DistilBERT: *distilbert-base-uncased*
- BERT: *bert-base-uncased*
- RoBERTa: *roberta-base*

Original models from 👉 https://huggingface.co

---
