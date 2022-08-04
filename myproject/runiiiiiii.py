"""def kxn_company(silpa):
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


# red=["hello",(5,9),[9,7],{75:(9,45)}]
# seetha=[item for item in(red) if type(item)==list]
# print(seetha)
#
mydict={'x':100,'y':200,'z':300,'a':{'b':{'c':1000}}}
print("The type of mydict is",type(mydict))
print("The value of x in mydict is",mydict['x'])
print("The value of y in mydict is",mydict['y'])
print("The value of z in mydict is",mydict['z'])
print("The value of a in mydict is",mydict['a'])
print("The value of a in mydict is",mydict['a']['b'])
print("The value of a in mydict is",mydict['a']['b']['c'])
print()
#List comprehentions
#without
"""mylist= range(50)
for item in mylist:
     if item %2==0:
         print("Even number is",item)
     else:
        print("Odd number is",item)
print()

#with
mylist=[item for item in range(20) if item %2==0]
print("The type of mylist is",type(mylist))
print("The Even number is",mylist)
print()

import time
start_time=time.time()
list=[item for item in range(50) if item %3==0]
print("The type of list is",type(list))
print("The mylist is",list)
end_time=time.time()
print("Time executes from start to end",(end_time-start_time))
print()


mywords=["Hiee","Hello","World","Earth","oceans"]
print("The type of mylist is",type(mywords))
mylist=[item for item in mywords if "l" in item]
print("My words are",mylist)
print("The type of mylist is",type(mylist))
print()


mylist=[(1,2),"India",(3,4),"Australia",(5,6),"Germany"]
newlist=[item for item in (mylist) if type(item)==str]
print(newlist)
print()

import time
start_time=time.time()
list=[item for item in range (30) if item %2==0]
print("The type of item is",type(list))
print("Even number is",list)
end_time=time.time()
print("Time execution",(end_time-start_time))
print()


mylist=range(10)
newlist=[item for item in mylist if item>5]
print("The newlist is",newlist)
print()

import time
start_time=time.time()
mylist=["Rose","Lilly","Lotus","Jasmine"]
mylist1=[item if item !="Lilly" else "Sunflower" for item in mylist]
print("The mylist1 is",mylist1)
end_time=time.time()
print("Time execution",(end_time-start_time))
print()

mylist=[500,600,700,800,1000,200]
mylist1=[mounika if mounika ==200 else 2000 for mounika in mylist]
print("The type of mylist is",type(mylist))
print("The mylist1 is",mylist1)
print()


mylist=range(30)
mydict= {item:True if item %2==0 else False for item in mylist}
print(mydict)
print()


mylist=[(1,2),"India",(3,4),"Australia",(5,6),"Germany"]
mydict={item:True if type(item)==str else False for item in mylist}
print(mydict)"""


#Dict comprehensions
"""mydict={1:{2:{3:{4:{5:{6:600}}}}}}
print("My dict of 1 is",mydict[1])
print("My dict of 2 is",mydict[1][2])
print("My dict of 3 is",mydict[1][2][3])
print("My dict of 4 is",mydict[1][2][3][4])
print("My dict of 5 is",mydict[1][2][3][4][5])
print("My dict of 5 is",mydict[1][2][3][4][5][6])
print()


mydict={'a':{'b':{'c':{'d':{'e':'Elephant'}}}}}
print("My dict of a is",mydict['a'])
print("My dict of b is",mydict['a']['b'])
print("My dict of c is",mydict['a']['b']['c'])
print("My dict of d is",mydict['a']['b']['c']['d'])
print("My dict of e is",mydict['a']['b']['c']['d']['e'])
print()


mydict={"Brand":"BMW","Model":"Mustang","Year":{"Date":30}}
print("The type of mydict is",type(mydict))
print("The Brand in mydict is", mydict["Brand"])
print("The Brand in mydict is", mydict["Year"])
print()


mydict={"Hero":"Advi shesh","Heroine":"Deepika","Movie":{"Movie2":{"Movie3":"Major"}}}
print("The type of mydict is",type(mydict))
print("The Hero in mydict is", mydict["Hero"])
print("The Heroine in mydict is", mydict["Heroine"])
print("The Movie in mydict is", mydict["Movie"])
print("The Movie2 in mydict is", mydict["Movie"]["Movie2"])
print("The Movie3 in mydict is", mydict["Movie"]["Movie2"]["Movie3"])
print()


