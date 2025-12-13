# Trained Models for Mental Health Text Classification

---
## **‼️ The google drive folder for the stored model can be accessed through this link (as the file size is too big):**
[MODEL LINK](https://drive.google.com/drive/folders/1-_lgZsWNAplRe4scNaO6M1VHPd1mWBHp?usp=sharing)
---


This folder contains the **fine-tuned Transformer models** used in the final project:

🔹 **DistilBERT** — `/distilbert_trained`  
🔹 **BERT-base** — `/bert_trained`  
🔹 **RoBERTa-base** — `/roberta_trained`

All models were fine-tuned using the *mental_health_dataset_augmented.csv* dataset for **7 mental health labels classification**:

```
0: "Normal",
1: "Depression",
2: "Suicidal",
3: "Anxiety",
4: "Bipolar",
5: "Stress",
6: "Personality Disorder"
```

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

Original models from https://huggingface.co

---
