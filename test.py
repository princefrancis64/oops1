class Person :

    def __init__(self,name,surname,emailid, year_of_birth):
        self.name=name
        self.surname=surname
        self.emailid=emailid
        self.year_of_birth= year_of_birth

prince_var = Person("prince","francis","prince.francis64@gmail.com",1996)
ashi = Person("ashish","shaji","asfsajfds@gmail.com", 1995)
barca  = Person("barca", "cryuff" , "barca@gmail.com", 1988 )
print(prince_var.name)
print(ashi.name)
print(barca.name)
print(prince_var.year_of_birth)
print(type(barca))