class person:

    def age(self,current_year,year_of_birth):
        return current_year-year_of_birth

    def email_id_input(self,email_id):
        print("take and mail id from a person and print it", email_id)

    def ask_name(self):
        name = input("tell me your name")
        return name

    def ask_dob(self):
        dob = input("tell me your dob")
        return dob

prince=person()
anuj=person()
barca=person()

prince.email_id_input("prince.francis64")
print(prince.ask_name())
print(barca.ask_name())