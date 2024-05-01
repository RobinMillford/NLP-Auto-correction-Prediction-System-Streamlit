
---

# NLP Word Correction and Suggestions App

This is a Streamlit web application for word correction and suggestions using natural language processing techniques. The app provides two main functionalities:

1. **Autocorrect**: Automatically corrects misspelled words and provides suggestions for correct words based on the Jaccard distance.

2. **Word Suggestions**: Provides suggestions for words that are not found in the vocabulary based on Levenshtein normalized similarity.

## Features

- **Autocorrect**: Automatically corrects misspelled words in real-time.
- **Word Suggestions**: Provides suggestions for correct words based on user input.
- **User-Friendly Interface**: Simple and intuitive interface for entering words and viewing suggestions.
- **Deployment**: Deployed using Streamlit Sharing for easy access.

## How to Use

1. Select the desired option: Autocorrect or Word Suggestions.
2. Enter the word in the input field.
3. Click the corresponding button to get suggestions.
4. For Autocorrect, corrected words will be displayed in real-time.
5. For Word Suggestions, suggested words will be displayed after clicking the button.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/RobinMillford/NLP-Auto-correction-Prediction-System-Streamlit.git
   ```

2. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```
   streamlit run app.py
   ```

## Deployment

The app is deployed using Streamlit Sharing. You can access it [here](https://bwqdrwycrh7klbgdugu577.streamlit.app/).

## Technologies Used

- Python
- Streamlit
- Pandas
- Textdistance

## Screenshots
![Alt Text](https://github.com/RobinMillford/NLP-Auto-correction-Prediction-System-Streamlit/blob/main/Autocorrect.png)
![Alt Text](https://github.com/RobinMillford/NLP-Auto-correction-Prediction-System-Streamlit/blob/main/suggestion.png)

## Future Improvements

- Implement more advanced natural language processing techniques for better word correction and suggestions.
- Improve the user interface with additional features and customization options.

---
