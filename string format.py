

# str.format() =    optional method that gives users
#                   more control when displaying output

number = 1000
print("The number pi is {:.3f}".format(number))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number))



name = "Bro"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))    # padding
print("Hello, my name is {:<10}. Nice to meet you".format(name))    # padding right
print("Hello, my name is {:>10}. Nice to meet you".format(name))    # padding left
print("Hello, my name is {:^10}. Nice to meet you".format(name))    # padding center


animal = ("cow")
item = "moon"

print("The "+animal+" jumped over the"+item)
print("The {} jumped over the {}".format(animal,item))
print("The {1} jumped over the {1}".format(animal,item)) #positional argument
print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) #keyword argument - longer but cooler

text = "The {} jumped over the {}"
print(text.format(animal,item))