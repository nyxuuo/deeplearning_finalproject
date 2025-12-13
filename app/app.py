import streamlit as st
import torch
# from transformers import (
#     DistilBertTokenizerFast, DistilBertForSequenceClassification,
#     BertTokenizerFast, BertForSequenceClassification,
#     RobertaTokenizerFast, RobertaForSequenceClassification,
# )

from transformers import AutoTokenizer, AutoModelForSequenceClassification

label_map = {
    0: "Normal",
    1: "Depression",
    2: "Suicidal",
    3: "Anxiety",
    4: "Bipolar",
    5: "Stress",
    6: "Personality Disorder"
}

def load_model(model_name):
    base_path = "./model/"

    models = {
        "distilbert": f"{base_path}/distilbert_trained",
        "bert": f"{base_path}/bert_trained",
        "roberta": f"{base_path}/roberta_trained",
    }

    model_path = models[model_name]

    # load tokenizer & model langsung dari folder
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)

    model.to("cpu")
    model.eval()
    return tokenizer, model


st.title("🧠 Mental Health Text Classification")

model_choice = st.selectbox("Choose a model:", ["distilbert", "bert", "roberta"])
tokenizer, model = load_model(model_choice)

text = st.text_area("Enter text to analyze:")

if st.button("Predict"):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        pred = int(torch.argmax(logits, dim=1))

    st.subheader("Prediction")
    st.write(f"**{label_map[pred]}**")

