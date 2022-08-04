# # myTuple = (10,20,30,40)
# # print("2nd index of myTuple is ",myTuple[2])
# # print()
# # print("myTuple is ",myTuple)
# #
# # # myTuple[2]=500
# # # print("2nd index of myTuple after update is ",myTuple[2])
# # # print()
# # # print("myTuple after update is ",myTuple)
# #
# #
# #
# # myString = "INDIA"
# # print("2nd index of myString is ",myString[2])
# # print()
# # print("myString is ",myString)
# #
# # # myString[2]="d"
# # #
# # # print("2nd index of myString after update is ",myString[2])
# # # # print()
# # # # print("myString after update is ",myString)
# # # myDict = {12: 45, "height":6, (14,5,4,4): 300}
# # # print()
# # # print("myDict[12] is ",myDict[12])
# # #
# # #
# # # myDict = {12: 45, "height":6, (14,5,4,4): 300}
# # # print()
# # # print("myDict[12] is ",myDict[12])
# # #
# # # myDict[12] = 90
# # # print()
# # # print("myDict after update is ",myDict)
# # list=[1,2,3,4,5]
# # print("2nd index of list is",list[2])
# # print("list is",list)
# # list[2]=6
# # print("2nd index of  list after update is",list[2])
# # print("list after update is",list)
# #
# # tuple=(1,2,3,4,5)
# # print("2nd index of tuple is",tuple[2])
# # print("list is",tuple)
# #
# # str="1,2,3,4,5"
# # print("2nd index of str is",str[2])
# # print("list is",str)
#
# # set={4,8,5,8,5,5,7}
# # set.add(10)
# # # print(set)
# # #
# # # set.remove(7)
# # # # print(set)
# #
# # Dict={12:[1,4,7],"rani":87,(1,2,3):67}
# # print()
# # print("Dict [12] is",Dict[12])
# #
# # Dict[12]=10
# # print()
# # print("Dict after update is",Dict)
# #
# # # myDict = {12: 45, "height":6, (14,5,4): 300}
# # # print()
# # # print("myDict[12] is ",myDict[12])
# # #
# # # myDict[12] = 90
# # # print()
# #
# # ##############
# # #Algorithm
# #
# # if   8>7:
# #     print("kerala")
# # elif 6>8:
# #     print("kala")
# # elif 9>0:
# #     print("jaipoor")
# # else:
# #     print("sree lanka")
# #
# # if   4>7:
# #     print("kerala")
# # elif 5>8:
# #     print("kala")
# # elif 9>5:
# #     print("jaipoor")
# # else:
# #     print("sree lanka")
# #
# # if   4>7:
# #     print("kerala")
# # elif 5>8:
# #     print("kala")
# # elif 4>5:
# #     print("jaipoor")
# # else:
# #     print("sree lanka")
#
#
# # #####################
# # import time
# # list=[1,2,3,3,3,4]
# # for a in list:
# #     if a %3==0:
# #         print(a)
# #     time.sleep(3)
# import time
# # list=[1,2,87,95,48,25]
# # for a in list:
# # #     if a %5!=2:
# # #         print(a)
# # # #     time.sleep(5)
# # # A={1,3,5,67}
# # # for s in A:
# # #     if s %2!=0:
# # #         print(A)
# # #     time.sleep(3)
# # import time
# # A=[1,2,3,4,5,6,7]
# # for a in A:
# #     if a%4!=0:
# #         print(a)
# #         time.sleep(2)
# #     else:
# #         print("hello")
#
# #function
# def addition(name1,name2):
#     print("name1 is",name1)
#     print("name2 is",name2)
#     if type(name1)==int and type(name2)==int:
#         print("addition is",name1+name2)
#     else:
#         if name1!=int:
#             print("name1 is invalied value for + operater")
#         if name2!=int:
#             print("input2 is invalied value please pass only integer type")
# addition(10,20)
#
#
#
#
#
#
#

# file_obj=open(r'C:\Users\evasu\OneDrive\Documents\New_practice.txt','r')
# read_txt=file_obj.read()
# print(read_txt)
# file_obj.close()
# file_obj=open(r'C:\Users\evasu\OneDrive\Documents\New_practice.txt','r')
# read_txt=file_obj.readlines()
# print(read_txt)
# file_obj.close()

# file_obj=open(r'C:\Users\evasu\OneDrive\Documents\New_practice.txt','r')
# read_txt=file_obj.readline()
# print(read_txt)
# file_obj.close()

# file_obj=open(r'C:\Users\evasu\OneDrive\Documents\New_practice.txt','w')
# file_obj.write("india is beautiful country")
# file_obj.close()


# file_obj=open(r'C:\Users\evasu\OneDrive\Documents\New_practice.txt','w')
# file_obj.writelines(["india/n"," is/n ","beautiful/n"," country/n"])
# file_obj.close()

#
# file_obj=open(r'C:\Users\evasu\OneDrive\Documents\New_practice.txt','a')
# file_obj.write("india is beautiful country")
# file_obj.close()

file_obj=open(r'C:\Users\evasu\OneDrive\Documents\New_practice.txt','a')
file_obj.writelines(["india is beautiful country"])
file_obj.close()