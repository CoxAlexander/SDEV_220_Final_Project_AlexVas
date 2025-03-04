from tkinter import *
import subprocess
import time

root = Tk()
root.title('Timer Menu')
root.geometry('500x600')

width = 500
height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')



# A function to run another Python script
def run_script(script_name):
    subprocess.Popen(['python', script_name])
    root.destroy()

# A function to update the clock
def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text = 'CURRENT TIME: ' + current_time)
    root.after(1000, update_clock)

my_menu = Menu(root)
root.config(menu = my_menu)

# Timer display label
title_label = Label(root, text = 'TIMER MENU', font = ('Helvetica', 30))
title_label.pack(pady = 1)
title_label = Label(root, text = 'CHOOSE ONE:', font = ('Helvetica', 10))
title_label.pack(pady = 0)

# Adds buttons below the menu
button_frame = Frame(root)
button_frame.pack(pady = 200)

button1 = Button(button_frame, text = 'Countdown', command = lambda: run_script('COUNTDOWN_TIMER.py'), width = 20, height = 6,)
button1.pack(side = LEFT, padx = 50)

button2 = Button(button_frame, text = 'Stopwatch', command = lambda: run_script('stopwatchGui.py'), width = 20, height = 6)
button2.pack(side = LEFT, padx = 50)

# Adds a clock label
clock_label = Label(root, font=('Helvetica', 30))
clock_label.pack(pady = 0)


update_clock()

root.mainloop()