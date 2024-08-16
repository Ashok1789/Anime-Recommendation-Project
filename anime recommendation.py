
import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import random

def generate_text():
    input_text = entry.get()  # Get input text from the Entry widget
    if input_text:
        output_text = generator(input_text, max_length=100)[0]["generated_text"]
        output_label.config(state=tk.NORMAL)
        output_label.delete(1.0, tk.END)  # Clear previous output
        output_label.insert(tk.END, output_text)
        output_label.config(state=tk.DISABLED)
        status_var.set("Text generated successfully.")
    else:
        status_var.set("Please enter some text before generating.")

def save_output():
    output_text = output_label.get(1.0, tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(output_text)
        messagebox.showinfo("Save Successful", "Output text saved successfully!")
        status_var.set(f"Output saved to {file_path}.")

def clear_input():
    entry.delete(0, tk.END)
    status_var.set("Input cleared.")

def clear_output():
    output_label.config(state=tk.NORMAL)
    output_label.delete(1.0, tk.END)
    output_label.config(state=tk.DISABLED)
    status_var.set("Output cleared.")

def generate_random_text():
    random_texts = [
        "Once upon a time...",
        "In a galaxy far, far away...",
        "It was a dark and stormy night...",
        "To be or not to be, that is the question...",
        "In the beginning, God created the heavens and the earth..."
    ]
    random_text = random.choice(random_texts)
    entry.delete(0, tk.END)
    entry.insert(tk.END, random_text)
    status_var.set("Random text generated.")

def toggle_theme():
    current_theme = root.tk_setPalette()  # Get the current theme
    if "light" in current_theme:
        root.tk_setPalette("dark")
        status_var.set("Dark theme applied.")
    else:
        root.tk_setPalette("light")
        status_var.set("Light theme applied.")

root = tk.Tk()
root.title("Text Generation")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=lambda: messagebox.showinfo("Not Implemented", "File opening not implemented yet"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

label = tk.Label(input_frame, text="Enter input text:")
label.pack(side=tk.LEFT, padx=5)

entry = tk.Entry(input_frame, width=50, font=("Arial", 12))
entry.pack(side=tk.LEFT, padx=5)

button = tk.Button(root, text="Generate Text", command=generate_text)
button.pack(pady=10)

output_frame = tk.Frame(root)
output_frame.pack()

output_label = scrolledtext.ScrolledText(output_frame, width=60, height=10, wrap=tk.WORD, state=tk.DISABLED, font=("Arial", 12))
output_label.pack(padx=10, pady=10)

save_button = tk.Button(root, text="Save Output", command=save_output)
save_button.pack(side=tk.LEFT, padx=5)

clear_input_button = tk.Button(root, text="Clear Input", command=clear_input)
clear_input_button.pack(side=tk.LEFT, padx=5)

clear_output_button = tk.Button(root, text="Clear Output", command=clear_output)
clear_output_button.pack(side=tk.LEFT, padx=5)

random_text_button = tk.Button(root, text="Random Text", command=generate_random_text)
random_text_button.pack(side=tk.LEFT, padx=5)

theme_button = tk.Button(root, text="Toggle Theme", command=toggle_theme)
theme_button.pack(side=tk.RIGHT, padx=5)

status_var = tk.StringVar()
status_bar = tk.Label(root, textvariable=status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

model_path = r"C:\Users\ashok\OneDrive\Desktop\demo\dataset\model"
model = AutoModelForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

root.mainloop()



import numpy as np
import re
from PyPDF2 import PdfReader
import os
import docx
def read_documents_from_file(file_path):
    with open(r"C:\Users\ashok\OneDrive\Desktop\demo\dataset\dataset", 'r', encoding='utf-8', errors='ignore') as file:
        text = file.read()
    return text
file_path = (r"C:\Users\ashok\OneDrive\Desktop\demo\dataset\dataset")
text_data = read_documents_from_file(file_path)
text_data = re.sub(r'\n+', '\n', text_data).strip()
with open(r"C:\Users\ashok\OneDrive\Desktop\demo\dataset\dataset", "r",encoding="utf-8", errors = "replace") as file:
    text_data = file.read()
from transformers import AutoModelForCausalLM,AutoTokenizer
model_path =  (r"C:\Users\ashok\OneDrive\Desktop\demo\dataset\model")
model = AutoModelForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)