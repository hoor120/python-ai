#   class assignment  1

# edu=int(input("enter your education"))
# age=int(input("enter your age"))
# hight=int(input("enter your hight"))
 
# if(edu >= 12 and(age <= 32 and age >= 18)):
#     print ("passed")
# elif((age <= 32 and age >= 18 )and hight >= 5.6):
#     print("passed")
# elif(hight >= 5.6 and edu >= 12):
#     print("passed")
# else:
#     print("not passed")

# class assigmnt   2

# marks =int(input( "enter ur marks"))
# total_num = int(input("enter ut total num"))
# percentage = marks / total_num*100
# print(percentage)

# class assigment  3

# marks =int(input("marks"))
# total_num = int(input("total_num"))
# percentage = marks / total_num*100 
# print(percentage)


# class assignment   4                  reverse methode


 
# ls = [ "lahore","Faisalabad","jaranwala"]
# lp = []
# for x in ls:
#     lp.insert(0,x)
# print(lp)


# class assignment    5    


#     write table of 2

# num = 2

# a = int(input('enter ur num'))
# for i in range(1,11):
#     print(num, '*' ,i ,'=' , num*i)


#  class assignment    6

         
#     seprate 3 in 100


# # count = 0
# for i in range(1,101):
#     count += str(i).count("3")
# print(count)

    
#  class assignment     7i   
    
    
#     # find fictorial
    
# a = int(input('enter ur value'))
# fic = 1
# for i in range(1 , a+1):
#     fic = fic*i
# print(fic)
    
# import math                               factorial
# print(math.factorial(int(input('enter ur num'))))


# class assignmnt             8
# tuple methode

# tup = ('lahore ', 'multan','karachi')
# ls = list((tup))
# ls = ls[0].upper() + [1:].lower()
# print(ls)



# tup = (1,2)
# print(tup)
# print(type(tup))


# assignment no       9

# st ={'item1' , 'item2'}
# (st1 , st2) = st
# st1 = {'mobile'}
# st2 = {'fan'}
# st.update(st1)
# st.update(st2)
# print(st)
# ls =list((st))
# print(ls)
# tup = tuple(st)
# print(tup)


# ls =['apple', 'mango']
# tup = ('apple', 'kiwi')
# ls2 = list(tup) + ls
# # print(ls2)
# st3={'orange'}
# st = set(ls2)
# print(st)
# st2 = st3.union(st)
# print(st2)
# st2 = st3-(st)
# print(st2)





# t = (1,2,3,4,5,6,7,8,9,10)
# (tup1 , tup2 ,tup3,tup4 , tup5 , tup6 , tup7, *tup8 ,tup9) = t
# print(tup8)                                                                                                                                                         
# # ls = list(t)
# tup8.append(11)
# print(tup8)
# st = set(tup8)
# print(st)

# assinment                10

# n_dic = {'entery 1':{'name': "sana" , 'age' : 23} ,'entery 2': {'name': 'eman' , 'age' :34}}
# print(type(n_dic))

# n_dic.['entery 2']['name'] = 'hoor'
# print(n_dic)


# assignment          11 (5 cities leni or aik city user s leni or dono ko compare krna then print clean agr wo city apki list m h ni to not clean)

# flag method 

# def fun (c):
#     alp = False
#     ls = ['lahore', 'multan','islamabad','karachi','jaranwala']
    
#     for city in ls:
#         if city == c :
#             alp = True
#     if(alp):
#         print('city is  clean')
#     else:
#         print('city is not clean')
# c = (input('enter ur city'))
# fun(c)


# 2nd method


# def fun (c):
#     ls = ['lahore', 'multan','islamabad','karachi','jaranwala']
#     if c in ls :
#         print ('ur city is clean')
#     else:
#         print('ur city in not')
        
# c = (input('enter ur city'))
# fun(c)
        
        
        
    # assignment.......   12
    
# def fun():
    # alp = False
#     num = 50 + 70-20 *2 /5
#     print(num)
#     if (num>=50 and num<=500):
#          alp = True
#     if(alp):
#         print('true')
#     else :
#         print ('false')
        
# fun()



    # assignmnt 13............ setter / getter 


# class Sum():
#     def setSum(self,a,b):
#         self.a = a
#         self.b = b
#     def getSum(self):
#         print(f'{self.a + self.b}')
# qa = Sum()
# qa.setSum(15,20)
# qa.getSum()


# assignment 14 .................... constructor

# class Girls():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def getGirls(self):
#         print(f'{self.name}:{self.age}')
# g1 = ('noor',6)
# g2 = ('nehmal',4)
# g3 = ('ali',23)
# g4 = ('akram',33)
# g5 = ('mano',33)
# girls = [g1,g2,g3,g4,g4,g5]
# for name , age in girls:
#     girls = Girls(name,age)
#     girls.getGirls()

# single inheitence.............

# class Person:
#     def show_name(self,name):
#         self.name = name
#         print(name)
# class Student(Person):
#     def show_roll_num(self,roll_num):
#         self.roll_num = roll_num
#         print(roll_num)

# ab = Student()
# ab.show_name('ali')
# ab.show_roll_num(11)


# multi level...................

# class Grandfather():
#     def show_grandfather(self):
#         print('i am grandfather')

# class Father(Grandfather):
#     def show_father(self):
#         print('i am father')

# class Son(Father):
#     def show_son(self):
#         print("i am son")


# ab = Son()
# ab.show_father()
# ab.show_grandfather()
# ab.show_son()

# multiple inheritance------------------------

# class Mother:
#     def show_Mother(self):
#         print("i am mother")
# class Father:
#     def show_Father(self):
#         print("i am father")
        
# class Child(Father,Mother):
#     def show():
#         print('I am a child')
        
        
# c=Child()

# c.show_Father()


# oopss


# class Employee:
    
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age=age
        
#     def display(self):
#         print(f'Employee name {self.name} and age is {self.age}')
        
  
# emp = Employee('asad',24)

# emp.display()      
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        