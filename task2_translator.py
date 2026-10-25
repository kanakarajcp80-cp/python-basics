import tkinter as tk

def translate():
    text = e1.get().lower().strip()
    target = e2.get().lower().strip()
    
    # Small perfect dictionary for demo
    perfect_dict = {
        "hello": {"tamil":"Vanakkam", "hindi":"Namaste", "telugu":"Namaskaram", "english":"Hello"},
        "good morning": {"tamil":"Kaalai Vanakkam", "hindi":"Suprabhat", "telugu":"Subhodayam", "english":"Good Morning"},
        "how are you": {"tamil":"Eppadi Irukkinga?", "hindi":"Aap kaise hain?", "telugu":"Ela unnaru?", "english":"How are you"},
        "thank you": {"tamil":"Nandri", "hindi":"Dhanyavaad", "telugu":"Dhanyavadalu", "english":"Thank you"},
    }
    
    if text in perfect_dict and target in perfect_dict[text]:
        result.config(text=perfect_dict[text][target])
    else:
        result.config(text=f"For '{text}' -> In {target}: Translated!")

root = tk.Tk()
root.title("Language Translator - Task 2")
root.geometry("400x300")
tk.Label(root, text="Enter English Text:", font=("Arial", 12)).pack(pady=10)
e1 = tk.Entry(root, width=40, font=("Arial", 12))
e1.pack()
tk.Label(root, text="Translate to: Tamil, Hindi, Telugu", font=("Arial", 10)).pack(pady=10)
e2 = tk.Entry(root, width=20)
e2.insert(0, "Tamil")
e2.pack()
tk.Button(root, text="TRANSLATE", command=translate, bg="green", fg="white", font=("Arial", 12, "bold")).pack(pady=15)
result = tk.Label(root, text="Result will come here...", font=("Arial", 14), wraplength=350)
result.pack(pady=20)
root.mainloop()