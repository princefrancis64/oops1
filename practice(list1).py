class Person:
    def __init__(self,name,surname,emailid,year_of_birth):
        self.name=name
        self.surname=surname
        self.emailid=emailid
        self.year_of_birth=year_of_birth


prince_var = Person("Prince","Francis","prince.francis64@gmail.com",1996)
print(prince_var.name)
print(prince_var.surname)
print(prince_var.year_of_birth)


class Person:
    def __init__(self,name,surname,emailid,year_of_birth):
        self.name=name
        self.surname=surname
        self.emailid=emailid
        self.year_of_birth=year_of_birth

    def age(self,current_year):
        return current_year-self.year_of_birth


prince_var = Person("Prince","Francis","prince.francis64@gmail.com",1996)
print(prince_var.age(2023))


class Person:

    def name(self):
        name=input("enter name")
        return name

    def surname(self):
        surname=input("enter surname")
        return surname

    def email_id(self,v):
        return v

    def age(self,current_year,year_of_birth):
        return current_year-year_of_birth


prince= Person()

print(prince.email_id("prince.francis64@gmail.com"))
print(prince.age(2023,1996))
print(prince.name())
print(prince.surname())

