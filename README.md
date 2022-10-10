# Python projects 
This repository contains my bachelor thesis. 

![GitHub last commit](https://img.shields.io/github/last-commit/Mazilius/Python-projects)

## Libraries 
Use the package manager pip in order to install the other libraries for the bachelor project. 
```python
import os
import tweepy as tw 
import pandas as pd 
import numpy as np 

import statistics 
from statistics import mean 

import sqlalchemy 
from sqlalchemy import create_engine 

import psycopg2 

import nltk
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords

import matplotlib.pyplot as plt
import seaborn as sns 
import itertools 
import collections 
from collections import Counter

import re 
from textblob import TextBlob
```
## Usage 

### Topic mining and text processing - Bachelor project
The following bullet points contains prerequisits in order to use the system. 
* Credentials from [Twitter](https://developer.twitter.com/) in order to use their API if you wish to gather more data
* Connect to [postgresql](https://www.postgresql.org/) database in order to handle and view the data
* The original data is in the zip folder
