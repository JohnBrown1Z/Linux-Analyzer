class Restaraunt():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    def describe_restaraunt(self):
        return(f"{self.name} {self.cuisine}")
    def open_restaraunt(self):
        return(f"{self.name} is open!")
Restar = Restaraunt('Luchia', 10)
print(f"{Restar.name}")
print(f"{Restar.cuisine}")
print(f"{Restar.describe_restaraunt()}")
print(f"{Restar.open_restaraunt()}")

