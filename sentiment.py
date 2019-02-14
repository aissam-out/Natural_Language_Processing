import os
import re
import nltk
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

# load the training data
train = pd.read_csv("./data/labeledTrainData.tsv", header = 0, delimiter = '\t')

def review_to_words(raw_review):
        review_text = BeautifulSoup(raw_review, features="html5lib").get_text()
        letters_only = re.sub("[^a-zA-Z]", " ", review_text)
        words = letters_only.lower().split()
        stops = set(stopwords.words("english"))
        meaningful_words = [w for w in words if not w in stops]
        return(" ".join( meaningful_words ))
