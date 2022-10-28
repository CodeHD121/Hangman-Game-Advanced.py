import string
from find_word import find_word


def main(guesses):
    # User chooses between either German with "1" or English with "2". Also making sure no other options are accepted
    possible_answers = [1,2]
    while True:
        try:
            user_language = int(input("Choose 1 for German or 2 for English> "))
            print("""Enter "exit" to quit the game.""")
            if user_language in possible_answers:
                break
        except:
            print("Invalid.")

    # find_word is called according to the user_language chosen earlier and will return one word(w)
    if user_language == 1:
        w = find_word(1).lower()
    elif user_language == 2:
        w = find_word(2).lower()

    # Each character is placed into a dictionary with it's index as key and the character as the value
    word = {}
    for i, element in enumerate(w):
        word[i] = element

    # According to the number of characters of the word, another dictionary with "-" for each character is created
    hidden_word = {}
    for i, element in enumerate(w):
        hidden_word[i] = "_"

    counter_misses = 0
    while True:
        if word == hidden_word:
            print(f"Word guessed! The word was '{w.capitalize()}'.")
            break
        else:
            print("".join(list(hidden_word.values())))
            user_guess = input('Guess> ')
            # The character is in the word
            if user_guess.lower() in word.values():
                # Going through each value in dict. word until the match from user_guess is found
                for x, y in word.items():
                    if user_guess == y:
                        print("Yes!")
                        # Replacing the blank '_' in hidden_word with the correctly guessed character
                        for d, f in hidden_word.items():
                            hidden_word[x] = user_guess
            # The user can exit the game anytime prior
            elif user_guess.lower() == "exit":
                print(f"Game stopped. The word was '{w.capitalize()}'.")
                break
            # The guess was wrong, one miss is counted
            else:
                print("No!")
                counter_misses += 1
                print(f"You have {guesses + 1 - counter_misses} guess(es) left.")
        if counter_misses > guesses:
            print(f"Game over! The word was '{w.capitalize()}'.")
            break

# This is the main-game-loop, which will keep the game running as long as the user wishes to do so
while True:
    difficulty = input("How many attempts?> ")
    if difficulty not in string.digits:
        print("Invalid.")
        continue

    main(int(difficulty))
    answer = input("Do you want to play again? Enter y or n> ")
    if answer == "n":
        break
