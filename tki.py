import random
import tkinter as tk

from content import sentences, sentences_tenses
lesson_sentences = sentences


class HTS:

    def __init__(self):

        def set_sentences():
            global lesson_sentences
            lesson_sentences = sentences

        def set_sentences_tenses():
            global lesson_sentences
            lesson_sentences = sentences_tenses

        self.window = tk.Tk()
        self.menubar = tk.Menu(self.window)
        self.empty_menu = tk.Menu(self.window)

        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label="Close", command=exit)
        self.file_menu.add_command(label="Close2", command=exit)
        self.file_menu.add_separator()
        self.about_menu = tk.Menu(self.menubar, tearoff=0)
        self.about_menu.add_command(label="About", command=exit)
        self.lessons_menu = tk.Menu(self.menubar, tearoff=0)
        self.lessons_menu.add_command(label="basic", command=set_sentences)
        self.lessons_menu.add_command(label="tenses", command=set_sentences_tenses)

        self.menubar.add_cascade(menu=self.file_menu, label="File")
        self.menubar.add_cascade(menu=self.about_menu, label="?")
        self.menubar.add_cascade(menu=self.lessons_menu, label="Lessons")

        self.window.config(menu=self.empty_menu)
        self.is_menu_showed = False

        self.sentence = {'ru': '', 'en': '', 'ua': ''}
        self.sentence_str = ''
        self.bg_color = '#696969'
        self.text_color = '#EEE8AA'
        self.h_text_color = '#747474'

        self.window.configure(background=self.bg_color)

        self.space_label = tk.Label(height=16, width=43, background=self.bg_color)
        self.ru_label = tk.Label(height=4, width=43, text="[     -     ]", background=self.bg_color, fg=self.text_color)
        self.report_label = tk.Label(height=2, width=8, text="report", background=self.bg_color, fg=self.h_text_color)
        self.fav_label = tk.Label(height=2, width=8, text="favorite", background=self.bg_color, fg=self.h_text_color)
        self.en_label = tk.Label(height=4, width=43, background=self.bg_color, fg=self.text_color)
        self.comment_label = tk.Label(height=4, width=43, background=self.bg_color, fg=self.text_color)

        def sentence_text(e):
            self.report_label["text"] = "report"
            self.fav_label["text"] = "favorite"
            self.sentence = random.choice(lesson_sentences)
            self.ru_label["text"] = wrapped(self.sentence.get('ru'))
            self.en_label["text"] = "[     -     ]"
            self.comment_label["text"] = ""

        def report_problem(e):
            self.report_label["text"] = "reported"
            self.fav_label["text"] = "favorite"
            with open('problems.txt', 'a', encoding='utf-8') as fw:
                fw.write(self.sentence_str)

        def to_favorite(e):
            self.report_label["text"] = "report"
            self.fav_label["text"] = "ok"
            with open('favorite.txt', 'a', encoding='utf-8') as fw:
                fw.write(self.sentence_str)

        def translate(e):
            self.report_label["text"] = "report"
            self.fav_label["text"] = "favorite"
            self.en_label["text"] = wrapped(self.sentence.get('en'))
            self.comment_label["text"] = wrapped(self.sentence.get('comment'))

        def show_menu(e):
            menu = self.empty_menu if self.is_menu_showed else self.menubar
            self.is_menu_showed = not self.is_menu_showed
            self.window.config(menu=menu)

        def set_lesson():
            print('lesson')

        self.space_label.grid(row=0, column=0, columnspan=2)
        self.ru_label.grid(row=1, column=0, columnspan=2)
        self.report_label.grid(row=2, column=0)
        self.fav_label.grid(row=2, column=1)
        self.en_label.grid(row=3, column=0, columnspan=2)
        self.comment_label.grid(row=4, column=0, columnspan=2)

        self.ru_label.bind("<Button-1>", sentence_text)
        self.report_label.bind("<Button-1>", report_problem)
        self.fav_label.bind("<Button-1>", to_favorite)
        self.en_label.bind("<Button-1>", translate)
        self.space_label.bind("<Button-1>", show_menu)

        self.window.mainloop()


def wrapped(long_string, line_length=40):
    from textwrap import wrap

    return '\n'.join(wrap(long_string, line_length))


HTS()
