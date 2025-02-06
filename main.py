import tkinter as tk
from tkinter import Canvas
import os

root = tk.Tk()
root.title("LinesPy 1")
root.geometry("598x612")
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)
canvasWidth = root.winfo_screenwidth()
canvasHeight = root.winfo_screenheight()

def update_dimensions():
    global canvasWidth, canvasHeight
    canvasWidth = canvas.winfo_width()
    canvasHeight = canvas.winfo_height()

def cls(color="white"):
    canvas.delete("all")
    canvas.create_rectangle(0, 0, canvasWidth, canvasHeight, fill=color, outline="")

def plot(x, y, color="black"):
    canvas.create_line(x, y, x+1, y, fill=color)

def line(x1, y1, x2, y2, thickness=1, color="black", cap="butt"):
    canvas.create_line(x1, y1, x2, y2, width=thickness, fill=color, capstyle=cap)

def rect(x, y, w, h, thickness=1, color="black", radius=0):
    if radius > 0:
        radius = min(radius, w // 2, h // 2)
        canvas.create_arc(x, y, x + 2 * radius, y + 2 * radius, start=90, extent=90, outline=color, width=thickness, style=tk.ARC)
        canvas.create_arc(x + w - 2 * radius, y, x + w, y + 2 * radius, start=0, extent=90, outline=color, width=thickness, style=tk.ARC)
        canvas.create_arc(x, y + h - 2 * radius, x + 2 * radius, y + h, start=180, extent=90, outline=color, width=thickness, style=tk.ARC)
        canvas.create_arc(x + w - 2 * radius, y + h - 2 * radius, x + w, y + h, start=270, extent=90, outline=color, width=thickness, style=tk.ARC)
        canvas.create_line(x + radius, y, x + w - radius, y, fill=color, width=thickness)
        canvas.create_line(x + radius, y + h, x + w - radius, y + h, fill=color, width=thickness)
        canvas.create_line(x, y + radius, x, y + h - radius, fill=color, width=thickness)
        canvas.create_line(x + w, y + radius, x + w, y + h - radius, fill=color, width=thickness)
    else:
        canvas.create_rectangle(x, y, x+w, y+h, width=thickness, outline=color)

def frect(x, y, w, h, color="black", radius=0):
    if radius > 0:
        radius = min(radius, w // 2, h // 2)
        canvas.create_arc(x, y, x + 2 * radius, y + 2 * radius, start=90, extent=90, fill=color, outline=color)
        canvas.create_arc(x + w - 2 * radius, y, x + w, y + 2 * radius, start=0, extent=90, fill=color, outline=color)
        canvas.create_arc(x, y + h - 2 * radius, x + 2 * radius, y + h, start=180, extent=90, fill=color, outline=color)
        canvas.create_arc(x + w - 2 * radius, y + h - 2 * radius, x + w, y + h, start=270, extent=90, fill=color, outline=color)
        canvas.create_rectangle(x + radius, y, x + w - radius, y + h, fill=color, outline=color)
        canvas.create_rectangle(x, y + radius, x + w, y + h - radius, fill=color, outline=color)
    else:
        canvas.create_rectangle(x, y, x+w, y+h, fill=color, outline=color)

def circle(x, y, r, thickness=1, color="black"):
    canvas.create_oval(x-r, y-r, x+r, y+r, width=thickness, outline=color)

def fcircle(x, y, r, color="black"):
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=color, outline="")

def print(text, x=0, y=0, size=12, color="black", anchor="no", blink=0):
    mapping = {
        "no": "nw", "nc": "n", "ne": "ne",
        "co": "w", "cc": "center", "ce": "e",
        "so": "sw", "sc": "s", "se": "se"
    }
    anchor = mapping.get(anchor, "nw")
    canvas.create_text(x, y, text=text, fill=color, font=("Helvetica", size), anchor=anchor)

def input(prompt, x=0, y=0, size=12, color="black", anchor="no", width=10):
    frame = tk.Frame(root, bg="white")
    frame.place(x=x, y=y)

    label = tk.Label(frame, text=prompt, bg="white", fg=color, font=("Helvetica", size))
    label.pack(side="left")

    entry_var = tk.StringVar()
    entry = tk.Entry(frame, textvariable=entry_var, width=width)
    entry.pack(side="left")
    entry.focus_set()

    def on_enter(event=None):
        frame.destroy()
        root.quit()
    
    entry.bind('<Return>', on_enter)
    root.wait_window(frame)
    return entry_var.get()

def pause(t):
    root.after(t, root.quit)
    root.mainloop()
    root.update()

def key(key):
    return root.bind_all("<KeyPress-%s>" % key)

script_dir = os.path.dirname(os.path.abspath(__file__))
access = os.path.join(script_dir, "code.py")

if os.path.exists(access):
    with open(access, "r") as file:
        code_content = file.read()

    exec(code_content, globals())
else:
    print("code.py not found in the same directory as main.py", 200, 200, size=20, color="black", anchor="no", blink=0)

root.mainloop()
