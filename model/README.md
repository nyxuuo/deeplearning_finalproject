# Trained Models for Mental Health Text Classification

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

```
model_name_trained/
│── config.json
│── tokenizer.json
│── tokenizer_config.json
│── vocab.txt / merges.txt (depending on model)
│── pytorch_model.bin   (model weights)
```

**Example:**

```
distilbert_trained/
│── config.json
│── tokenizer.json
│── tokenizer_config.json
│── vocab.txt
│── pytorch_model.bin
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

---

## > How to Use the Model for Prediction

```python
text = "I feel overwhelmed and sad."

inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

with torch.no_grad():
    logits = model(**inputs).logits
    pred = torch.argmax(logits, dim=1).item()

print("Predicted label:", pred)
```
## ⚠️ Notes

- These models were **fine-tuned on Colab** and saved into Google Drive.
- There is **no `.pt` file** because models were saved using the HuggingFace format.
- Works with both **CPU** and **GPU**.

---

## 📘 Citation / References

These models are fine-tuned versions of:

- DistilBERT: *distilbert-base-uncased*
- BERT: *bert-base-uncased*
- RoBERTa: *roberta-base*

Original models from 👉 https://huggingface.co

---

## The google drive folder for the stored model can be accessed through this link:
[models_link](https://drive.google.com/drive/folders/1-_lgZsWNAplRe4scNaO6M1VHPd1mWBHp?usp=sharing)
