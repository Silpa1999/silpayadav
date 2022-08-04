"""#constacter
class student:
    def __init__(self,name,age,section,gender):
         self.name=name
         self.age=age
         self.section=section
         self.gender=gender
    def student_name(self):
        print("student_name is {}".format(self.name))
    def student_age(self):
        print("stadent_age is {}".format(self.age))
    def student_section(self):
        print("student_section is {}".format(self.section))
    def student_gender(self):
        print("student_gender is {}".format(self.gender))
stu1=student("vani",34,"B","female")
stu1.student_name()
stu1.student_age()
stu1.student_section()
stu1.student_gender()


class world:
    def __init__(self,place,city):
        self.place=place
        self.city=city
    def world_place(self):
        print("world_place is {}".format(self.place))
    def world_city(self):
        print("world_city is {}".format(self.city))
wo=world("tajmahal","agra")
wo.world_place()
wo.world_city()

class feild:
    def __init__(self,rice,vegtables):
        self.rice=rice
        self.vegtables=vegtables
    def s1(self):
        print("feild_rice is {}".format(self.rice))
    def s2(self):
        print("feild_vegtables is {}".format(self.vegtables))
fe=feild("sonamasura","chilli")
fe.s1()
fe.s2()

class colleage:
    def __init__(self,room1,room2):
        self.room1=room1
        self.room2=room2
    def c1(self):
        print("colleage_room1 is {}".format(self.room1))
    def c2(self):
        print("colleage_room2 is {}".format(self.room2))
co=colleage("delhi","hydrabed")
co.c1()
co.c2()



class  usa:
    def __init__(self,place,temple):
        self.place=place
        self.temple=temple
class chennai(usa):
    def __init__(self,place,temple):
        self.place=place
        self.temple=temple
ch=chennai("tiger","lion")
print(ch.place)
print(ch.temple)
"""

class bus:
    def __init__(self,color,weel):
        self.color=color
        self.weel=weel
class aeroplane:
    def __init__(self,color,weel):
        self.color=color
        self.weel=weel
aer=aeroplane("red","two")
print(aer.color)
print(aer.weel)







