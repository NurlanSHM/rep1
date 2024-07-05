
try:
    with open('test') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")
