import logging
logging.basicConfig(filename="string1.log",level=logging.DEBUG,format="%(levelname)s %(name)s %(asctime)s %(message)s")

class string1():

    def index(self,s):
        try:
            logging.info("we are into this function")
            return s[1:300:3]
        except Exception as e:
            logging.error(e)
            logging.info("function failed")

    def reverse(self,s):
        return(s[::-1])

    def upper1(self,s):
        return s.upper().split()

    def lower1(self,s):
        return s.lower()

    def capitalize(self,s):
        return s.capitalize()

    def replace1(self,s):
        return s.replace("i","o")

    def center1(self,s):
        return s.center(20,"$")

s = string1()

try:
    print(s.index(123423))
except Exception as e:
    logging.error(e)
print(s.reverse( "this is My First Python programming class and i am learNING python string and its function"))
print(s.upper1( "this is My First Python programming class and i am learNING python string and its function"))
print(s.lower1( "this is My First Python programming class and i am learNING python string and its function"))
print(s.capitalize( "this is My First Python programming class and i am learNING python string and its function"))
print(s.replace1("prince"))
print(s.center1("prince"))


