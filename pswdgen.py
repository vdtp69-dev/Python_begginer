import random
def password_generator(a,b):  
    password=''
    if b.lower() == "y":
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
        
    else:
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
      
    if a > 0:
        for i in range(a):
            password+=random.choice(chars)
        return password
            
    else:
        print("Nothing will be generated")

a=int(input("Enter the length of your password: "))
b=input("Include Special Characters? (y/n)")
c=int(input("How many passwords?"))
print("Generated passwords:")
for i in range(c):
    password=password_generator(a,b)
    print(f"\n\n{i+1}.{password}")