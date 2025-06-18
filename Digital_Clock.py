import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
root.attributes("-fullscreen", True)
root.configure(bg="black")
root.bind("<Escape>", lambda e: root.destroy())

clock_font = ("DS-Digital", 180, "bold")
date_font = ("DS-Digital", 40)

clock_label = tk.Label(root, font=clock_font, fg="#00ffff", bg="black")
clock_label.pack(anchor='center', expand=True)

date_label = tk.Label(root, font=date_font, fg="#00cccc", bg="black")
date_label.pack(anchor='center')

def update_time():
    time_str = strftime('%I:%M:%S %p')
    date_str = strftime('%A, %d %B %Y')
    clock_label.config(text=time_str)
    date_label.config(text=date_str)
    root.after(1000, update_time)

brightness = 255
step = -10

def glow():
    global brightness, step
    color = f'#00{brightness:02x}{brightness:02x}'
    clock_label.config(fg=color)
    brightness += step
    if brightness <= 100 or brightness >= 255:
        step *= -1
    root.after(50, glow)

update_time()
glow()
root.mainloop()