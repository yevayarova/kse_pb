import random
#Буду додавати пропуски між рядками для читабельності
def choose_secret_word(words):
    return random.choice(words)
#Там були зміні xyz, на мою думку абсолютно зайві 
#Можна просто random вибір слова і просто довжина слова
#І тут я вирішила спочатку задати всі функції - щоб їх просто викликати за потребою
def get_guess(expected_length):
    while True:
        guess = input(f"Enter your guess ({expected_length} letters): ").lower()
        if len(guess) == expected_length:
            return guess
        print(f"Invalid input. Expected a word with {expected_length} letters.")
#

def evaluate_guess(secret_word, guess):
    result = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            result.append('correct')
        elif guess[i] in secret_word:
            result.append('present')
        else:
            result.append('absent')
    return result

def format_feedback(guess, evaluation):
    display = []
    for letter, status in zip(guess, evaluation):
        if status == 'correct':
            display.append(f"[{letter.upper()}]")
        elif status == 'present':
            display.append(f"({letter})")
        else:
            display.append(f" {letter} ")
    return ' '.join(display)

#В оригінальному коді там привітання не в функції і воно не зациклене 
#воно просто зверху є. Не ефективно. 
#До того ж гра закінчується після 1 ініціювання 
# Я вирішила додати можливість продовжити гру через питання.
def play_round(words, tries=6):
    secret_word = choose_secret_word(words)
    word_length = len(secret_word)

    print(f"\nNew Round! Guess the {word_length}-letter word. You have {tries} tries.")

    attempt = 1
    while tries > 0:
        print(f"\nAttempt {attempt}/{6}")
        guess = get_guess(word_length)
        
        if guess == secret_word:
            print("You win!!!")
            return True

        evaluation = evaluate_guess(secret_word, guess)
        feedback = format_feedback(guess, evaluation)
        print("Result:", feedback)

        tries -= 1
        attempt += 1

    print(f"You lose! The word was: {secret_word}")
    return False

def game_loop():
    words = ['apple', 'bread', 'candy', 'dream', 'eagle', 'flame', 'grape', 'house', 'input', 'joker']
    print("Welcome to Wordle!")

    while True:
        play_round(words)
        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing Wordle!")
            break

game_loop()
