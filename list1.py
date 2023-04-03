import logging
logging.basicConfig(filename="list1.log",level=logging.DEBUG,format="%(levelname)s %(name)s %(asctime)s %(message)s")


class list1():


    def __init__(self,s):
        self.s=s

    def reverse1(self):
        try:
           return self.s[::-1]
        except Exception as e:
            logging.error(e)
            logging.info("please enter the subscriptables")

    def list2(self):
        l1=[]
        for i in self.s:
            if type(i)==list:
                l1.append(i)
        return l1

    def sudh(self):
        l1=[]
        for i in self.s:
            if type(i)==dict:
                for j in i.values():
                    if j=="sudh":
                        l1.append(j)
        return l1

    def value(self):
        l1=[]
        for i in self.s:
            if type(i)==dict:
                for j in i.values():
                        l1.append(j)
        return l1


    def keys(self):
        l1=[]
        for i in self.s:
            if type(i)==dict:
                for j in i:
                        l1.append(j)
        return l1

var = list1(12131)

print(var.reverse1())

print(var.list2())

print(var.sudh())

print(var.value())

print(var.keys())