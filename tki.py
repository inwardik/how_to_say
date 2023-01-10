import random
import tkinter as tk
from textwrap import wrap

from content import sentences

sentence = ['', '']
sentence_str = ''
bgcolor = '#696969'
text_color = '#EEE8AA'
h_text_color = '#747474'

window = tk.Tk()
window.configure(background=bgcolor)

space_label = tk.Label(height=16, background=bgcolor)
ru_label = tk.Label(height=4, width=43, text="[     -     ]", background=bgcolor, fg=text_color)
report_label = tk.Label(height=2, width=8, text="report", background=bgcolor, fg=h_text_color)
favorite_label = tk.Label(height=2, width=8, text="favorite", background=bgcolor, fg=h_text_color)
en_label = tk.Label(height=4, width=43, background=bgcolor, fg=text_color)


def sentence_text(e):
    report_label["text"] = "report"
    favorite_label["text"] = "favorite"
    global sentence_str
    global sentence
    sentence = random.choice(sentences)
    # sentence = sentence_str.split(';')
    wrapped_text = '\n'.join(wrap(sentence.get('ru'), 40))
    ru_label["text"] = wrapped_text
    en_label["text"] = "[     -     ]"


def report_problem(e):
    report_label["text"] = "reported"
    favorite_label["text"] = "favorite"
    with open('problems.txt', 'a', encoding='utf-8') as fw:
        fw.write(sentence_str)


def to_favorite(e):
    report_label["text"] = "report"
    favorite_label["text"] = "ok"
    with open('favorite.txt', 'a', encoding='utf-8') as fw:
        fw.write(sentence_str)


def translate(e):
    global sentence
    report_label["text"] = "report"
    favorite_label["text"] = "favorite"
    wrapped_text = '\n'.join(wrap(sentence.get('en'), 40))
    en_label["text"] = wrapped_text


space_label.grid(row=0, column=0)
ru_label.grid(row=1, column=0, columnspan=2)
report_label.grid(row=2, column=0)
favorite_label.grid(row=2, column=1)
en_label.grid(row=3, column=0, columnspan=2)

ru_label.bind("<Button-1>", sentence_text)
report_label.bind("<Button-1>", report_problem)
favorite_label.bind("<Button-1>", to_favorite)
en_label.bind("<Button-1>", translate)

window.mainloop()
