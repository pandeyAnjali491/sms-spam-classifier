import streamlit as st
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


try:
    nltk.data.find('tokenizers/punkt')
except:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except:
    nltk.download('stopwords')

ps = PorterStemmer()
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("Email/SMS Spam Classifier")
input_sms = st.text_area("Enter the Message")

def transform_text(text):
    # lower case
    text = text.lower()
    # tokenize
    text = nltk.word_tokenize(text)
    # removing special char
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    # removing stop words and punctuations
    # [:] is used for cloning
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    # stemming
    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)

if st.button("Predict"):
    # 1. preprocess
    transform_sms = transform_text(input_sms)

    # 2. vectorize
    vector_input = tfidf.transform([transform_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. display
    if(result==1):
        st.header("Spam")
    else :
        st.header("Not spam")

