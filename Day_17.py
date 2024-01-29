#write a prgramthat capitalizes the first letter of each word in a sentence
import tkinter
from tkinter import *

root = Tk()

root.title("Capitalize each letter in a sentence")
root.geometry("1000x700")
root.config(background="#91D8E4")

def check_spelling():
    words= enter_text.get("1.0","end-1c")
    words=words.title()
    
    cs=Label(root,text="Result:", font=("Comic Sans MS",20),bg="#91D8E4", fg="#460C68")
    cs.place(x=10, y=350)
    word_title.config(text=words)


heading=Label(root, text="Write a sentence to count frequency of words", font=("Comic Sans MS", 20, "bold"), bg="#91D8E4", fg="#460c68")
heading.pack(pady=(50,0))

enter_text =Text(root,bg="white",fg="black",border=2,height="4",width="30", font=("Comic Sans MS", 20,"bold"))
enter_text.pack(pady=10)
enter_text.focus()

Button=Button(root, text="Convert",font=("Comic Sans MS", 20,"bold"), bg="#758ED9",fg="white", command=check_spelling)
Button.pack()

word_title=Label(root, text="string result",font=("Comic Sans MS", 10,"bold"), bg="#758ED9",fg="#460C68")
word_title.place(x=10,y=400)
root.mainloop()
