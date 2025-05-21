import joblib
import re
import nltk
import language_tool_python
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Setup once
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

# Initialize tools once
tool = language_tool_python.LanguageTool('en-US')
lemmatizer = WordNetLemmatizer()
nltk_stop_words = set(stopwords.words('english'))
custom_stop_words = {
    'the', 'a', 'an', 'in', 'on', 'at', 'is', 'it', 'of', 'for',
    'to', 'and', 'or', 'as', 'with', 'this', 'that'
}
all_stop_words = nltk_stop_words.union(custom_stop_words)

# Load pipeline once
_pipeline = None
def load_pipeline(path='text_classification_pipeline.pkl'):
    global _pipeline
    if _pipeline is None:
        _pipeline = joblib.load(path)
    return _pipeline

# Grammar correction
def correct_grammar(text):
    return tool.correct(text)

# Text cleaning
def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)  # keep only letters and spaces
    text = re.sub(r'\s+', ' ', text).strip().lower()  # normalize whitespace and lowercase
    tokens = text.split()
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in all_stop_words]
    return ' '.join(tokens)

# Main prediction
def predict_text(text):
    corrected = correct_grammar(text)
    cleaned = clean_text(corrected)
    pipeline = load_pipeline()
    prob = pipeline.predict_proba([cleaned])[0]
    return {
        "human": round(prob[0] * 100, 1),
        "AI": round(prob[1] * 100, 1),
    }
