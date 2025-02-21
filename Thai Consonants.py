import tkinter as tk
import random

# Thai consonants and their names
thai_consonants = {
    "ก": "กอ ไก่", "ข": "ขอ ไข่", "ฃ": "ฃอ ขวด",
    "ค": "คอ ควาย", "ฅ": "ฅอ คน", "ฆ": "ฆอ ระฆัง",
    "ง": "งอ งู", "จ": "จอ จาน", "ฉ": "ฉอ ฉิ่ง",
    "ช": "ชอ ช้าง", "ซ": "ซอ โซ่", "ฌ": "ฌอ เฌอ"
}

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        self.root.geometry("300x200")
        
        self.current_consonant = None
        self.is_flipped = False

        # Flashcard Button
        self.card = tk.Button(
            root, text="Click to Flip", font=("Arial", 24), width=10, height=4,
            command=self.flip_card
        )
        self.card.pack(expand=True)

        # Next Button
        self.next_button = tk.Button(
            root, text="Next", font=("Arial", 14), command=self.show_new_card
        )
        self.next_button.pack()

        self.show_new_card()
    
    def show_new_card(self):
        self.current_consonant = random.choice(list(thai_consonants.keys()))
        self.card.config(text=self.current_consonant)
        self.is_flipped = False
    
    def flip_card(self):
        if self.current_consonant:
            if not self.is_flipped:
                self.card.config(text=thai_consonants[self.current_consonant])
            else:
                self.card.config(text=self.current_consonant)
            self.is_flipped = not self.is_flipped

# Run the app
root = tk.Tk()
app = FlashcardApp(root)
root.mainloop()
