import random
import secrets



letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


if 1 <= nr_letters <= 9:
    letters_extra = ("".join(random.choices(letters, k=nr_letters)))
if 1 <= nr_symbols <= 9:
    symbols_extra = ("".join(random.choices(symbols, k=nr_symbols)))
if 1 <= nr_numbers <= 9:
    numbers_extra = ("".join(random.choices(numbers, k=nr_numbers)))

mypassword = list(letters_extra + symbols_extra + numbers_extra)

random.shuffle(mypassword)
print("".join(mypassword))