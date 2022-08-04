# class employee:
#     def __init__(self,name,company,experience,salary):
#         self.name=name
#         self.company=company
#         self.experience=experience
#         self.salary=salary
#     def name_1(self):
#         print("employee name is{}".format(self.name))
#     def company_1(self):
#         print("employee company is{}".format(self.company))
#     def experience_1(self):
#         print("employee experience is{}".format(self.experience))
#     def salary_1(self):
#         print("employee salary is{}".format(self.salary))
# emp1=employee("sarala","wipro",5,50000)
# emp1.name_1()
# emp1.company_1()
# emp1.experience_1()
# emp1.salary_1()

file_obj=open(r'C:\Users\evasu\OneDrive\Documents\New_practice.txt','r')
read_txt=file_obj.read()
print(read_txt)
file_obj.close()
