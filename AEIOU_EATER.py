user_word_eaten = ""
user_word = input("Enter your Word:\n")
user_word = user_word.upper()
# Prompt the user to enter a word
# and assign it to the user_word variable.

for letter in user_word:
        if letter in "AEIOU":
            continue
        else:
            user_word_eaten += letter
print(user_word_eaten)