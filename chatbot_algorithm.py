# Importing Relevant Libraries

import json
import string
import random
import time
import datetime
import webbrowser
import requests
import urllib
#  pip install requests_html
from requests_html import HTML
from requests_html import HTMLSession
import re
from os import system, name
from difflib import SequenceMatcher

import nltk
# nltk.download('omw-1.4')

import numpy as np
from nltk.stem import WordNetLemmatizer
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.models import load_model

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import string
 
# nltk.download ("punkt")
# nltk.download ("wordnet")

#Loading the Dataset:
data_file = open('intents.json').read()
data = json.loads(data_file)

qa_dict = []

# Creating data_X and data_Y

words = [] #For Bow model/ vocabulary for patterns
classes = [] #for Bow model/ vocabulary for tags

data_X = [] #for storing each pattern

data_y = [] #for storing tag corresponding to each pattern in datax
# Iterating over all the intents

def remove_punct(input_str):
	#print (input_str)
	output_str = re.sub('[^A-Za-z0-9]+', ' ', input_str)
	#print (output_str)

	return ([output_str])

def remove_all_punct(words):
	hasil = []
	for word in words:
		hasil.extend(remove_punct(word))

	return (hasil)

def remove_two_letters(words):
	hasil = []
	for word in words:
		word = word.replace(" ", "")
		if (len(word)>2):
			hasil.extend([word])

	return (hasil)

def fuzzy_search(wordcheck, words, strictness, strictoke):
    rtbesar = 0
    wordpilih = wordcheck
    for word in words:
        similarity = SequenceMatcher(None, word, wordcheck)
        if (rtbesar<similarity.ratio()):
            rtbesar = similarity.ratio()
            wordpilih = word

    if (strictoke==1 and rtbesar>=strictness):
        wordhasil = wordpilih
    else:
        wordhasil = wordcheck
                    
    return wordhasil, rtbesar


def get_right_word(tulisan):
    tulisan = re.sub("\s\s+", " ", tulisan)
    words_list = tulisan.split()
    hasil = []
    tulisanx = ''
    for word in words_list:
        wordpilih, rasio = fuzzy_search(word, words, 0.8, 1)
        # print ('asli=', word, ', fuzzy_search=', wordpilih, ', rasio=', rasio)
        hasil.extend([wordpilih])
        tulisanx = tulisanx + ' ' + wordpilih

    tulisanx = re.sub("\s\s+", " ", tulisanx)
    tulisanx = tulisanx.strip()
            
    return tulisanx, hasil 


for intent in data["intents"]:
    for pattern in intent["patterns"]:
        tokens = nltk.word_tokenize(pattern) # tokenize each pattern
        words.extend(tokens) #and append tokens to words
        data_X.append(pattern) #appending pattern to data_X
        data_y.append(intent["tag"]) # appending the associated tag to each pattern

    # adding the tag to the classes if it's not there already
    if intent["tag"] not in classes:
        classes .append(intent["tag"])

 
# initialzing lemmatizer to get stem of words

factory = StemmerFactory()
stemmer = factory.create_stemmer()

# lemmatize all the words in the vocab and convert them to lowercase
# if the words don't appear in punctuation

words = [stemmer.stem(word.lower()) for word in words if word not in string.punctuation]

# sorting the vocab and classes in alphabetical order and taking the # set to ensure no duplicates occur
words = sorted(set(words))
words = remove_all_punct(words)
words = remove_two_letters(words)

classes = sorted(set(classes))

 
# Text to Numbers

training = []

out_empty = [0] * len(classes)

# creating the bag of words model
for idx, doc in enumerate(data_X):
    bow = []
    text = stemmer.stem (doc.lower())
    for word in words:
        bow.append(1) if word in text else bow.append(0)

    # mark the index of class that the current pattern is associated
    # to
 
    output_row = list(out_empty)
    output_row[classes.index(data_y[idx])] = 1
    # add the one hot encoded BoW and asociated classes to training
    training.append([bow, output_row])

# shuffle the data and convert it to an array
random.shuffle (training)
training = np.array(training, dtype=object)
# split the features and target labels
train_X = np.array(list(training[:, 0]))
train_Y = np.array(list(training[:, 1]))


# The Neural Network Model

model = Sequential ()
model.add(Dense(128, input_shape=(len(train_X[0]),), activation="relu"))
model.add(Dropout (0.5))
model.add(Dense(64, activation="relu"))
model.add(Dropout (0.5))
model.add(Dense(len(train_Y[0]), activation = "softmax"))
adam = tf.keras.optimizers.legacy.Adam(learning_rate=0.01, decay=1e-6)
model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=["accuracy"])

 
print (model.summary())
model.fit(x=train_X, y=train_Y, epochs=100, verbose=2) #epoch diubah 500 verbose 2

model.save('acc.h5')