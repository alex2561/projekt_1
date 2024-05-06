'''
projekt_1.py: prvni projekt do Engeto Online Python Akademie

author: Alexandr Sytko
email: sytko.alex@gmail.com
discord: alex_89608
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

# Registrovani uzivatele
registered_users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# Ziskani prihlasovacich udaju od uzivatele
username = input("username:")
password = input("password:")

# Overeni, zda je uzivatel registrovany
if username in registered_users and registered_users[username] == password:
    print("----------------------------------------")
    print(f"Welcome to the app, {username}")
    print("We have 3 texts to be analyzed.")
    print("----------------------------------------")

    # Ziskani cisla textu od uzivatele
    selected_text = input("Enter a number btw. 1 and 3 to select: ")

    # Overeni, zda je zadany vstup platnym cislem mezi 1 a 3
    if selected_text.isnumeric():
        selected_text = int(selected_text)
        if selected_text in range(1, 4):
            selected_text -= 1  
            text = TEXTS[selected_text]

            # Analyza textu
            words = text.split()
            word_count = len(words)
            titlecase_count = sum(1 for word in words if word.istitle())
            uppercase_count = sum(1 for word in words if word.isupper())
            lowercase_count = sum(1 for word in words if word.islower())
            numeric_count = sum(1 for word in words if word.isnumeric())
            numeric_sum = sum(int(word) for word in words if word.isnumeric())

            # Vypis vysledku analyzy
            print("----------------------------------------")
            print(f"There are {word_count} words in the selected text.")
            print(f"There are {titlecase_count} titlecase words.")
            print(f"There are {uppercase_count} uppercase words.")
            print(f"There are {lowercase_count} lowercase words.")
            print(f"There are {numeric_count} numeric strings.")
            print(f"The sum of all the numbers {numeric_sum}")
            print("----------------------------------------")

            # Vytvoreni histogramu delky slov
            word_lengths = [len(word.strip(".,!?")) for word in words]
            word_length_counts = {length: word_lengths.count(length) for length in set(word_lengths)}

            print("LEN|  OCCURENCES  |NR.")
            print("----------------------------------------")
            for length, count in sorted(word_length_counts.items()):
                print(f"{length:2}| {'*' * count:13}| {count}")
            print("----------------------------------------")
        else:
            print("Invalid input. Please enter a number between 1 and 3.")
    else:
        print("Invalid input. Please enter a number.")
else:
    print("unregistered user, terminating the program..")
