class Person :

    def __init__(prince,name,surname,emailid, year_of_birth):
        prince.name1=name
        prince.surname=surname
        prince.emailid=emailid
        prince.year_of_birth= year_of_birth



    def age(prince,current_year):
        return current_year-prince.year_of_birth

prince_var = Person("prince","francis","prince.francis64@gmail.com",1996)
ashi = Person("ashish","shaji","asfsajfds@gmail.com", 1995)
barca  = Person("barca", "cryuff" , "barca@gmail.com", 1988 )
print(prince_var.age(2022))

