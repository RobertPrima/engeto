'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Robert Prima
email: primarobert@gmail.com
discord: robert.prima
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
cara = ("*" * 40)
users = {
    "bob": "123", 
    "ann": "pass123",
    "mike": "password", 
    "liz": "pass123"
    }
user = input("Enter your username:\n")
print(cara)
password = str(input("Enter your password:\n"))
print(cara)

if user in users.keys() and password in users.values():
    print(f"Hello {user.upper()} you can analyze texts.")
else:
    print(f"Unregistered user, terminating the program..")
    quit()
print(cara)
print(f"We have {len(TEXTS)} texts to be analyzed")
print(cara)

while True:
    choice = input(f"Enter a number btw. 1 and {len(TEXTS)} to select:\n")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(TEXTS):
            selected_text = TEXTS[choice - 1]
            print("you have selected this text:", cara, selected_text, sep="\n")
            break
        else:
            print(f"Invalid choice, you can only enter a number 1 to {len(TEXTS)}, try again")
    else:
        print(f"Invalid choice, you can only enter a number 1 to {len(TEXTS)}, try again")



clear_text = []
sum_words = 0
sum_upper_word = 0
sum_upper_all = 0
sum_lower_word = 0
digits = 0
sum_digit = 0



#  cisteni
for word in selected_text.split():
    clear_word = word.strip(".,?:;!")
    clear_text.append(clear_word)

# pocet slov
sum_words = len(clear_text)

for word in clear_text:
    if word[0].isupper():
        sum_upper_word += 1
    elif word.isupper(): 
        sum_upper_all += 1
    elif word.islower():
        sum_lower_word += 1
    elif word.isdigit():
        digits += 1
        if word.isdigit():
            sum_digit += int(word)

print(cara)
print(f"There are {sum_words} words in the selected text.")
print(f"There are {sum_upper_word} titlecase words.")
print(f"There are {sum_upper_all} uppercase words.")
print(f"There are {sum_lower_word} lowercase words.")
print(f"There are {digits} numeric strings.")
print(f"The sum of all the numbers {sum_digit} . ")
print(cara)


word_length = {}

for word in clear_text:
    length = len(word)
    if length in word_length:
        word_length[length] += 1
    else:
        word_length[length] = 1

print("Frequency of word lengths in the text:")
print(cara)

for length, frequency in sorted(word_length.items()):
        print(f"• {length} | {'*' * frequency} {frequency}")
print(cara)











        








                                   












 