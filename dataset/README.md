# Dataset Description

This project uses a mental health–related text dataset provided externally via Google Drive.

Due to dataset size, the dataset is **not stored directly in this repository**.  
Instead, it can be accessed through the following link:

🔗 **Dataset Link (Google Drive):**  
https://drive.google.com/drive/folders/1WFwNkBf3vp8r4-0HuUbgXnxXZAL2pHko?usp=sharing

---

## Dataset Overview

The dataset consists of text data related to mental health discussions, intended for **text classification tasks** such as sentiment or mental health condition detection. The augmented dataset is available in the link above,
and is used for training

The dataset is used to fine-tune and evaluate Transformer-based models, including:
- BERT
- DistilBERT
- RoBERTa

---

## Access Instructions

1. Open the Google Drive link above.
2. Download the dataset file (**mental_health_dataset_augmented.csv**) to your local machine. The other raw dataset is available in the link, but in a seperate folder. 
3. Place the downloaded files inside this `dataset/` directory before running the code.

Example directory structure:
```
dataset/
 ├──  mental_health_dataset_augmented.csv
 ├── README.md
```
