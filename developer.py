class House:
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to (self , new_floor):
         if 1 < new_floor < self.number_of_floors :
             for i in range (1,new_floor + 1):

                 print(i)
             else:
                print("такой этаж отсутствует")

    def __len__ (self):

        return self.number_of_floors

    def __str__(self):

        return f"название: {self.name} , количество этажей: {self.number_of_floors}"

h1 = House("ЖК Юпитер",20)
h2 = House("ЖК Венера",8)

h1.go_to(25)
h1.go_to(4)


print(h1)
print(h2)
print(len(h1))
print(len(h2))
