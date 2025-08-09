import tkinter as tk
from tkinter import simpledialog, messagebox
import random

def random_pastel_color():
    r = random.randint(150, 255)
    g = random.randint(150, 255)
    b = random.randint(150, 255)
    return f'#{r:02x}{g:02x}{b:02x}'

class StickyNotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 Sticky Notes App")
        self.root.geometry("600x400")

        # Create a canvas for gradient background
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack(fill="both", expand=True)

        # Draw vertical gradient on canvas
        for i in range(0, 400):
            c = 255 - int(i * 0.5)
            color = f'#{c:02x}{200:02x}{c:02x}'
            self.canvas.create_line(0, i, 600, i, fill=color)

        # Create a frame on top of the canvas for notes and buttons
        self.main_frame = tk.Frame(root, bg="#f0fff0")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center", width=580, height=380)

        self.notes = []

        self.notes_frame = tk.Frame(self.main_frame, bg="#f0fff0")
        self.notes_frame.pack(fill="both", expand=True, padx=10, pady=10)

        btn_frame = tk.Frame(self.main_frame, bg="#f0fff0")
        btn_frame.pack(pady=10)

        self.add_btn = tk.Button(btn_frame, text="Add Note", command=self.add_note,
                                 font=("Arial", 14), bg="#ffb347", fg="black", padx=15, pady=8)
        self.add_btn.pack(side="left", padx=5)

        self.clear_btn = tk.Button(btn_frame, text="Clear All Notes", command=self.clear_all_notes,
                                   font=("Arial", 14), bg="#ff6961", fg="white", padx=15, pady=8)
        self.clear_btn.pack(side="left", padx=5)

    def add_note(self):
        note_text = simpledialog.askstring("New Note", "Enter note text:", parent=self.root)
        if note_text:
            self.notes.append(note_text)
            self.display_notes()

    def display_notes(self):
        for widget in self.notes_frame.winfo_children():
            widget.destroy()

        for idx, note in enumerate(self.notes):
            bg_color = random_pastel_color()
            frame = tk.Frame(self.notes_frame, bg=bg_color, bd=2, relief="raised", padx=5, pady=5)
            frame.pack(fill="x", pady=5)

            label = tk.Label(frame, text=note, font=("Arial", 14), bg=bg_color, anchor="w", justify="left")
            label.pack(side="left", fill="x", expand=True)

            del_btn = tk.Button(frame, text="Delete", bg="#ff6347", fg="white",
                                command=lambda i=idx: self.delete_note(i))
            del_btn.pack(side="right", padx=5)

    def delete_note(self, index):
        del self.notes[index]
        self.display_notes()

    def clear_all_notes(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to delete all notes?", parent=self.root):
            self.notes.clear()
            self.display_notes()

if __name__ == "__main__":
    root = tk.Tk()
    app = StickyNotesApp(root)
    root.mainloop()
