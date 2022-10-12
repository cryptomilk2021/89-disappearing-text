from tkinter import *

time_to_go = 5

window = Tk()
window.title("disappearing text")
window.minsize(width=800, height=600)
window.config(padx=50, pady=50)

# Labels
padx = 50
pady = 20

label_time_left = Label(text="time left: 0")
label_time_left.grid(row=0, column=2)
label_time_left.config(padx=padx, pady=pady)


def letter_pressed(event):
    global time_to_go
    time_to_go = 5
    label_time_left.config(text=f"time left: {str(time_to_go)}")


type_text = Text(width=50, height=10, wrap='word', font=("Arial", 20))
# type_text.insert('1.0', split_list)
# type_text['state'] = 'disabled'
type_text.grid(row=1, column=1)
type_text.bind('<Key>', letter_pressed)
type_text.focus_set()


def timer():
    global time_to_go
    time_to_go -= 1
    if time_to_go < 0:
        type_text.delete('1.0', END)
        type_text.focus_set()
        time_to_go = 5
    label_time_left.config(text=f"time left: {str(time_to_go)}")

    window.after(1000, timer)




window.after(1000, timer)
window.mainloop()
