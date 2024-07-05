class Car:

    wheels = 4 #class variable - default

    def __init__(self,make,model,year,color):
        self.make = make        #instance variable - in constructor
        self.model = model      #instance variable
        self.year = year        #instance variable
        self.color = color      #instance variable
