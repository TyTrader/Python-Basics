class Car:
    def __init__(self, make, model, yr, color, power):
        self.make = make
        self.model = model
        self.yr = yr
        self.color = color
        self.power = power

    def showroom(self):
        print(self.make, self.model, self.yr, self.color, self.power)


car1 = Car('Nissan', 'Gtr', '2016', 'Grey', '650hp')
car2 = Car('Porsche', '911', '2019', 'Black', '556hp')
car3 = Car('Chevrolet', 'Z06', '2021', 'Yellow', '602hp')
car4 = Car('Citroen', 'DS9', '2012', 'Blue', '332hp')
car5 = Car('Aston Martin', 'Victor', '2020', 'Forest green', '789hp')
car1.showroom()
car2.showroom()
car3.showroom()
car4.showroom()
car5.showroom()
