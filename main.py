from tkinter import *

STORY = ''
TIMER_COUNTER = 10
TIME_LEFT=TIMER_COUNTER
TIMER = None


#ogarnc jak dziala ten timer zeby sprawdzalo w petli


def timer(time):
    global TIMER
    global TIME_LEFT
    if time > 0:
        TIME_LEFT = time
        canva.itemconfig(time_text, text=time)
        check()
        TIMER = window.after(1000, timer, time - 1)


    else:
        canva.itemconfig(time_text, text='Czas koniec')
        text_area.delete(0, 'end')
        reset_timer()



def reset_timer():
    if TIMER != None:
        window.after_cancel(TIMER)


def check():
    if text_area.get() == STORY:
        canva.itemconfig(message, text='to samo co porzednio')
        set_story()
        # return True
    else:
        canva.itemconfig(message, text='inne')
        set_story()
        reset_timer()
        timer(TIMER_COUNTER)
        # return False




def set_story():
    global STORY
    STORY = text_area.get()


def start():
    reset_timer()
    timer(TIMER_COUNTER)





window = Tk()
window.title('teskt')
window.config(padx=30, pady=30)

canva = Canvas(width=500, height=200, background='lightyellow')
canva.config(highlightthickness=0)
time_label = canva.create_text(220, 100, text='Time: ')
time_text = canva.create_text(250, 100, text='0')
message = canva.create_text(250, 70)
canva.pack()
text_area = Entry()
text_area.pack()
button_start = Button(text='Rozpocznij', command=start)
button_start.pack()

# window.bind('<Return>',check)

window.mainloop()
