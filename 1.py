import logging
logging.basicConfig(filename="1.log",level=logging.DEBUG,format="%(levelname)s %(name)s %(asctime)s %(message)s")


def index1():
    try:
        v=int(input("enter an integer"))
    except Exception as e:
         logging.error(e)
         logging.info("please enter a string")


index1()
