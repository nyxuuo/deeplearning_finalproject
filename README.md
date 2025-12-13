# DEEP LEARNING FINAL PROJECT
# Mental Health Text Classification using DistilBERT, BERT, and RoBERTa

## Full google drive link:
🔗 [FINALPROJECT_DEEPLEARNING](https://drive.google.com/drive/folders/1jcaEpzCvAloIWYjkwoNsH087PG773ei-?usp=sharing)

This project aims to **predict mental health categories from user-written text** using three state-of-the-art Transformer models:

- **DistilBERT**
- **BERT-base**
- **RoBERTa-base**

The app classifies text into **7 mental health labels**:

0: "Normal"
1: "Depression"
2: "Suicidal"
3: "Anxiety"
4: "Bipolar"
5: "Stress"
6: "Personality Disorder"

This project includes **dataset preprocessing**, **model training**, **evaluation**, and a **Streamlit web application**.


## 🎯 Project Goals

This project was built to:

- Detect mental health predictions/indications from user input (written text)
- Compare model performance (DistilBERT vs BERT vs RoBERTa)  
- Evaluate classification quality using F1-score and confusion matrix  
- Deploy an interactive demo using Streamlit  


## 🧠 Model Overview

### **DistilBERT**
- a lighter and faster version of BERT  
- 40% smaller, 60% faster    
- Works best for **real-time applications**

### **BERT-base**
- has a strong semantic understanding  
- good for complex text reasoning  
- more expensive (computationally)

### **RoBERTa-base**
- Optimized BERT (longer training, dynamic masking, larger batches)  
- Often achieves the highest accuracy 
- Most robust among the other 3


## 🧪 Model Training & Evaluation

The notebook `model.ipynb` includes:

- Data cleaning  
- Tokenization  
- Fine-tuning all 3 models  
- Saving trained models  
- Evaluating using:
  - Classification report  
  - Confusion matrix  
  - Macro F1-score  
- Loss comparison (training & validation via forward pass)

To view the detailed training logs, see:  
📄 **model.ipynb**

---

## 🚀 Running the Streamlit App

### **1. Install dependencies**
```bash
pip install streamlit torch transformers
```

### **2. Run the app**
Run the app by:
``` 
streamlit run app/app.py
```

### **FOR GOOGLE COLAB**
Run the app by installing cloudfare & running the streamlit:
```
!wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
!dpkg -i cloudflared-linux-amd64.deb
!streamlit run /content/drive/MyDrive/FINPRO_DEEPLEARNING/app/app.py --server.port 8501 &>/dev/null &
!cloudflared tunnel --url http://localhost:8501 --no-autoupdate
```

After running the tunnel, it will show a link to access the streamlit app (usually in a format of xxx.trycloudfare.com)



