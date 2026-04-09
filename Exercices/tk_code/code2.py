import tkinter as tk

root = tk.Tk()

# Label
label = tk.Label(root, text="Nom :")
label.grid(row=0, column=0, padx=5, pady=5)

# Entry
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)

# Text (multiligne)
text = tk.Text(root, height=5, width=30)
text.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Button
def get_text():
    print(f"Nom: {entry.get()}")
    print(f"Message: {text.get('1.0', tk.END)}")

button = tk.Button(root, text="Valider", command=get_text)
button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()