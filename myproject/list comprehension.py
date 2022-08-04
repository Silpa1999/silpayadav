# with out comprehention
# myList=range(50)
# oddList=[]
#
# for item in myList:
#     if item%2 !=0:
#         oddList.append(item)
# print(oddList)
#
# MySilpa=[item for item in range(50) if item%2 !=0]
# print(MySilpa)
#

# Jai=[item for item in range(70) if item%5 ==0]
# print(Jai)
#
# kala=[item for item in range(100)if item%10 ==0]
# print(kala)
#
# latha=[item for item in range(90) if item%9!=0]
# print(latha)
#
# kavya=[item for item in range(10)if item %5==0]
# print(kavya)
#
# usa=[item for item in range(20)if item %3==0]
# print(usa)
#
# yash=[item for item in range (40)if item %4!=2]
# print(yash)
#

# k=[x for x in range(10) if x %5!=9]
# print(k)
#
# g=[w for w in range(190) if w %5!=9]
# print(g)

## With List comprehentions
# intList = [item for item in [1,2,"india", [4,5]] if type(item)==int]
# print(intList)
#
# intList = [item for item in [1,2,"india", [4,5]] if type(item)==str]
# print(intList)
# intList = [item for item in [1,2,"india", [4,5]] if type(item)==list]
# print(intList)
# intList = [item for item in [1,2,"india", [4,5],(12,33)] if type(item)==tuple]
# print(intList)
#
#
# Myfan=[1,2,(77,54)]
# List=[item for item in(Myfan) if type(item)==int]
# print(List)
#
# america=[1,2,(77,54),"kerala",{12:(9,9)}]
# link=[item for item in(america) if type(item)==dict]
# print(link)
#
# red=["hello",(5,9),[9,7],{75:(9,45)}]
# seetha=[item for item in(red) if type(item)==list]
# print(seetha)
#
# geetha=["hello",(5,9),[9,7],{75:(9,45)}]
# srinu=[item for item in(geetha) if type(item)==tuple]
# print(srinu)
#
# s=["hello",(5,4,6,9),[9,7],{75:(9,45)}]
# sree=[item for item in(s) if type(item)==tuple]
# print(sree)
#
# geethu=["hello",{1,3} , (5,9),[9,7],{75:(9,45)}]
# j=[item for item in(geethu) if type(item)==set]
# print(j)
#
#
# q=["hello",(5,9),[9,7],{75:(9,45)}]
# h=[item for item in(q) if type(item)==tuple]
# print(h)
#
# # Dict Comprehention
# K = [44,55,74,85,99]
# S= {d:False if d %2!=0 else True for d in  K}
# print(S)
#
# K = [78,45,96,15,46]
# S= {A:False if A%2!=0 else True for A in  K}
# print(S)
#
# r = [44,55,74,85,99]
# p= {h:False if h%2!=0 else True for h in  r}
 #print(p)
#
# c=[1,4,7,8]
# h={p:p**2 for p in c}
# print(h)
#
# g=[1,2,3,4,5]
# f={h:h**3 for h in g}
# print(f)
#
# p=[1,2,3,8,9]
# o = {h: h ** 4 for h in p}
# print(o)
#
#
# p = [7,8,9,4]
# o = {h: h ** 4 for h in p}
# print(o)
# #nested dictionary
# h={1:
#   {2:
#   {3:
#   {4:50} }}}
0# # print("h[1] is ",h[1])
# # print("h[2] is ",h[1][2])
# # print("h[3]is",h[1][2][3])
# # print("h[4]is",h[1][2][3][4])
# #
# # h={11:
# #   {12:
# #   {13:
# #   {14:50} }}}
# # print("h[1] is ",h[11])
# # print("h[2] is ",h[11][12])
# # print("h[3]is",h[11][12][13])
#
# ph={4:
#   {5:
#   {6:
#   {7:
#   {8:100}}}}}
# print("h[1] is ",ph[4])
# print("h[2] is ",ph[4][5])
# print("h[3]is",ph[4][5][6])
# print("h[4]is",ph[4][5][6][7])
# print("h[5]is",ph[4][5][6][7][8])
#
ph={9:
  {5:
  {2:
  {7:
  {1:400}}}}}
print("h[1] is ",ph[9])
print("h[2] is ",ph[9][5])
print("h[3]is",ph[9][5][2])
print("h[4]is",ph[9][5][2][7])
print("h[5]is",ph[9][5][2][7][1])
