import random
def password_generator(a):  
    password=''
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    if a > 0:
        for i in range(a):
            password+=random.choice(chars)
        return password
        
    else:
        print("Nothing will be generated")
  

a=int(input("Enter the length of your password: "))

password=password_generator(a)

print(f"Your password is: {password}")