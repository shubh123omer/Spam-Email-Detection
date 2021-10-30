import os
from collections import Counter
# Above library is used to count frequency of words which appear in the dataset.
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
import _pickle as c
# this is used to save our files created so we dont have to create them again and again.
import matplotlib.pyplot as plt


#this function saves our file using pickle library
def save(clf, name):
    with open(name, 'wb') as fp:
        c.dump(clf, fp)
    print("saved")

#this will create a dictionary of words used in our data and will return most common 3000 words.
def make_dict():
    direc = "emails/"
    files = os.listdir(direc)  # returns a list containing the names of the files in this directory

    emails = [direc + email for email in files]  # this list contains all the files, basically appending paths
    # print(emails)

    words = []
    length = len(emails)
    #this function will give ll the words present in the data used.
    for email in emails:
        f = open(email, errors="ignore")
        currfile = f.read()
        words += currfile.split(" ")
        print(length)
        length -= 1


    for i in range(len(words)):
        if words[i].isalpha() == False or len(words[i]) <= 1:  # deleting all those characters which are not alphabets
            words[i] = ""

    dictionary = Counter(words)
    del dictionary[""]
    #print(dictionary)
    return dictionary.most_common(3000)

#this function will create our dataset required
def make_dataset(dictionary):
    direc = "emails/"
    files = os.listdir(direc)

    emails = [direc + email for email in files]

    feature_set = []
    labels = []
    length = len(emails)
    for email in emails:
        data  = []
        f = open(email, errors ="ignore")
        words = f.read().split(' ')
        for entry in dictionary:
            data.append(words.count(entry[0]))
        print(data)
        feature_set.append(data)
        if "ham" in email:
            labels.append(0)
        if "spam" in email:
            labels.append(1)
        print(length)
        length -= 1
    return feature_set,labels

d = make_dict()
save(d,"spamdict.dict")
features , labels = make_dataset(d)




x_train,x_test, y_train , y_test = tts(features , labels , test_size=0.2)
clf = MultinomialNB()

clf.fit(x_train, y_train)

preds = clf.predict(x_test)

print(accuracy_score(y_test,preds))

save(clf, "test-classifier.mdl")

