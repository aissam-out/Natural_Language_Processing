import os
import re
import nltk
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

train = pd.read_csv("./data/labeledTrainData.tsv", header = 0, delimiter = '\t')
