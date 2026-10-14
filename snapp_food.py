from sklearn.metrics import confusion_matrix,classification_report
import pandas as pd 
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
import tkinter as tk 
from PIL import Image,ImageTk




def pre ():
    global im 
    entry = en.get()
    p = model.predict(tf.transform([entry]))[0]
    if p == "HAPPY" :
        im = ImageTk.PhotoImage(Image.open("1.ico").resize((100,100)))
        label = tk.Label(w,image=im,bg="midnightblue")
        label.place(x=150,y=40)

    if p == "SAD" :
        im = ImageTk.PhotoImage(Image.open("3.ico").resize((100,100)))
        label = tk.Label(w,image=im,bg="midnightblue")
        label.place(x=150,y=40)

data = pd.read_csv("snapfood_train(1).csv")

x=data["comment"]
y=data["label"]

tf = TfidfVectorizer(ngram_range=(1,3),min_df=1,max_df=0.98)

xx= tf.fit_transform(x)

len(xx[8].toarray()[0])

model = LinearSVC()
model.fit(xx,y)

d_test = pd.read_csv("snapfood_test(1).csv")

o = []

for i in range(9033):
    p = model.predict(tf.transform([d_test["comment"].iloc[i]]))
    o.append(p[0])
o



d_test["prediction"]=o
d_test.to_excel("test.xlsx",index=False)

predictions=d_test["prediction"].values
truth=d_test["label"].values


print(classification_report(truth,predictions))


w = tk.Tk()

w.geometry("500x200")
w.title("text")
w.config(bg="midnightblue")

en = tk.Entry()
en.place(x=23,y=50)

la=tk.Label(text="Please enter a text : ",fg="lightgoldenrod1",bg="midnightblue", font=("Britannic Bold",12))
la.place(x=20,y=20)

but = tk.Button(text="Enter", font=("Britannic Bold",10),bg="lightgoldenrod1",command=pre)
but.place(x=60,y=70)




w.mainloop()