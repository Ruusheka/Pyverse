from tkinter import *
import os

# ---------- Functions ----------
def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")

def log_out():
    os.system("shutdown /l")

def shutdown():
    os.system("shutdown /s /t 1")

# ---------- Main Window ----------
st = Tk()
st.title("⚙️ System Control Panel")
st.geometry("950x520")
st.config(bg="#0f172a")  # deep navy background

# ---------- Modern Font ----------
MODERN_FONT = ("Bahnschrift SemiBold", 15)  # clean, geometric, sleek
TITLE_FONT = ("Bahnschrift SemiBold", 28, "bold")

# ---------- Title ----------
Label(
    st,
    text="System Power Options",
    font=TITLE_FONT,
    bg="#0f172a",
    fg="white"
).pack(pady=30)

# ---------- Frame for Buttons ----------
frame = Frame(st, bg="#0f172a")
frame.pack(pady=20)

# ---------- Hover Effect ----------
def on_enter(e):
    e.widget.config(bg="#334155")

def on_leave(e):
    e.widget.config(bg="#1e293b")

# ---------- Button Card Creator ----------
def make_button(parent, text, icon, command):
    card = Frame(parent, bg="#1e293b", width=160, height=160, bd=0, highlightthickness=2, highlightbackground="#334155")
    card.pack(side=LEFT, padx=25)
    card.pack_propagate(False)  # keep square shape

    btn = Button(
        card,
        text=f"{icon}\n{text}",
        font=MODERN_FONT,
        bg="#1e293b",
        fg="white",
        bd=0,
        activebackground="#334155",
        activeforeground="white",
        cursor="hand2",
        command=command
    )
    btn.pack(expand=True, fill=BOTH, padx=8, pady=8)

    # hover animation
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# ---------- Buttons ----------
make_button(frame, "Restart", "🔁", restart)
make_button(frame, "Restart (20s)", "⏱️", restart_time)
make_button(frame, "Log Out", "🔒", log_out)
make_button(frame, "Shut Down", "⏻", shutdown)

# ---------- Footer ----------
Label(
    st,
    text="Created by Ruusheka ⚡",
    font=("Bahnschrift Light", 12),
    bg="#0f172a",
    fg="#94a3b8"
).pack(side="bottom", pady=20)

st.mainloop()
