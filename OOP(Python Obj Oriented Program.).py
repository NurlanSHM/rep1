from car import Car

car_1 = Car("Koenigsegg","Jesko",2024,"full carbon")
car_2 = Car("Porsche","911 GT3",2022,"Saturn Black Wrap")

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive()
car_2.stop()
