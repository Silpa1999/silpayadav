 #decorater
"""import time
start_time=time.time()
time.sleep(3)
a=23
end_time=time.time()
print("program took {} secs to execute for a=23".format(end_time-start_time))
time.sleep(2)
b=10
end_time=time.time()
print("program took {} sec to execute for b=10".format(end_time-start_time))
while time:
    if a<b:
        print("a is {}".format(a))
end_time=time.time()
print("program took {} secs to execute for condition".format(end_time-start_time))
end_time=time.time()
print("program took {} secs to execute".format(end_time-start_time))




import time
start_time=time.time()
time.sleep(3)
a=10
end_time=time.time()
print("this lines takes{} secs for a=10".format(end_time-start_time))
time.sleep(4)
b=4
end_time=time.time()
print("this lines takes{} secs for b=4".format(end_time-start_time))
while True:
    if a>b:
       print("a is {}".format(a))
end_time=time.time()
print("this lines takes{} secs".format(end_time-start_time))
end_time=time.time()
print("this lines takes {} secs".format(end_time-start_time))
"""
""""
def fun_dec(s1):
    print(" s1 name is {}".format(s1.__name__))
    def data():
        s1()
        print("in decorator function")
    return data
@fun_dec
def add():
    a=39
    b=38
    print("sum is",a+b)
add()

def fun_name(d1):
    print("d1 name is {}".format(d1.__name__))
    def fun():
        d1()
        print("farmer is back boon of india")
    return fun
@fun_name
def add():
    a=89
    b=78
    print(a+b)
add()

def fun_name(usa):
    print("usa name is {}".format(usa.__name__))
    def fun():
        usa()
        print("all is well")
        return fun
@fun_name
def add():
    a=2
    b=3
    print(a+b)
add()
"""


# def silpa(america):
#     print("gggggggggggggggggggggggggggggggg")
#     def fun():
#         america()
#         print("keep smaile")
#     return fun()
# @silpa
# def add():
#     a=6
#     b=9
#     print("sum is",a+b)
# add()

def mpdo(offine):
    def wrapper():
        offine()
        print("we are getting good marks in ssc")
    return wrapper
@mpdo
def sum():
    a=3
    b=5
    print(a+b)
sum()

def geetha(run):
    def jjj():
        run()
        print("we both going chennai")
    return jjj
@geetha
def sub():
    a=0
    b=0
    print("a=b")
sub()

def hari_name(student):
    print("a is bigger than b is {}".format.__name__)
    def colleage():
        student()
        print("let me call")
    return colleage
@hari_name
def hhh():
    a=90
    b=9
    print("a+b is",a+b)


def j_name(location):
    print("a is bigger than b is {}".format.__name__)
    def colleage():
        location()
        print("let me call")
    return colleage
@j_name
def hhh():
    a=96
    b=93
    print("a+b is",a+b)
hhh()


def j_name(location):
    print("a is bigger than b is {}".format.__name__)
    def colleage():
        location()
        print("let me call")
    return colleage
@j_name
def hhh():
    a=96
    b=93
    print("a+b is",a+b)
hhh()

def j_name(location):
    print("a is bigger than b is {}".format.__name__)
    def colleage():
        location()
        print("let me call")
    return colleage
@j_name
def hhh():
    a=96
    b=93
    print("a+b is",a+b)
hhh()

"def kxn_company(silpa):
    print("silpa is good{}".format(silpa.__name__))
    def EEE ():
        a=10
        silpa()
        b=23
        print("a+b is",a+b)
    return EEE
@kxn_company
def sss():
    c=2323
    d=5869906
    print("c+b is value",c+d)
sss()
#
#
# def wipro(me):
#     print("me and she")
#     def hhh():
#         a=19
#         b=18
#         print("a+b is",a+b)
#     return hhh
# @wipro
# def fff():
#     v=6543
#     n=987654
#     print("v+n is value",v+n)
# fff()
#
#
# def cisco(keerthi):
#     print("i am going to office")
#     def fff():
#         a=55
#         b=66
#         print("a+b is",a+b)
#     return fff
# @cisco
# def kkk():
#     a=33
#     b=32
#     print(a+b)
# kkk()
# """
# def tcs(janu):
#     print("i start with programming")
#     def hhh():
#         a=66
#         b=88
#         print("a+b is",a+b)
#         return hhh
# @tcs
# def jjj():
#     a=9
#     b=6
#     print(a+b)
# jjj()

