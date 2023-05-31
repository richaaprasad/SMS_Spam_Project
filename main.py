import streamlit as st
import pickle
import string
import gensim
import nltk
from gensim.utils import tokenize
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

ps= PorterStemmer()
all_stopwords = gensim.parsing.preprocessing.STOPWORDS

def transform_text(text):
    text = text.lower()
    text = list(tokenize(text))

    t = []
    for i in text:
        if i.isalnum():
            t.append(i)

    text = t[:]
    t.clear()

    for i in text:
        if i not in string.punctuation and i not in all_stopwords:
            t.append(i)

    text = t[:]
    t.clear()

    for i in text:
        t.append(ps.stem(i))

    return " ".join(t)  # To return it in string form


tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("SMS/Email Classifier")
input_sms = st.text_area("Enter The Message")

if st.button('Predict'):

    # Work in 4 steps
    # 1.Preprocess
    transformed_sms = transform_text(input_sms)

    # 2.Vectorize
    vector_input = tfidf.transform([transformed_sms])

    # 3.Predict
    result = model.predict(vector_input)[0]

    # 4.Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")



