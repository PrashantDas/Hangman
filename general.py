import words700, images
import re

question_word = words700.pick_one().upper()
# print(question_word)
display_book = {digit: '_' for digit, letter in zip(range(len(question_word)), question_word)}  #dictionary


def show_current_word()->None:
    print("Current word: ", end='')
    for each in display_book.values():
        print(each, end=' ')
    print()


word_length = len(set(question_word))
correct_attempts = 0
wrong_attempts = 0
wrong_letters_used = ''


print("""The hangman is about to hang this word,
save the word by guessing letter-by-letter""")
show_current_word()


while (wrong_attempts < 10) and (correct_attempts < word_length):
    if len(wrong_letters_used) > 0:
        print("Wrong letters used: ", wrong_letters_used)
    user_input = input("\nYour guess: ").upper()
    if (len(user_input) != 1) or (not user_input.isalpha()):
        print("Please enter only a single letter between A & Z")
        continue
    if user_input in question_word:
        correct_attempts += 1
        for each in re.finditer(user_input, question_word):
            index = each.span()[0]
            display_book[index] = user_input
        print("Ah! such relief. ", end='')
        show_current_word()
        if correct_attempts == word_length:
            print('You did well!')
    else:
        wrong_attempts += 1
        images.show_man(wrong_attempts)
        if wrong_attempts < 10:
            print("Ow!, I'm dying. ", end='')
            show_current_word()
            wrong_letters_used += user_input+' '
            print("Attempts left: ", 10 - wrong_attempts)
        if wrong_attempts == 10:
            print("The word was: ", question_word)

