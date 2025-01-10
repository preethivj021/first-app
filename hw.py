
'''correct_username = "user"
correct_password = "password"

max_attempts = 3
attempts = 0

while attempts < max_attempts:
   
    username = input("Enter username: ")
    password = input("Enter password: ")
   
    if username == correct_username and password == correct_password:
        print("Access granted")
        break
    else:
        print("Invalid username or password")
        attempts += 1
        print(f"Attempts left: {max_attempts - attempts}")

if attempts == max_attempts:
    print("Blocked")'''
#----------------------------------------------------------------------------------------------------
'''correct_username = "admin"
correct_password = "password123"
attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == correct_username and password == correct_password:
        print("Access granted")
        break
    else:
        attempts -= 1
        print(f"Invalid credentials. You have {attempts} attempts left.")
        
    if attempts == 0:
        print("Blocked")'''
#----------------------------------------------------------
username='gaana'
password='gaana'
attempts=1

while attempts > 0:
    name=input('enter your name')
    password1=input('enter your password')

    if username==name and password1==password:
        print('succesfull')
        break
    else:
        attempts == 1
        print('valid input ')
        break

   
    

