import tkinter

FONT_NAME = "Arial"

wpm = 40
cpm = 40
correct_words = 100


def show_frame(frame):
    frame.tkraise()


def restart():
    pass


# ------------------------- UI SETUP -------------------------------------- #
window = tkinter.Tk()
window.title("Typing Speed Test")
window.config(padx=100, pady=25)
# window.geometry("700x400")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

start_frame = tkinter.Frame(window)
end_frame = tkinter.Frame(window)

for frame in (start_frame, end_frame):
    frame.grid(column=0, row=0, sticky="nsew")

# ----------------- START FRAME -----------------#
title_label = tkinter.Label(start_frame, text="Speed Typing Test", font=(FONT_NAME, 25, "bold"))
title_label.grid(column=0, row=0, columnspan=4, pady=35)

time_left_label = tkinter.Label(start_frame, text="Time Left: ")
time_left_label.grid(column=1, row=1)

counter = tkinter.Label(start_frame, text="60")
counter.grid(column=2, row=1)

restart_button = tkinter.Button(start_frame, text="Restart", width=15, command=restart)
restart_button.grid(column=3, row=1)

words_to_type = tkinter.Text(start_frame, state="disabled", height=5, width=50)
words_to_type.grid(column=0, row=3, columnspan=4, pady=25)

words_entry = tkinter.Entry(start_frame, width=67)
words_entry.grid(column=0, row=5, columnspan=4, pady=15)

# show_frame(start_frame)

# ----------------- END FRAME -----------------#
title_label = tkinter.Label(end_frame, text="Speed Typing Test", font=(FONT_NAME, 20, "bold"))
title_label.grid(column=0, row=0, pady=30)

score_label = tkinter.Label(end_frame, text="Your Score is: ", font=(FONT_NAME, 15, "bold"))
score_label.grid(column=0, row=1, pady=15)

wpm_label = tkinter.Label(end_frame, text=f"{wpm} WPM", font=(FONT_NAME, 12, "bold"))
wpm_label.grid(column=0, row=2)

cpm_label = tkinter.Label(end_frame, text=f"That is {cpm} CPM", font=(FONT_NAME, 12, "bold"))
cpm_label.grid(column=0, row=3)

correct_words = tkinter.Label(end_frame, text=f"Congratulations! You typed {correct_words} words correctly.",
                              font=(FONT_NAME, 12, "bold"))
correct_words.grid(column=0, row=4, pady=15)

window.mainloop()
