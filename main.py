from datetime import datetime
import math
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("700x80")
window.title("Year progress.")
window.resizable(False, False)

progress_bar = ttk.Progressbar(window, orient="horizontal", length=500, mode="determinate")
progress_bar.pack()

today = datetime.now().date()
day_of_year = today.timetuple().tm_yday


def calculate():
    global today
    global day_of_year
    todayPercent: int = math.floor((day_of_year / 365) * 100)
    tomorrowPercent: int = math.floor(((day_of_year + 1) / 365) * 100)
    print(str(math.floor((day_of_year / 365) * 100)) + f"% of {datetime.now().year}")
    progress_bar["value"] = 0
    progress_bar["maximum"] = 365
    progress_bar["value"] = day_of_year
    window.update_idletasks()
    if todayPercent == tomorrowPercent:
        stats.configure(text=f"{math.floor((day_of_year / 365) * 100)}% of {datetime.now().year} complete.")
    elif todayPercent != tomorrowPercent:
        stats.configure(text=f"{math.floor((day_of_year / 365) * 100)}% of {datetime.now().year} complete. Wait for tomorrow!")


calc_button = tk.Button(window, text="Calculate", command=calculate)
calc_button.pack()
calc_button.place(relx=0.5, rely=0.75, anchor="center")

stats = tk.Label(window, text=f"")
stats.pack()

tk.mainloop()
