import tkinter as tk
import time

root = tk.Tk()
root.title("Digital Clock")

SIZE = 350
root.geometry(f"{SIZE}x{SIZE}")
root.resizable(False, False)
root.configure(bg="#0f172a")  # dark background

frame = tk.Frame(root, bg="#1e293b", bd=0)
frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=300)

title = tk.Label(frame, text="DIGITAL CLOCK", 
                 font=("Arial", 12, "bold"),
                 fg="#94a3b8", bg="#1e293b")
title.pack(pady=(20, 5))

# Time label
time_label = tk.Label(frame, 
                      font=("Arial", 32, "bold"),
                      fg="#38bdf8", bg="#1e293b")
time_label.pack(pady=10)

# Date label
date_label = tk.Label(frame,
                      font=("Arial", 14),
                      fg="#cbd5f5", bg="#1e293b")
date_label.pack()

def update_time():
    current_time = time.strftime("%I:%M:%S %p")  # 12-hour
    current_date = time.strftime("%A, %d %B %Y")

    time_label.config(text=current_time)
    date_label.config(text=current_date)

    root.after(1000, update_time)

update_time()
root.mainloop()
