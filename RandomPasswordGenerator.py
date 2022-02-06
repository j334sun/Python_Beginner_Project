import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print("\n\n\n\nWelcome to the PyPassword Generator!")

letters_count = int(input("How many letters would you like in your password?\n")) 

symbols_count = int(input("How many symbols would you like?\n"))

numbers_count = int(input("How many numbers would you like?\n"))

password = ""

for l in range(1,letters_count+1):
    l = letters[random.randint(0,len(letters)-1)]
    password += l

for s in range(1,symbols_count+1):
    s = symbols[random.randint(0,len(symbols)-1)]
    password += s

for n in range(1,numbers_count+1):
    password += random.choice(numbers)
    

ran_pass = list(password)
random.shuffle(ran_pass)

passy = (''.join(ran_pass))

print("Your password is {}.\n\n\n".format(passy))


