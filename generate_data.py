from pathlib import Path
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
import pickle

# Download NLTK data
nltk.download('stopwords')

def save_data(data, file_path):
    with open(file_path, "wb") as file:
        pickle.dump(data, file)

# Load the corpus
file_path = Path("corpus.txt")

with open(file_path, "r", encoding="utf-8") as file:
    file_content = file.read()

words = re.findall(r'\w+', file_content.lower())

V = set(words)

# Set of stopwords
stop_words = set(stopwords.words('english'))

# Filter out non-alphabetic words and stop words
filtered_words = [word for word in words if word.isalpha() and word not in stop_words]

# Count the frequency of each filtered word
word_freq = Counter(filtered_words)

# Save vocabulary and word frequencies
save_data(V, "vocabulary.pkl")
save_data(word_freq, "word_freq.pkl")