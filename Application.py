import tkinter as tk
from tkinter import filedialog
import spacy

nlp = spacy.load("hr_core_news_sm")

def analyze_text():
    text = text_entry.get("1.0", tk.END)
    doc = nlp(text)
    result_text.delete(1.0, tk.END)
    for ent in doc.ents:
        result_text.insert(tk.END, f"Entitet: {ent.text}, Tip: {ent.label_}\n")

def load_text_file():
    file_path = filedialog.askopenfilename(title="Odaberi tekstualnu datoteku")
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_entry.delete(1.0, tk.END)
            text_entry.insert(tk.END, file.read())

root = tk.Tk()
root.title("Imenovana Entitetska Identifikacija")

text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=10)

analyze_button = tk.Button(root, text="Analiziraj Tekst", command=analyze_text)
analyze_button.pack(pady=5)

load_button = tk.Button(root, text="Učitaj Tekst iz Datoteke", command=load_text_file)
load_button.pack(pady=5)

result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=10)

root.mainloop()



#Kod bez GUI

""" import spacy

nlp = spacy.load("hr_core_news_sm")

with open("neki_tekst.txt", "r", encoding="utf-8") as f:
    text = f.read()

doc = nlp(text)

for ent in doc.ents:
    print(f"Entitet: {ent.text}, Tip: {ent.label_}")

# Mogući tipovi entiteta: PERSON (osoba), ORG (organizacija), LOC (lokacija), itd. """
