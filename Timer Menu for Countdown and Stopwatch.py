from tkinter import *
import subprocess

root = Tk()
root.title('Timer Menu')
root.geometry('500x500')

# Function to run another Python script
def run_script(script_name):
    subprocess.Popen(['python', script_name])

my_menu = Menu(root)
root.config(menu=my_menu)

# Timer display label
title_label = Label(root, text= 'TIMER MENU', font=('Helvetica', 30))
title_label.pack(pady=1)
title_label = Label(root, text= 'CHOOSE ONE:', font=('Helvetica', 10))
title_label.pack(pady=0)

# Add buttons below the menu
button_frame = Frame(root)
button_frame.pack(pady=200)

button1 = Button(button_frame, text= 'Countdown', command = lambda: run_script('COUNTDOWN_TIMER.py'), width = 20, height = 6)
button1.pack(side=LEFT, padx=50)

button2 = Button(button_frame, text= 'Stopwatch', command = lambda: run_script('Insert file here, nerd!'), width = 20, height = 6)
button2.pack(side=LEFT, padx=50)

root.mainloop()