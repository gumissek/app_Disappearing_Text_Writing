import tkinter
from tkinter import *

STORY = ''
TIMER_COUNTER = 10
TIME_LEFT = TIMER_COUNTER
TIMER = None


# ogarnc jak dziala ten timer zeby sprawdzalo w petli
def reset_timer():
    if TIMER != None:
        window.after_cancel(TIMER)


def timer(time):
    global TIMER
    global TIME_LEFT
    if time > 0:
        TIME_LEFT = time
        canva.itemconfig(time_text, text=f'{time} s')
        if check():
            TIMER = window.after(1000, timer, time - 1)
        else:
            reset_timer()
            timer(TIMER_COUNTER)
    else:
        canva.config(background='lightpink')
        canva.itemconfig(time_text, text='Time is up!')
        text_area.delete('1.0','end')
        reset_timer()


def check():
    if text_area.get('1.0',tkinter.END) != STORY:
        set_story()
        return False
    else:
        set_story()
        return True


def set_story():
    global STORY
    STORY = text_area.get('1.0','end')


def start(event=None):
    canva.config(background='lightyellow')
    text_area.delete('1.0','end')
    text_area.focus()
    reset_timer()
    timer(TIMER_COUNTER)


window = Tk()
window.title('Disappearing Text Writing APP')
window.config(padx=30, pady=30)

canva = Canvas(width=400, height=200, background='white')
canva.config(highlightthickness=0)
time_label = canva.create_text(200, 100, text='Time: ')
time_text = canva.create_text(250, 100, text='0')
canva.pack()
text_area = Text(window,height=10,width=50)
text_area.pack()
button_start = Button(text='Click or hit Enter:', command=start)
button_start.pack()

window.bind('<Return>', start)

window.mainloop()
