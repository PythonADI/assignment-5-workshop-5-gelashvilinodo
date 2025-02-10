name = "Nodo"
print("Is name == 'Nodo'? I predict True.")
print(name == 'Nodo')
print("\nIs name == 'nodo'? I predict False.")
print(name == 'nodo')

name1 = "Anano"
print("\nIs name1 == 'Anano'? I predict True.")
print(name1 == 'Anano')
print("\nIs name1 == 'anano'? I predict False.")
print(name1 == 'anano')

name2 = "Nia"
print("\nIs name2 == 'Nia'? I predict True.")
print(name2 == 'Nia')
print("\nIs name2 == 'nia'? I predict False.")
print(name2 == 'nia')

name3 = "Irakli"
print("\nIs name3 == 'Irakli'? I predict True.")
print(name3 == 'Irakli')
print("\nIs name3 == 'irakli'? I predict False.")
print(name3 == 'irakli')

name4 = "Nika"
print("\nIs name4 == 'Nika'? I predict True.")
print(name4 == 'Nika')
print("\nIs name4 == 'nika'? I predict False.")
print(name4 == 'nika')


name = "Nodo"
print(name != "nodo")
print(name == "Nodo")

print(name.lower() == "nodo")
print(name.lower() != "Nodo")

num1 = 5
num2 = 10
num3 = 15
print(num1 == num2)
print(num1 != num2)
print(num1 < num2)
print(num1 > num2)
print(num1 <= num2)
print(num1 >= num2)
print(num1 and num2 < num3)
print(num1 or num2 < num3)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_number = 12
if my_number in numbers:
    print(f"{my_number} is in the list.")
else:
    print(f"{my_number} is not in the list.")
    

alien_color = "green"
if alien_color == "green":
    print("You just earned 5 points!")
    
if alien_color == "green":
    print("you just earned 5 points for shooting Alien.")
if alien_color != "green":
    print("you earned 10 poits.")
    
if alien_color == "green":
    print("you just earned 5 points for shooting Alien.")
else:
    print("you just earned 5 points for shooting Alien.")
    
    
if alien_color == "green":
    print("You just earned 5 points!")
elif alien_color == "yellow":
    print("You earned 10 points!")
else:
    print("You earned 15 points")
    

alien_color = "yellow"
    

if alien_color == "green":
    print("You just earned 5 points!")
elif alien_color == "yellow":
    print("You just earned 10 points!")
else:
    print("You just earned 15 points")
    

alien_color = "red"


if alien_color == "green":
    print("You just earned 5 points!")
elif alien_color == "yellow":
    print("You just earned 10 points!")
else:
    print("You just earned 15 points")
    


# task 6
age = int(input("Enter your age: "))

if age < 0:
    print("Please, enter non-negative number")
elif age < 2:
    print("Person is a baby")
elif 4 > age >= 2:
    print("Person is a toddler")
elif 13 > age >= 4:
    print("Person is a kid")
elif 20 > age >= 13:
    print("Person is a teenager")
elif 65 > age >= 20:
    print("Person is an adult")
elif age >= 65:
    print("Person is an elder")
    
    
favorite_fruits = ["watermelon", "mango", "alucha"]

if "watermelon" in favorite_fruits:
    print("I really love watermelon")

if "mango" in favorite_fruits:
    print("I really love mango")
    
if "alucha" in favorite_fruits:
    print("I really love alucha")
    
if "watermelon" and "alucha" in favorite_fruits:
    print("that's the best combo")
    
if "watermelon" "mango" and "alucha" in favorite_fruits:
    print("that's too much")
    
    

usernames = ["admin", "Nodo", "Nika", "Irakli", "Nuka"]

for name in usernames:
    if name == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {name}, thank you for logging in again.")
    
if len(usernames) == 0:
    print("We need to find some users!")
    
current_users = ["admin", "Nodo", "Nika", "Irakli", "Nuka"]
new_users = ["Nodo", "Nika", "Anano", "Nana", "Nia"]
for user in new_users:
    if user in current_users:
        print(f"Sorry {user}, you need to enter a new username")
    if user not in current_users:
        print(f"Hello {user}, your username is available")
    
        
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")