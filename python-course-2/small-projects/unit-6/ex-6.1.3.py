import tkinter as tk

def handle_button_click():
    image_label.pack()

# Create the main window
window = tk.Tk()
window.geometry("400x300")
window.title("MY DOG!")
label = tk.Label(window, text="How my dog looks like?")
label.pack()
button = tk.Button(window, text="Click Me", command=handle_button_click)
button.pack()
image = tk.PhotoImage(file="image1.png")
image_label = tk.Label(window, image=image)
image_label.config(image = image)



window.mainloop()
