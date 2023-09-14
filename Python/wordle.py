import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

# Global dictionaries and list to store color information
green_dict = {}
orange_dict = {}
gray_list = []
guess = ['candy', 'plume', 'riots']
ring=0

class ColorChangerApp:
    def __init__(self, root, guesses):
        self.root = root
        self.guesses = guesses
        self.current_guess_index = 0  # Start before the first guess
        self.initialize_interface()
        
    def initialize_interface(self):
        self.color_mapping = {
            "Orange": "#FFA500",
            "Gray": "#808080",
            "Green": "#008000"
        }

        self.color_frames = []
        self.text_items = []
        self.color_vars = []

        blocks_frame = tk.Frame(self.root)
        blocks_frame.pack(pady=10)

        word = self.guesses[self.current_guess_index].upper()
        letters = list(word)
        for i, letter in enumerate(letters):
            color_var = tk.StringVar()
            color_var.set("Select a color")
            self.color_vars.append(color_var)

            color_frame = tk.Canvas(blocks_frame, width=40, height=40, bg="white")
            color_frame.grid(row=0, column=i, padx=10)
            self.color_frames.append(color_frame)

            text_item = color_frame.create_text(20, 20, text=letter, fill="black", font=("Helvetica", 12))
            self.text_items.append(text_item)

            color_dropdown = ttk.Combobox(blocks_frame, textvariable=color_var, values=list(self.color_mapping.keys()))
            color_dropdown.bind("<<ComboboxSelected>>", lambda event, i=i: self.change_color(event, i))
            color_dropdown.grid(row=1, column=i, padx=10)

        self.submit_button = tk.Button(self.root, text="Submit", state=tk.DISABLED, command=self.submit_sequence)
        self.submit_button.pack(pady=10)

        self.current_word_label = tk.Label(self.root, text="Current Word: " + word)
        self.current_word_label.pack()


    def change_color(self, event, index):
        selected_color = self.color_vars[index].get()
        if selected_color != "Select a color":
            color_code = self.color_mapping[selected_color]
            self.color_frames[index].config(bg=color_code)
            self.color_frames[index].itemconfig(self.text_items[index], fill=self.get_text_color(color_code))
            self.check_submit_button()

    def get_text_color(self, bg_color):
        r, g, b = int(bg_color[1:3], 16), int(bg_color[3:5], 16), int(bg_color[5:7], 16)
        brightness = (r * 299 + g * 587 + b * 114) / 1000
        if brightness < 128:
            return "#FFFFFF"
        else:
            return "#000000"

    def check_submit_button(self):
        if any(color_var.get() != "Select a color" for color_var in self.color_vars):
            self.submit_button.config(state=tk.NORMAL)
    
    def submit_sequence(self):
        color_sequence = [color_var.get() for color_var in self.color_vars]
    
        if all(color == "Green" for color in color_sequence):
            messagebox.showinfo("Guessed Word", "Guessed word!")
            ring=1
            self.root.quit() 
        else:
            self.update_color_info(color_sequence)
            self.next_word() 
    
    def update_color_info(self, color_sequence):
        word = self.guesses[self.current_guess_index].upper()
        for i, color in enumerate(color_sequence):
            letter = word[i]
            if color == "Green":
                green_dict[letter] = i
            elif color == "Orange":
                orange_dict[letter] = i
            elif color == "Gray":
                gray_list.append(letter)
                 
    def next_word(self):
        self.current_guess_index += 1
        if self.current_guess_index <= len(self.guesses):
            if self.current_guess_index == len(self.guesses): 
                guess_word = GSD(self)  
                self.current_word_label.config(text="Current Word: " + guess_word)
            else:
                guess_word = self.guesses[self.current_guess_index].upper()
                self.current_word_label.config(text="Current Word: " + guess_word)

            letters = list(guess_word)
            for i, letter in enumerate(letters):
                self.color_vars[i].set("Select a color")
                self.color_frames[i].config(bg="white")
                self.color_frames[i].itemconfig(self.text_items[i], text=letter, fill="black")

            self.submit_button.config(state=tk.DISABLED)


file = open('Text files/words.txt','r')
word_list = file.read().splitlines()

def GSD(self):
    global word_list
    matching_words = []
    for word in word_list:
        word = word.upper()

        if all(word[j] == letter for letter, j in green_dict.items()):
            if all(letter not in gray_list for letter in word):
                orange_conditions_met = True
                cnt = len(orange_dict)
                ind = 0

                for alph in orange_dict:
                    if alph in word:
                        ind += 1

                if ind == cnt:
                    for letter, positions in orange_dict.items():
                        if word[positions] == letter:  # Directly compare positions
                            orange_conditions_met = False
                            break

                    if orange_conditions_met:
                        matching_words.append(word)

    if matching_words:
        guess_word = random.choice(matching_words)
        guess.append(guess_word)
        return guess_word
    else:
        return "NO_MATCHING_WORD_FOUND"
    


def main():
    global green_dict, orange_dict, gray_list
    global guess
    root = tk.Tk()
    if ring==0:
        app = ColorChangerApp(root, guess)
        root.mainloop()
    else:
        root.destroy()

if __name__ == "__main__":
    main()

file.close()
