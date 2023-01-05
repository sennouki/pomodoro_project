import tkinter.messagebox
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
countdown = None
# ---------------------------- WINDOW POP ------------------------------- #
def focus_window(option):
    if option == "on":
        window.deiconify()
        window.focus_force()
        window.attributes('-topmost', 1)
    elif option == "off":
        window.attributes('-topmost', 0)
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    start.config(state="normal")
    reset.config(state="disabled")
    global REPS
    window.after_cancel(countdown)
    REPS = 0
    checkmark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global REPS
    REPS += 1
    start.config(state="disabled")
    reset.config(state="normal")

    working_rep = WORK_MIN * 60
    short_break_rep = SHORT_BREAK_MIN * 60
    long_break_rep = LONG_BREAK_MIN * 60
    if REPS % 8 == 0:
        focus_window("on")
        tkinter.messagebox.showinfo(title="Long breakkie!", message="20 mins for ya!")
        count_down(long_break_rep)
        timer.config(text="Break", fg=GREEN)
    elif REPS % 2 == 0:
        focus_window("on")
        tkinter.messagebox.showinfo(title="Breakkie time!", message="5 mins for ya!")
        count_down(short_break_rep)
        timer.config(text="Break", fg=PINK)
    else:
        focus_window("off")
        tkinter.messagebox.showinfo(title="Work, work, work", message="Start working!")
        count_down(working_rep)
        timer.config(text="Work", fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global REPS
    minutes_timer = math.floor(count / 60)
    seconds_timer = count % 60
    if 0 <= seconds_timer <= 9:
        seconds_timer = f"0{seconds_timer}"
    canvas.itemconfig(timer_text, text=f"{minutes_timer}:{seconds_timer}")

    if count > 0:
        global countdown
        countdown = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(REPS/2)
        for _ in range(work_session):
            marks += "✔"
        checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer.grid(column=1, row=0)
start = Button(text="Start", command=start_timer, state="normal")
start.grid(column=0, row=2)
reset = Button(text="Reset", command=reset_timer, state="disabled")
reset.grid(column=2, row=2)
checkmark = Label(fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
