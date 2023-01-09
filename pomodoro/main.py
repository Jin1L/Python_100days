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
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(TIMER)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    global REPS
    REPS = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1

    work_secs = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 2 == 1:
        count_down(work_secs)
        timer_label.config(text="Work", fg=RED)
    elif REPS % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=PINK)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(REPS/2)):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)




timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_bt = Button(text="Start", highlightthickness=0, command=start_timer)
start_bt.grid(column=0, row=2)

reset_bt = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_bt.grid(column=2, row=2)




window.mainloop()