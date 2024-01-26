#write a function that counts the frequency of each word in a sentence
import tkinter
from tkinter import *

root = Tk()

root.title("Words frequency count")
root.geometry("1000x700")
root.config(background="#91D8E4")

def check_spelling():
    words= enter_text.get("1.0","end-1c").lower()
    words=words.replace('.',' ')
    words=words.replace(';',' ')
    words=words.replace(':',' ')
    words=words.replace('?',' ')

    
    dict_keys=words.split()
    print(dict_keys)
    #a=TextBlob(words)
    words_count_dict={}
    for key in dict_keys:
        if key in words_count_dict:
            words_count_dict[key]+=1
        else:
            words_count_dict[key]=1
    
    cs=Label(root,text="words count:", font=("Comic Sans MS",20),bg="#91D8E4", fg="#460C68")
    cs.place(x=10, y=350)
    word_count.config(text=words_count_dict)


heading=Label(root, text="Write a sentence to count frequency of words", font=("Comic Sans MS", 20, "bold"), bg="#91D8E4", fg="#460c68")
heading.pack(pady=(50,0))

enter_text =Text(root,bg="white",fg="black",border=2,height="4",width="30", font=("Comic Sans MS", 20,"bold"))
enter_text.pack(pady=10)
enter_text.focus()

Button=Button(root, text="Count",font=("Comic Sans MS", 20,"bold"), bg="#758ED9",fg="white", command=check_spelling)
Button.pack()

word_count=Label(root, text="word count",font=("Comic Sans MS", 10,"bold"), bg="#758ED9",fg="#460C68")
word_count.place(x=10,y=400)
root.mainloop()
