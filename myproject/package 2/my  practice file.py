#single
"""class bike:
    last_name="four"
class cycle(bike):
    pass
cy=cycle()
print(cy.last_name)

class seeds:
    location="farmer"
class vegtables(seeds):
    pass
ve=vegtables()
print(ve.location)

class tiger:
    last_name="lion"
class cat(tiger):
    pass
c=cat()
print(c.last_name)

class kala:
    last_name="l"
class latha(kala):
    pass
la=latha()
print(la.last_name)
#multiple
class ap:
    first_name="c"
class tn:
    last_name="d"
class andrarashtram(ap,tn):
    pass
ar=andrarashtram()
print(ar.last_name)
print(ar.first_name)

#mulity level
class gp:
    f_name="q"
class p(gp):
    p_name="p"
class child(p):
    pass
ch=child()
print(ch.f_name)

print(ch.p_name)


#hierarchical
class america:
    l_name="p"
class q1:
    pass
class q2:
    pass
class q3:
    pass
class q4:
    n_name="u"
q4=q4
print(q4.l_name)
print(q4.n_name)

#hybird
class  q:
     l_name="kkk"
class w:
     k_name="e"
class r(q,w):
     pass
class jion(r):
     pass
j=r()
j=jion()
print(j.l_name)
print(j.k_name)
"""
#opps
"""class tajmahal:
     taj_name="india"
     def taj_place(self):
          return{"place":"agra","special":"wonder","color":"white"}
india_obj=tajmahal()
print(tajmahal)
print(india_obj)
print(india_obj.taj_name)
print(india_obj.taj_place())


class hydrabed:
     hy_name="ap"
     def hy_place(self):
          return{"place":"ap","location":"jublihils"}
ap_obj=hydrabed()
print(hydrabed)
print(ap_obj)
print(ap_obj.hy_name)
print(ap_obj.hy_place())



class bike:
     bi_name="hero"
     def bi_place(self):
          return{"name":"hero","color":"blue"}
he_obj=bike()
print(bike)
print(he_obj)
print(he_obj.bi_name)
print(he_obj.bi_place())"""
"""
class parent:
     parent_name="suma"
     def parent_details(self):
           return{"name":"suma","age":"54","height":5.11}
suma_obj=parent()
print(parent)
print(suma_obj)
print(suma_obj.parent_name)
print(suma_obj.parent_details())

class mobile:
     m_name="sim"
     def m_details(self):
          return{"name":"redmi","vesion":7,"color":"black"}
sim_obj=mobile()
print(mobile)
print(sim_obj)
print(sim_obj.m_name)
print(sim_obj.m_details())

class animal:
    animal_name="cat"
    def animal_details(self):
        return{"color":"white","weight":2}
cat_obj=animal()
print(animal)
print(cat_obj)
print(cat_obj.animal_name)
print(cat_obj.animal_details())

class lap:
     lap_name="windows"
     def lap_place(self):
          return{"name":"dell","version":10}
w_obj=lap()
print(lap)
print(w_obj)
print(w_obj.lap_name)
print(w_obj.lap_place())


class seeds:
     se_name="vegtables"
     def feild_place(self):
          return{"name":"village","color":"green"}
ve_obj=seeds()
print(seeds)
print(ve_obj)
print(ve_obj.se_name)
print(ve_obj.feild_place())"""
#exception handling
try:
     a=10,
     b=20
     print(a+b)
except:
     print("there is error in this try block")
else:
     "No Error"
finally:
     print("defalut  always runs")

try:
     a=70
     b=12
     print(a,b,c)
     70,20
except:
     print("there is error in this try block")
else:
     "No error"
finally:
     print("defalut always runs")

try:
     a=10
except:
     print("there is error in this block")
else:
     print("No error")
finally:
     print("defalut always runs")

try:
     a=10
     b=20
     (a,b)
     10,20
except:
     print("there is error in this block")
else:
     print("No Error")
finally:
     print("defalut always runs")
#consracter
class farmer:
     def __init__(self,name,place,work):
          self.name=name
          self.place=place
          self.work=work
     def f_name(self):
          print("name is {}".format(self.name))
     def f_place(self):
          print("place is {}".format(self.place))
     def f_work(self):
          print("work is {}".format(self.work))
fa1=farmer("hari","village","feild")
fa1.f_name()
fa1.f_place()
fa1.f_work()

class sports:
     def __init__(self,name,place,players):
          self.name=name
          self.place=place
          self.players=players
     def s_name(self):
          print("name is {}".format(self.name))
     def s_place(self):
          print("place is {}".format(self.place))
     def s_player(self):
          print("player is {}".format(self.players))
sp1=sports("chess","chessbord","two")
sp1.s_name()
sp1.s_place()
sp1.s_player()

class game:
     def __init__(self,name,place,player):
          self.name=name
          self.place=place
          self.player=player
     def g_name(self):
          print("name is {}".format(self.name))
     def g_place(self):
          print("place is {}".format(self.place))
     def g_player(self):
          print("player is {}".format(self.player))

ga1=game("cricket","ground","seven")
ga1.g_name()
ga1.g_place()
ga1.g_player()
#list methods
#append
mylist=[10,20,30]
mylist.append(12)
print(mylist)
#extend
mylist=[10,20,30]
mylist.extend([89,90,99])
print(mylist)
#count
mylist=[10,20,30,40]
a=mylist.count(30)
print(a)
#remove
mylist=[10,20,30,40]
mylist.remove(20)
print(mylist)

# mystring="sunb ricesb inb eastb"
# print(mystring.split(b))
#
#
# mystring=['ind','ia i','s','a', 'eaut','ifulco,untry']
# print(mystring.split('b'))
# mystr="abc"
# mystr="india".jion(mystr)
# print(mystr)

#*arguments
def add(* input):
     print(input)
     return sum(input)
print(add())
print(add(1,2,3))


def add(* just):
     print(just)
     return add(just)
print(add())
print(add(8,8,9))






