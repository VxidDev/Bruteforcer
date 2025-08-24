import tkinter as tk
import string
from random import choice

window = tk.Tk()
window.resizable(width=False , height=False)
window.geometry("300x400")
window.title("BruteForcer")

window.config(bg="#2d2d2d")

types = ["Whole Word Guess" , "Letter by Letter Guess"]
user_choice = tk.StringVar()
tries_input = tk.StringVar()
word_input = tk.StringVar()
user_choice.set("Select Type Of Bruteforce")

def bruteforce():
    global word , tries, type_chosen
    tries_taken = 0
    for i in range(0 , tries):
        letters = []
        for _ in range(0 , len(word)):
            letters.append(choice(string.ascii_letters))
        word_guess = "".join(letters)
        tries_taken += 1
        if word_guess == word:
            result.config(text=f"{word_guess} took\n {tries_taken}!")
            break
    if word_guess != word:
        result.config(text="Unsuccessful bruteforce try.")
    else:
        pass

def fast_bruteforce():
    global word , tries , type_chosen
    tries_taken = 0
    word_letters = []
    word_guessed_letters = []
    for letter in word:
        word_letters.append(letter)
    for i in range(0 , tries):
        if len(word_letters) > 0:
            tries_taken += 1
            guess = choice(string.ascii_letters)
            if word_letters[0] == guess:
                word_guessed_letters.append(word_letters[0])
                word_letters.pop(0)
            output = "".join(word_guessed_letters)
            print(output)
        else:
            if output == word:
                result.config(text=f"{word_guess} took\n {tries_taken}!")
                break
    if output != word:
        result.config(text="Unsuccessful attempt.")

def submit():
    global tries , word , type_chosen
    try:
        tries = int(tries_entry.get())
        if word_input.get() != "":
            for digit in string.digits:
                if digit not in word_input.get():
                    pass
                else:
                    raise TypeError()
            for punctuation in string.punctuation:
                if punctuation not in word_input.get():
                    pass
                else:
                    raise TypeError()
            word = word_input.get()
        else:
            raise TypeError()
        if user_choice.get() == "Select Type Of Bruteforce":
            raise IndexError()
        else:
            type_chosen = user_choice.get()
        if type_chosen == "Whole Word Guess":
            result.config(text="Working...")
            bruteforce()
        else:
            fast_bruteforce()
            result.config(text="Working...")
    except ValueError:
        tries_input.set("Error!")
    except IndexError:
        word_input.set("Error!")
    except IndexError:
        pass

# GUI
type_choice = tk.OptionMenu(window , user_choice , *types)
type_choice.config(border=0 , highlightthickness=0 , bg="#3a3a3a" , activebackground="#494949" , indicatoron=False , fg="white")
type_choice["menu"].config(bg="#3a3a3a" , border=0 , fg="white" , activebackground="#494949" , tearoff=0)
type_choice.place(x=60 , y=280)

word_entry = tk.Entry(bg="#494949" , border=0 , width=30 , highlightthickness=0 , insertbackground="white" , fg="white" , textvariable=word_input)
word_entry.place(x=50 , y=200)

word_entry_label = tk.Label(bg="#2d2d2d" , fg="White" , text="Word")
word_entry_label.place(x=3 , y=200)

tries_entry = tk.Entry(bg="#494949" , border=0 , width=30 , highlightthickness=0 , insertbackground="white" , fg="white" , textvariable=tries_input)
tries_entry.place(x=50 , y=240)

tries_label = tk.Label(bg="#2d2d2d" , fg="White" , text="Tries")
tries_label.place(x=5 , y=240)

submit_button = tk.Button(bg="#3a3a3a" , fg="White" , text="Submit" , highlightthickness=0 , border=0 ,activebackground="#494949" , command=lambda: submit())
submit_button.place(x=115 , y=320)

result = tk.Label(bg="#2d2d2d" , fg="white" , text="No Task." , font=("arial" , 20 , "bold"))
result.place(x=70 , y=100)

window.mainloop()
