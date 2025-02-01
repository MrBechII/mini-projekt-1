import tkinter as tk
import time
import math

# Funktion til at opdatere uret
def update_clock():
    # Hent systemtid
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    hours = current_time.tm_hour % 12

    # Beregn vinkler for viserne
    second_angle = 6 * seconds
    minute_angle = 6 * minutes + seconds / 10
    hour_angle = 30 * hours + (minutes / 2)

    # Ryd tidligere tegn
    canvas.delete("all")

    # Skift farve på urrammen ved 12, 3, 6, 9
    if hours == 0:
        frame_color = "#FF6347"  # Tomatrød ved 12
    elif hours == 3:
        frame_color = "#32CD32"  # Limegrøn ved 3
    elif hours == 6:
        frame_color = "#1E90FF"  # Dodgerblå ved 6
    elif hours == 9:
        frame_color = "#FFD700"  # Guld ved 9
    else:
        frame_color = "white"  # Standardfarve (hvid)

    # Tegn urkredsen med farveskift
    canvas.create_oval(50, 50, 350, 350, outline=frame_color, width=5)

    # Tegn minutstreger (ved 5 minutters intervaller)
    for i in range(60):
        angle = math.radians(i * 6)
        x1 = 200 + 140 * math.cos(angle)
        y1 = 200 - 140 * math.sin(angle)
        x2 = 200 + 160 * math.cos(angle)
        y2 = 200 - 160 * math.sin(angle)

        # Skift farve ved 12, 3, 6, 9 (pause drik en øl)
        if i % 15 == 0:
            color = "#FF6347"  # Tomatrød
            if i == 0:
                canvas.create_text(200, 40, text="Pause, drik en øl", fill="white", font=("Helvetica", 12, "bold"))
            elif i == 15:
                canvas.create_text(340, 200, text="Pause, drik en øl", fill="white", font=("Helvetica", 12, "bold"))
            elif i == 30:
                canvas.create_text(200, 360, text="Pause, drik en øl", fill="white", font=("Helvetica", 12, "bold"))
            elif i == 45:
                canvas.create_text(60, 200, text="Pause, drik en øl", fill="white", font=("Helvetica", 12, "bold"))
        else:
            color = "white"
        canvas.create_line(x1, y1, x2, y2, fill=color, width=2)

    # Tegn sekundviser
    second_x = 200 + 140 * math.cos(math.radians(second_angle - 90))
    second_y = 200 + 140 * math.sin(math.radians(second_angle - 90))
    canvas.create_line(200, 200, second_x, second_y, fill="white", width=2)

    # Tegn minutviser
    minute_x = 200 + 120 * math.cos(math.radians(minute_angle - 90))
    minute_y = 200 + 120 * math.sin(math.radians(minute_angle - 90))
    canvas.create_line(200, 200, minute_x, minute_y, fill="white", width=4)

    # Tegn timeviser
    hour_x = 200 + 80 * math.cos(math.radians(hour_angle - 90))
    hour_y = 200 + 80 * math.sin(math.radians(hour_angle - 90))
    canvas.create_line(200, 200, hour_x, hour_y, fill="white", width=6)

    # Opdater uret hvert sekund
    root.after(1000, update_clock)

# Opret hovedvindue
root = tk.Tk()
root.title("Analog Ur")
root.configure(bg="black")

# Opret et canvas til at tegne uret
canvas = tk.Canvas(root, width=400, height=400, bg="black")
canvas.pack()

# Start opdatering af uret
update_clock()

# Start GUI'en
root.mainloop()
