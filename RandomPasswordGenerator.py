import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")

letters_count = int(input("How many letters would you like in your password?\n")) 

symbols_count = int(input(f"How many symbols would you like?\n"))

numbers_count = int(input(f"How many numbers would you like?\n"))

str_l = ""
str_s = ""
str_n = ""

for l in range(1,letters_count+1):
    l = letters[random.randint(0,len(letters)-1)]
    str_l += l

for s in range(1,symbols_count+1):
    s = symbols[random.randint(0,len(symbols)-1)]
    str_s += s

for n in range(1,numbers_count+1):
    n = numbers[random.randint(0,len(numbers)-1)]
    str_n += n
    
password = str_l + str_s + str_n

ran_pass = list(password)
random.shuffle(ran_pass)

passy = (''.join(ran_pass))

print(f"Your password is {passy}.")




