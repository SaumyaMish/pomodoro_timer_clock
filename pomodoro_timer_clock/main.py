from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
BOLD_GREEN ="#147864"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repeat = 0
timer =None

# ---------------------------- TIMER RESET ------------------------------- # 

# Reset Button
def reset_btn_action():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_lbl.config(text="Timer")

    global repeat
    count_lbl.config(text="")
    repeat = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
        global repeat
        repeat+=1
        if repeat % 8 == 0:
            mn = LONG_BREAK_MIN
            timer_lbl.config(text="Break",fg=RED)

        elif (repeat % 2) == 0:
            mn = SHORT_BREAK_MIN
            timer_lbl.config(text="Break",fg=PINK)

        else:
            mn = WORK_MIN
            timer_lbl.config(text="Work",fg=GREEN)

        if repeat>9:
            repeat = 0
            return 0
        count = mn *60
        count_down(count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minute = count//60
    count_sec = count%60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_minute < 10:
        count_minute = f"0{count_minute}"

    if count< 0:
        start_timer()

        # update check mark sign after every "25 minute work and  5 minutes break"
        mark = ""
        session_count = repeat//2
        for i in range(session_count):
            mark += "✔"
        count_lbl.config(text=f"{mark}")

    else:
        canvas.itemconfig(timer_text, text=f"{count_minute}:{count_sec}")
        global timer
        timer= window.after(1000,count_down, count-1)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=20,bg=YELLOW)

# add timer Label on screen
timer_lbl = Label(text="Timer",fg=GREEN,font=(FONT_NAME,35,"bold"),bg=YELLOW)
timer_lbl.grid(column=1,row=0 )


# add image in background
bg = PhotoImage(file="tomato.png")
canvas = Canvas(width=200,height=230,bg=YELLOW,highlightthickness=0  )
canvas.create_image(100,118,image=bg)

# add timer on screen
timer_text = canvas.create_text(100,150,text="00:00",font=(FONT_NAME,35,"bold"),fill='white')
canvas.grid(column=1,row=1)


# add count label on screen
count_lbl = Label(fg=BOLD_GREEN,font=(FONT_NAME,15,"bold"),bg=YELLOW )
count_lbl.grid(column=1,row=4)


# start button
def start_btn_action():
    start_timer()

start_btn = Button(text="Start",command=start_btn_action,highlightthickness=0 )
start_btn.grid(column=0,row=2)


reset_btn = Button(text="Reset", command= reset_btn_action,highlightthickness=0)
reset_btn.grid(column=2,row=2)


window.mainloop()
