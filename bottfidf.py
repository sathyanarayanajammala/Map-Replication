# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 18:25:07 2019

@author: satya
"""


import numpy
import tflearn
import tensorflow
import random
import json

from sklearn.feature_extraction.text import TfidfVectorizer

with open("C:\Chat bot\intents.json") as file:
    data = json.load(file)
    labels = []
    docs_x = []
    docs_y = []
 
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            docs_x.append(pattern)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])
 
    labels = sorted(labels)
 
    #### vectorizer of input 
    cv1= TfidfVectorizer(ngram_range=(1,2))
    x_traincv=cv1.fit_transform(docs_x)
    a = x_traincv.toarray()
    x_traincv=x_traincv.toarray()
    cv1.inverse_transform(a[0])
    
    ###### vectorizer for output
    cv2= TfidfVectorizer(ngram_range=(1,2))
    y_traincv2=cv2.fit_transform(docs_y)
    b= y_traincv2.toarray()
    y_traincv2=y_traincv2.toarray()
    cv2.inverse_transform(b[0])
 
    tensorflow.reset_default_graph()
    
    net = tflearn.input_data(shape=[None, len(x_traincv[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(y_traincv2[0]), activation="softmax")
    net = tflearn.regression(net)
    
    model = tflearn.DNN(net)
    
    model.fit(x_traincv, y_traincv2, n_epoch=1000, batch_size=8, show_metric=True)

def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break
        inp = cv1.transform([inp])
        results = model.predict(inp.toarray())
        
        results_index = numpy.argmax(results)
        tag = labels[results_index]
        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']

        print(random.choice(responses))

chat()    