import streamlit as st
import pandas as pd
import textdistance
import pickle

def load_data(file_path):
    with open(file_path, "rb") as file:
        data = pickle.load(file)
    return data

# Load vocabulary and word frequencies
V = load_data("vocabulary.pkl")
word_freq = load_data("word_freq.pkl")

def my_autocorrect(input_word):
    input_word = input_word.lower()  # Convert the input word to lowercase
    
    # Check if the input word is in the vocabulary
    if input_word in V:
        # Return a DataFrame with the correct word and similarity score 1.0
        return pd.DataFrame({'Word': [input_word], 'Similarity': [1.0]})
    
    # Calculate similarity scores using Jaccard distance
    similarity_scores = {word: textdistance.jaccard(input_word, word) for word in V}
    
    # Create a DataFrame from the similarity scores
    df = pd.DataFrame({'Word': list(V), 'Similarity': list(similarity_scores.values())})
    
    # Sort the DataFrame by 'Similarity' in descending order
    df = df.sort_values(by='Similarity', ascending=False)
    
    return df.head()

def correction_suggestion(word):
    word = word.lower()
    
    # Check if the word is in the vocabulary
    if word in V:
        suggestions = [w for w in V if w != word and textdistance.levenshtein.normalized_similarity(word, w) >= 0.7]
        if suggestions:
            return 'Your word seems to be correct: ' + word + ', Suggestions: ' + ', '.join(suggestions)
        else:
            return 'Your word seems to be correct: ' + word + ', No suggestions found.'
    
    # If the word is not in the vocabulary, find suggestions based on Levenshtein normalized similarity
    suggestions = [w for w in V if textdistance.levenshtein.normalized_similarity(word, w) >= 0.7]
    
    # Return the first suggestion from the list if suggestions exist, otherwise return None
    if suggestions:
        return suggestions[0]
    else:
        return None

# Streamlit App
st.title('Word Correction and Suggestions')

option = st.radio("Choose Option:", ('Autocorrect', 'Word Suggestions'))

if option == 'Autocorrect':
    input_word_auto = st.text_input("Enter a word for autocorrection:")
    if st.button('Correct'):
        suggestion_auto = my_autocorrect(input_word_auto)
        # Check if the suggestion is a string
        if isinstance(suggestion_auto, str):
            st.write(suggestion_auto)  # Display the string directly
        else:
            st.table(suggestion_auto)  # Display DataFrame in a table
        
elif option == 'Word Suggestions':
    input_word_sugg = st.text_input("Enter a word for suggestions:")
    if st.button('Suggest'):
        suggestion_word = correction_suggestion(input_word_sugg)
        st.write("Corrected word suggestion:", suggestion_word)