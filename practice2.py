class Person:
    def __init__(self,name,surname,emailid,year_of_birth):
        self.name=name
        self.surname=surname
        self.emailid=emailid
        self.year_of_birth=year_of_birth


prince_var=Person("prince","francis","prince.francis64",1996)
barca= Person("barcelona","camp nou","spotify12",1899)
real=Person("real","madrid","real13",1902)

print(prince_var.name)
print(barca.year_of_birth)
print(real.year_of_birth)
print(barca.name + barca.surname)


class Person:
    def __init__(self,name,surname,emailid,year_of_birth):
        self.name=name
        self.surname=surname
        self.emailid=emailid
        self.year_of_birth=year_of_birth

    def __init__(self,name,surname,emailid,year_of_birth):
        self.name=name
        self.surname=surname

    def age(self,current_year):
        return current_year-self.year_of_birth

barca= Person("barcelona","camp nou","spotify12",1899)
print(barca.name)



class Person():
    def name(self):
        name=input("enter the name")
        return name

    def surname(self):
        surname=input("enter the surname")
        return surname

    def age(self,current_year,year_of_birth):
        return current_year-year_of_birth

    def emailid(self):
        emailid=input("enter email id")
        return emailid

barca = Person()
real=Person()
Manu=Person()

print(barca.name())
print(barca.age(2023,1899))
