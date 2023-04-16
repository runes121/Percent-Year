from datetime import datetime
import math
import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(themename="darkly")
window.geometry("700x100")
window.title("Year progress.")
window.resizable(False, False)

progress_bar = ttk.Progressbar(window, orient="horizontal", length=500, mode="determinate")
progress_bar.pack()
progress_bar.place(relx=0.5, rely=0.2, anchor="center")

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

    for i in range(day_of_year+1):
        progress_bar["value"] = i
        print(f"Day of year: {day_of_year}")
        print(i)
        window.update_idletasks()

    if todayPercent == tomorrowPercent:
        stats.configure(text=f"{math.floor((day_of_year / 365) * 100)}% of {datetime.now().year} complete.")
    elif todayPercent != tomorrowPercent:
        stats.configure(text=f"{math.floor((day_of_year / 365) * 100)}% of {datetime.now().year} complete. Wait for tomorrow!")


calc_button = ttk.Button(window, text="Calculate", command=calculate)
calc_button.pack()
calc_button.place(relx=0.5, rely=0.75, anchor="center")

stats = ttk.Label(window, text="")
stats.pack()
stats.place(relx=0.5, rely=0.4, anchor="center")

tk.mainloop()
