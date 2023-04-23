import random
import urllib.request
import tkinter as tk

# Download the dictionary
urllib.request.urlretrieve("https://raw.githubusercontent.com/dwyl/english-words/master/words.txt", "words.txt")
with open('words.txt') as f:
    words = f.readlines()
words = [word.strip().lower() for word in words]

# Initialize the window
window = tk.Tk()
window.title('Hangman')

# Initialize the game variables
word = ''
display_word = []
guessed_words = []
hearts = 3
game_over = False

# Define the functions
def reset_game():
    global word, display_word, guessed_words, hearts, game_over
    word = random.choice(words)
    display_word = ['_' for _ in range(len(word))]
    guessed_words = []
    hearts = 3
    game_over = False
    word_label.config(text=' '.join(display_word))
    hearts_label.config(text='Hearts: ' + str(int(hearts)) + ' ♥')
    status_label.config(text='')

def play_game():
    reset_game()
    # Disable the play button and show the word label
    play_button.config(state='disabled')
    word_label.pack()
    guess_entry.config(state='normal')
    guess_button.config(state='normal')

def guess_letter(guess):
    global hearts, guessed_words, game_over
    
    # Clear the guess entry box
    guess_entry.delete(0, tk.END)

    # Check if the game is over
    if game_over:
        return

    # Check if the guess is empty
    if len(guess) == 0:
        status_label.config(text='Please enter a letter or word.')
        return

    # Check if the guess has already been guessed
    if guess in guessed_words:
        status_label.config(text='You already guessed that letter.')
        return

    # Check if the guess is correct
    elif guess in word:
        # Update the word with the guess
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
        word_label.config(text=' '.join(display_word))
        # Check if the player has won
        if '_' not in display_word:
            status_label.config(text='You win!')
            game_over = True
    # Incorrect guess
    else:
        # Remove a heart
        hearts -= 0.5 if len(guess) == 1 else 1
        hearts_label.config(text='Hearts: ' + str(int(hearts)) + ' ♥')
        # Check if the player has lost
        if hearts == 0:
            status_label.config(text='You lose! The word was ' + word)
            game_over = True
            guess_entry.config(state='disabled')
            guess_button.config(state='disabled')
            play_button.config(state='normal')
    # Add the guess to the list of guessed words
    guessed_words.append(guess)
    
    # Create the widgets
play_button = tk.Button(window, text='Play', font=('Arial', 14), command=play_game)
quit_button = tk.Button(window, text='Quit', font=('Arial', 14), command=window.destroy)
word_label = tk.Label(window, text='', font=('Arial', 24))
guess_entry = tk.Entry(window, font=('Arial', 14))
guess_button = tk.Button(window, text='Guess', font=('Arial', 14))
status_label = tk.Label(window, text='', font=('Arial', 14))
hearts_label = tk.Label(window, text='', font=('Arial', 14))

# Pack the widgets
play_button.pack(pady=10)
guess_entry.pack(pady=10)
guess_button.pack(pady=10)
status_label.pack(pady=10)
hearts_label.pack(pady=10)
quit_button.pack(side='bottom')

def reset_game():
    global word, display_word, guessed_words, hearts, game_over
    
    # Reset game variables
    word = random.choice(words)
    display_word = ['_' for _ in range(len(word))]
    guessed_words = []
    hearts = 3
    game_over = False
    
    # Update labels
    word_label.config(text=' '.join(display_word))
    hearts_label.config(text='Hearts: ' + str(int(hearts)) + ' ♥')
    status_label.config(text='')

def play_game():
    # Disable the play button and show the word label
    play_button.config(state='disabled')
    word_label.pack()
    
    # Reset the game
    reset_game()

def guess_letter(guess):
    global hearts, guessed_words, game_over
    
    # Clear the guess entry box
    guess_entry.delete(0, tk.END)

    # Check if the game is over
    if game_over:
        return

    # Check if the guess is empty
    if len(guess) == 0:
        status_label.config(text='Please enter a letter or word.')
        return

    # Check if the guess has already been guessed
    if guess in guessed_words:
        status_label.config(text='You already guessed that letter.')
        return

    # Check if the guess is correct
    elif guess in word:
        # Update the word with the guess
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
        word_label.config(text=' '.join(display_word))
        # Check if the player has won
        if '_' not in display_word:
            status_label.config(text='You win!')
            game_over = True
    # Incorrect guess
    else:
        # Remove a heart
        hearts -= 0.5 if len(guess) == 1 else 1
        hearts_label.config(text='Hearts: ' + str(int(hearts)) + ' ♥')
        # Check if the player has lost
        if hearts == 0:
            status_label.config(text='You lose! The word was ' + word)
            game_over = True
    # Add the guess to the list of guessed words
    guessed_words.append(guess)

    # Check if the game is over
    if game_over:
        # Enable the play button
        play_button.config(state='normal')

# Bind the guess button to the guess function
guess_button.config(command=lambda: guess_letter(guess_entry.get().lower()))

# Start the window
window.mainloop()