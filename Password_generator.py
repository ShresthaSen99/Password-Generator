import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print ("Welcome to Password generator")

letq = int(input("how many letters you want in your password?\n"))
numq = int(input("how many numbers you want in your password?\n"))
symq = int(input("how many symbol you want in your password?\n"))

password = []
for l in range (1, letq+1) :
    let = random.choice (letters)
    password.append(let)

# print (password)

for n in range (1, numq+1) :
    num = random.choice (numbers)
    password.append (num)

# print (password)

for s in range (1, symq+1) :
    sym = random.choice (symbols)
    password.append (sym)

# print (password)
random.shuffle (password)
# print (password)

password_rs = ""
for result in password :
    password_rs += result
print (f"Your password could be : {password_rs}")

