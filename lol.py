def hello():
    print("Hello, Python!")

hello()

# Unused variable (flake8 will flag this)
unused_var = 100

# Indentation error (flake8 will flag this)
if True:
print("Indentation issue detected!")  

# Insecure use of eval (bandit will flag this)
user_input = input("Enter something: ")
eval(user_input)
