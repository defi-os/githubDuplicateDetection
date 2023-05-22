import pandas as pd
import sklearn as sk
import math 
import nltk
from collections import Counter
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

def split_text(text:str) -> list:
    return text.split(" ")

def remove_stopwords(wordList: list) -> list:
    filtered_sentence = [w for w in wordList if not w in stop_words]
    return filtered_sentence

def generate_tf_idf(text: str) -> Counter:
    formatted_text = remove_stopwords(split_text(text))
    count = len(formatted_text)
    formatted_text_dict = Counter(formatted_text)
    for word in formatted_text_dict:
        formatted_text_dict[word] = formatted_text_dict[word]/count
    return formatted_text_dict

