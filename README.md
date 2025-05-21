
# AI-vs-Human-text-detection

A machine learning project that detects whether a given text is AI-generated or human-written. This tool is designed for content moderation, authenticity verification, and academic or research use cases.

We use **Natural Language Processing (NLP)** with **NLTK** for text preprocessing and a **Random Forest Classifier** for prediction. The model is deployed via **FastAPI** for easy integration and testing.

---

## 🚀 Features

- Detects AI-generated vs. human-written text
- NLP preprocessing using NLTK
- Trained with Random Forest Classifier
- FastAPI-based web service

---

## 📁 Project Structure

```
├── app/
│   ├── main.py              # FastAPI app
│   └── model/               # Model directory
│       └── model.rar        # Compressed model file (must be extracted)
├── requirements.txt
└── README.md
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-vs-Human-text-detection.git
cd AI-vs-Human-text-detection
```

---

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

---

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

### 4. Extract the Model File

> ⚠️ The model is compressed as a `.rar` file to keep file size manageable.

To extract it:

#### Install UnRAR:

**Linux/macOS:**

```bash
sudo apt install unrar    # or brew install unrar
```

**Windows:**

- Use WinRAR or 7-Zip GUI  
- Or install unrar with Chocolatey:
```bash
choco install unrar
```

#### Extract the file:

```bash
unrar x app/model/model.rar app/model/
```

Make sure that the extracted file (e.g., `model.pkl`) is placed in the `app/model/` directory.

---

### 5. Run the FastAPI App

```bash
uvicorn app.main:app --reload
```

Then go to:  
📍 http://127.0.0.1:8000/docs – to test the API in your browser with Swagger UI.

---

## 📤 API Usage Example

You can test the API using the Swagger UI or with `curl` / Postman.

### POST `/predict`

#### Request:

```json
{
  "text": "This article was written by an AI language model."
}
```

#### Response:

```json
{
  "prediction": "AI-generated"
}
```

---

## 🤖 Model Details

- **Preprocessing:** Tokenization, stopword removal, lemmatization using NLTK
- **Vectorization:** TF-IDF
- **Classifier:** Random Forest
- **Trained on:** A dataset of mixed AI-generated and human-written texts

---

## 🔮 Future Improvements

- Integrate deep learning models like LSTM or BERT
- Add confidence scores for predictions
- Build a user-friendly front-end interface

---

## 📄 License

This project is licensed under the MIT License – feel free to use, modify, and share!

---

## 🙋‍♂️ Contact

For support, questions, or feedback, contact:  
📧 your.email@example.com  
or open an issue in the GitHub repo: https://github.com/your-username/AI-vs-Human-text-detection