#List comprehentions
#without
"""mylist= range(50)
for item in mylist:
     if item %2==0:
         print("Even number is",item)
     else:
        print("Odd number is",item)
print()

#with
mylist=[item for item in range(20) if item %2==0]
print("The type of mylist is",type(mylist))
print("The Even number is",mylist)
print()

import time
start_time=time.time()
list=[item for item in range(50) if item %3==0]
print("The type of list is",type(list))
print("The mylist is",list)
end_time=time.time()
print("Time executes from start to end",(end_time-start_time))
print()


mywords=["Hiee","Hello","World","Earth","oceans"]
print("The type of mylist is",type(mywords))
mylist=[item for item in mywords if "l" in item]
print("My words are",mylist)
print("The type of mylist is",type(mylist))
print()


mylist=[(1,2),"India",(3,4),"Australia",(5,6),"Germany"]
newlist=[item for item in (mylist) if type(item)==str]
print(newlist)
print()

import time
start_time=time.time()
list=[item for item in range (30) if item %2==0]
print("The type of item is",type(list))
print("Even number is",list)
end_time=time.time()
print("Time execution",(end_time-start_time))
print()


mylist=range(10)
newlist=[item for item in mylist if item>5]
print("The newlist is",newlist)
print()

import time
start_time=time.time()
mylist=["Rose","Lilly","Lotus","Jasmine"]
mylist1=[item if item !="Lilly" else "Sunflower" for item in mylist]
print("The mylist1 is",mylist1)
end_time=time.time()
print("Time execution",(end_time-start_time))
print()

mylist=[500,600,700,800,1000,200]
mylist1=[mounika if mounika ==200 else 2000 for mounika in mylist]
print("The type of mylist is",type(mylist))
print("The mylist1 is",mylist1)
print()


mylist=range(30)
mydict= {item:True if item %2==0 else False for item in mylist}
print(mydict)
print()


mylist=[(1,2),"India",(3,4),"Australia",(5,6),"Germany"]
mydict={item:True if type(item)==str else False for item in mylist}
print(mydict)"""


#Dict comprehensions
"""mydict={1:{2:{3:{4:{5:{6:600}}}}}}
print("My dict of 1 is",mydict[1])
print("My dict of 2 is",mydict[1][2])
print("My dict of 3 is",mydict[1][2][3])
print("My dict of 4 is",mydict[1][2][3][4])
print("My dict of 5 is",mydict[1][2][3][4][5])
print("My dict of 5 is",mydict[1][2][3][4][5][6])
print()


mydict={'a':{'b':{'c':{'d':{'e':'Elephant'}}}}}
print("My dict of a is",mydict['a'])
print("My dict of b is",mydict['a']['b'])
print("My dict of c is",mydict['a']['b']['c'])
print("My dict of d is",mydict['a']['b']['c']['d'])
print("My dict of e is",mydict['a']['b']['c']['d']['e'])
print()


mydict={"Brand":"BMW","Model":"Mustang","Year":{"Date":30}}
print("The type of mydict is",type(mydict))
print("The Brand in mydict is", mydict["Brand"])
print("The Brand in mydict is", mydict["Year"])
print()


mydict={"Hero":"Advi shesh","Heroine":"Deepika","Movie":{"Movie2":{"Movie3":"Major"}}}
print("The type of mydict is",type(mydict))
print("The Hero in mydict is", mydict["Hero"])
print("The Heroine in mydict is", mydict["Heroine"])
print("The Movie in mydict is", mydict["Movie"])
print("The Movie2 in mydict is", mydict["Movie"]["Movie2"])
print("The Movie3 in mydict is", mydict["Movie"]["Movie2"]["Movie3"])
print()


mydict={'x':100,'y':200,'z':300,'a':{'b':{'c':1000}}}
print("The type of mydict is",type(mydict))
print("The value of x in mydict is",mydict['x'])
print("The value of y in mydict is",mydict['y'])
print("The value of z in mydict is",mydict['z'])
print("The value of a in mydict is",mydict['a'])
print("The value of a in mydict is",mydict['a']['b'])
print("The value of a in mydict is",mydict['a']['b']['c'])
print()"""






