from tkinter import *
from tkinter import filedialog, messagebox
import time

# ---------------------------- INITIAL PARAMETERS --------------------- #
FONT_NAME = "Arial"
WHITE = "#ecf4f3"
LBLUE = "#68b0ab"
DBLUE = "#006a71"
ORANGE = "#ff7e67"


# ---------------------------- START GAME -------------------- #
def start_game():
    global event_no

    event_no = 0
    header_label.config(text="Disappearing Text App")
    subheader_label.grid_forget()
    start_button.grid_forget()
    save_button.grid_forget()
    restart_button.grid_forget()
    exit_button.grid_forget()
    text_canvas.itemconfig(test_text, text="If you stop typing for 5 seconds, your text will disappear. Let's begin!")
    text_canvas.grid(column=0, row=1)
    user_input.grid(column=0, row=2)


# ---------------------------- IDENTIFY KEY PRESS ---------------- #
def key_press(event):
    global last_pressed, event_no

    last_pressed = time.time()

    event_no += 1
    if event_no == 1:
        timer()


# --------------------- CHECK TIME SINCE EVENT LESS THAN 5 SEC -------------- #
def timer():
    global last_pressed

    count = time.time() - last_pressed
    if count < 5:
        window.after(100, timer)
    else:
        collect_output()


# --------------------- COLLECT INFO FROM TEXT BOX ------------------------ #
def collect_output():
    global user_output

    user_output = user_input.get(1.0, END)

    user_input.delete(1.0, END)
    user_input.grid_forget()
    save_button.grid(column=0, row=2, pady=10)
    restart_button.grid(column=0, row=3, pady=10)
    exit_button.grid(column=0, row=4, pady=10)
    text_canvas.itemconfig(test_text, text="Time's up!!! Thanks for using the Disappearing Text App.")


# -------------------- SAVE TEXT BOX INFO IN FILE --------------------------- #
def save_as():
    global user_output

    filename = filedialog.asksaveasfilename(initialdir="/",
                                            title="Save as .txt",
                                            filetypes=[("Text files", "*.txt")],
                                            defaultextension=".txt")

    if filename:
        with open(filename, "w") as output:
            output.write(user_output)
            messagebox.showinfo(title="Save Complete",
                                message=f"Your file has been saved in the following location:\n{filename}")


# ----------------------- EXIT APP -------------------------------- #
def exit_function():
    msgbox = messagebox.askquestion(title="Exit Application",
                                    message="Are you sure you want to exit the application?",
                                    icon='warning')
    if msgbox == 'yes':
        window.destroy()


# ---------------------------- UI SETUP ---------------------- #
window = Tk()
window.title("Disappearing Text App")
window.config(padx=100, pady=50, bg=WHITE)

header_label = Label(text="Welcome to the Disappearing Text App", bg=WHITE, fg=DBLUE, font=(FONT_NAME, 30, "bold"))
subheader_label = Label(text="Don't stop writing or your progress will be lost!", bg=WHITE, fg=LBLUE, font=(FONT_NAME, 12, "bold"))
start_button = Button(text="Start", command=start_game, bg=ORANGE, fg=WHITE, highlightthickness=0, font=(FONT_NAME, 25, "bold"), width=20)
header_label.grid(column=0, row=0, pady=30)
subheader_label.grid(column=0, row=1, pady=30)
start_button.grid(column=0, row=2, pady=30)

text_canvas = Canvas(width=800, height=100, highlightthickness=0, bg=WHITE)
test_text = text_canvas.create_text(400, 50,
                                    width=800,
                                    text="",
                                    fill=LBLUE,
                                    font=(FONT_NAME, 12, "bold"))
user_input = Text(width=100, height=20, highlightthickness=0, fg=DBLUE, font=(FONT_NAME, 10, "normal"))

save_button = Button(text="Save Output", bg=ORANGE, fg=WHITE, command=save_as, highlightthickness=0, font=(FONT_NAME, 12, "bold"), width=15)
restart_button = Button(text="Restart", bg=ORANGE, fg=WHITE, command=start_game, highlightthickness=0, font=(FONT_NAME, 12, "bold"), width=15)
exit_button = Button(text="Exit", bg=ORANGE, fg=WHITE, command=exit_function, highlightthickness=0, font=(FONT_NAME, 12, "bold"), width=15)

user_input.bind("<Key>", key_press)
window.mainloop()


