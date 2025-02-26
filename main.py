from tkinter import *
from PIL import Image, ImageTk

FONT = ('Ubuntu', 14, 'bold')

TIMER_COUNTER = 10
TIME_LEFT = TIMER_COUNTER
TIMER = None
PREVIOUS_TEXT = ''


def reset_timer():
    if TIMER != None:
        window.after_cancel(TIMER)


def timer(time):
    global TIMER
    global TIME_LEFT
    if time > 0:
        TIME_LEFT = time
        canva.itemconfig(time_text, text=f'Do not stop writing! Time left: {time} s')
        if check():
            TIMER = window.after(1000, timer, time - 1)
        else:
            reset_timer()
            timer(TIMER_COUNTER)
    else:
        canva.itemconfig(time_text, text='Time is up!\nClick button or hit enter to restart')
        text_area.delete('1.0', 'end')
        reset_timer()


def check():
    if text_area.get('1.0', 'end') != PREVIOUS_TEXT:
        set_previous()
        return False
    else:
        set_previous()
        return True


def set_previous():
    global PREVIOUS_TEXT
    PREVIOUS_TEXT = text_area.get('1.0', 'end')


def start(event=None):
    text_area.delete('1.0', 'end')
    text_area.focus()
    reset_timer()
    timer(TIMER_COUNTER)


window = Tk()
window.title('Disappearing Text Writing APP ~gumissek')
window.config(background='white')

# images
# image_hand=Image.open('hand.png')
# image_hand= image_hand.resize((100,100))
# image_hand_tk=ImageTk.PhotoImage(image_hand)

image_text = Image.open('speedup.png')
image_text = image_text.resize((400, 200))
image_text_tk = ImageTk.PhotoImage(image_text)

canva = Canvas(width=400, height=210, background='white')
canva.config(highlightthickness=0)
canva.create_image(200, 100, image=image_text_tk)
# canva.create_image(100, 210, image=image_hand_tk)
time_text = canva.create_text(163, 188, text='Click button or hit enter to start!', font=FONT)
canva.pack()

text_area = Text(window, height=10, width=50)
text_area.pack()
button_start = Button(text='Start', command=start, font=FONT)
button_start.pack()

window.bind('<Return>', start)

window.mainloop()

# https://github.com/gumissek/app_Disappearing_Text_Writing
