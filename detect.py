import os
import _pickle as c
from sklearn import *
from collections import Counter
from tkinter import *

def load(clf_file):
    with open(clf_file, 'rb') as fp:
        clf = c.load(fp)
    return clf

#loading classifier and dictionary
clf = load("test-classifier.mdl")
d= load("spamdict.dict")

def detect():
    loadinglabel.config(text = "")
    features = []
    inp = entrytext.get("1.0" ,END).split()
    #print(inp)
    if len(inp) == 0:
        loadinglabel.config(text = "Please enter the mail" )

    else:
        for word in d:
            features.append(inp.count(word[0]))
        res = clf.predict([features])
        if res == 0:
            loadinglabel.config(text="Hurray.. It is Not Spam!", fg="#3AED09")
        else:
            loadinglabel.config(text="Beware it is a Spam!", fg="#810E0E")
        submitbttn.config(text="Detect Again")
        entrytext.delete("1.0 ", END)


#main GUI
win  = Tk()
win.geometry("500x500")

win.title("Spam Mail Detector")

win.config(bg = "white")

topframe = Frame(height = 80 ,bg = "#EFF4F3")
topframe.pack(side = TOP ,fill = X)

label  = Label(topframe,text = "Spam Mail Detector" , fg = "#CD3142", bg = "#EFF4F3" , font = 'Times 30 bold')
label.place(x = 80,y=10)

enterlabel = Label(win,text = "Paste the content of the email below" , bg ="white" ,fg ="black" , font = 'Times 13 italic')
enterlabel.place(x = 90,y = 90)


entrytext = Text(win, bd = 3, height = 10,width = 40,padx = 12,pady = 12 ,bg ="#EFF4F3")
entrytext.place(x = 80, y = 130 )

loadinglabel = Label(win,text = "",bg ="white" ,font = 'Times 15 bold')
loadinglabel.place(x = 150, y = 320)

submitbttn = Button(win,text = "Detect" , height = 2,width  =15 ,font = 'Times 13 bold', fg = "#EFF4F3" , bg = "#CD3142",activebackground = "#098273" ,activeforeground = "white" ,command = detect)
submitbttn.place(x = 180,y = 360)

win.mainloop()

