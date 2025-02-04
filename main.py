import tkinter as tk
from tkinter import Canvas

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

def arect_r(self, x1, y1, x2, y2, radius=25, **kwargs):
    if radius > min(abs(x2 - x1), abs(y2 - y1)) // 2:
        radius = min(abs(x2 - x1), abs(y2 - y1)) // 2
    
    self.create_arc(x1, y1, x1 + 2 * radius, y1 + 2 * radius, start=90, extent=90, **kwargs)
    self.create_arc(x2 - 2 * radius, y1, x2, y1 + 2 * radius, start=0, extent=90, **kwargs)
    self.create_arc(x1, y2 - 2 * radius, x1 + 2 * radius, y2, start=180, extent=90, **kwargs)
    self.create_arc(x2 - 2 * radius, y2 - 2 * radius, x2, y2, start=270, extent=90, **kwargs)
    self.create_rectangle(x1 + radius, y1, x2 - radius, y2, **kwargs)
    self.create_rectangle(x1, y1 + radius, x2, y2 - radius, **kwargs)

Canvas.arect_r = arect_r

def rect(x, y, w, h, thickness=1, color="black", radius=0):
    if radius > 0:
        canvas.arect_r(x, y, x+w, y+h, radius=radius, width=thickness, outline=color)
    else:
        canvas.create_rectangle(x, y, x+w, y+h, width=thickness, outline=color)

def frect(x, y, w, h, color="black", radius=0):
    if radius > 0:
        canvas.arect_r(x, y, x+w, y+h, radius=radius, fill=color, outline="")
    else:
        canvas.create_rectangle(x, y, x+w, y+h, fill=color, outline="")

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

with open("code.py", "r") as file:
    code = file.read()

exec(code)

root.mainloop()