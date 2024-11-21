import tkinter as tk
import random

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game")
        
        # Define the card images
        self.card_images = ["img1.png", "img2.png", "img3.png", "img4.png"]
        self.cards = self.card_images * 2  # Create pairs
        random.shuffle(self.cards)  # Shuffle the cards
        self.buttons = []
        self.card_buttons = {}
        self.matches_found = 0
        self.first_card = None
        self.second_card = None
        self.cover_image = self.resize_image("cover.png")
        self.image_dict = {}

        self.create_board()
        
    def resize_image(self, img_path, width=100, height=100):
        """Resizes the image to fit the button."""
        img = tk.PhotoImage(file=img_path)
        return img.subsample(int(img.width() / width), int(img.height() / height))

    def create_board(self):
        for row in range(2):
            for col in range(4):
                index = row * 4 + col
                button = tk.Button(self.root, image=self.cover_image, command=lambda index=index: self.reveal_card(index))
                button.grid(row=row, column=col)
                self.buttons.append(button)
                self.card_buttons[index] = self.cards[index]
        
    def reveal_card(self, index):
        """Handles the logic when a card is clicked."""
        if self.first_card is None and self.second_card is None:
            self.first_card = index
            self.update_button_image(index)
        elif self.first_card is not None and self.second_card is None:
            self.second_card = index
            self.update_button_image(index)
            self.check_for_match()

    def update_button_image(self, index):
        """Updates the image on a card button."""
        image_path = self.card_buttons[index]
        img = self.resize_image(image_path)
        self.buttons[index].config(image=img)
        self.buttons[index].image = img

    def check_for_match(self):
        """Checks if the two flipped cards match."""
        if self.card_buttons[self.first_card] == self.card_buttons[self.second_card]:
            self.matches_found += 1
            if self.matches_found == 4:  # All matches found
                self.show_message("You found all the matches!")
            else:
                self.show_message("Found a match!")
        else:
            self.show_message("Keep trying")
            self.hide_cards()

    def hide_cards(self):
        """Hides the unmatched cards after a brief delay."""
        self.root.after(1000, self.reset_cards)

    def reset_cards(self):
        """Resets the first and second cards to the cover image."""
        self.update_button_image(self.first_card)  # Reset the first card
        self.update_button_image(self.second_card)  # Reset the second card
        self.first_card = None
        self.second_card = None

    def show_message(self, message):
        """Displays the message on the screen."""
        message_label = tk.Label(self.root, text=message, font=("Arial", 14))
        message_label.grid(row=3, column=0, columnspan=4)

# Set up the Tkinter window
root = tk.Tk()
game = MemoryGame(root)
root.mainloop()
