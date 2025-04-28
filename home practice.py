# if  elif  else statement


# a= int(input('enter ur age'))
# b= int(input('enter ur experience'))

# if a== 20 and b ==2 :
#     print ('create ur id')
# elif a >= 50  and  b >=5  :
#     print('create ur id with premium gifts')
# elif a <10 and b <1 :
#     print('only enter data')
# else:
#     print('stay connected') 
    
# a = int(input('enter ur num'))
# b = int(input('enter ur age'))
# if a >= 10 and b >= 20:
#     print ('pass')
# elif a >= 30 and b >= 35:
#     print('excellent')
# else:
#     print('fail')
        
        
#    percentage practice

# t = int(input('enter your bonus'))
# d = int(input('enter your percentage'))
# e = int(input('enter your leave days'))
# p = d/100
# new_bonus = t*p-e
# print(new_bonus)

# length practice

# f = ['amna', 'hoor', 'eman']
# print (len(f))

# uper and lower case practice

# a = 'FATIMA'
# b = 'ARSHAD'
# print(a[0:6].lower() + ' '+ b[0:6].lower())

# s= 'sanaarshad'
# print(s[0:10].upper())

# string silicing

# a = 'good work'
# print(a[1:2])

# v= 'nvttc PYTHON'
# print(v[-4:-2])

# q = 'further clarification!'
# print(q[5:9])

# split string

# w = 'wlcome : home'
# print(w.split(':'), w)

# q = 'string in python'
# print(q.split(' '), q ,len(q), q[2:6])

# for loops

# ls = ['pakistan' , 'dubai', 'england']
# lp = []
# for a in ls:
#     b = a[:-1].lower() + a[-1].upper()
#     lp.append(b)
#     lp.insert(0,a)
#     print(b)
# print(lp)

# ls = ['canda' , 'england', 'germany']
# lp = []
# for a in ls:
#     p = a[-1].upper() + a[0:].lower()
#     print(p)
#     lp.insert(0 , a)
    
# print(lp)


# list comprehension
# square of 2 range 1,10

# x = [a**2 for a in range(1,11)]
# print(x)



# Filter even numbers from the list [12, 15, 18, 21, 24, 27, 30].

# num = [12, 15, 18, 21, 24, 27, 30]
# x = [a for a in num if a % 2 == 0]
# print(x)


#  Create a list of words from this sentence: "Python is a powerful language" but only include words with more than 3 letters.

# a = ("Python is a powerful language")
# x = [d for d in a.split() if len (d) >3]
# print(x)

# y = [1,2,3,4,5,6,7,8,9]
# r = [u*2 for u in y]
# print(r)


# n =[2,3,4,5,6,7,8,9]
# e = [w*2 for w in n]
# print(e)

# numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]
# e = [q for q in numbers if q % 10 == 0]
# print(e)

# numbers = [1, 5, 8, 12, 15, 18, 21, 24, 27, 30]
# e = [q for q in numbers if q % 2 == 0]
# print(e)

# numbers = [3, 7, 12, 18, 21, 25, 30, 35, 40, 42, 50]
# e = [q for q in numbers if q % 3 == 0 and q % 5 == 0]
# print(e)


# words = ["apple", "banana", "cherry", "date", "grape", "kiwi", "mango", "orange", "peach", "pear"]

# e = [q for q in words if q[0].lower() in  ('a,e,i,o,u')]
# print(e)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# w = [q**2 if q %2==0 else q*2 for q in numbers]
# print(w)


# names = ["Ali", "Ahmed", "Sara", "Usman", "Ayesha", "Bilal", "Umar", "Eman", "Farhan", "Iqra"]
# e = [q for q in names if q[0].lower() in  ('a,e,i,o,u')]
# print(e)


# t = (4,2,7,7,87)
# ls = list(t)
# print (ls)


# s1 = {1,2,True}
# s2 = {4,2,1}
# s3 = {5,4,6,}
# s4 = {7,8,9}

# s = s1 | s2 | s3 |s4
# print(s) 

# tup = tuple(s)
# print(tup)

# ls = list(tup)
# print(ls)



# tup = tuple(s1|s2|s3|s4)
# print(tup)


# ls = list(tup)
# print(ls)

# s0 = set(ls)
# print(s0)

# parameter (variables)
# arguments (values)


# def checknum(n):
#     if n %2 == 0:
#       print('even')
#     else:
#       print ('odd')
      
# x = int(input('enter ur num'))
# n = int(x)
# # print(n)
# checknum(n)


# def table(n):
#     for i in  range (1,11):
#         print(n , '*' , i ,'=' , n*i)
# s = int(input('enter ur num'))

# table(s)


# def fun():
#     a = ("hello world")
#     s = a.split("hello")
#     print(s) 
         
#     print(len(s[-1]))
# fun()


# c = "red|green|blue|yellow|purple"
# s = c.split('|')
# print(s)



# def fun():
#     f = "apple,orange,banana,grapes"
#     s = f.split(',')
#     print(s)
#     for f in s:
#         print(len(f))
# fun()


# def fun():
#     f = "apple mango banana cherry"
#     s = f.split(' ')
#     print(s)
#     for f in s:
#         print(len(f))
# fun()


# class Car:
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#     def info(self):
#         print(self.brand,self.model,self.year)
# c1 = Car('lamo',2,1990)
# c2 = Car('zamo',3,2009)

# c1.info()
# c2.info()


# class Person:
#     def __init__(self,name,age,marks):
#         self.name = name
#         self.age = age
#         self.marks = marks
#     def info(self):
#         print(f'{self.name} : {self.age} : {self.marks}')
#         total_marks = sum(self.marks)
#         print(total_marks/2)
        
# s1 = Person('mukeet',43,[65,35,35,53])
# s2 = Person('dua',24,[53,62,98])


# s1.info()
# s2.info()



# Class and Object Basics practice..................

# Ek class banaen Car naam ki, jisme model aur color attributes hon.
# Ek method ho show_details jo car ka model aur color print kare.

# Is class ka object banaen aur method call karein.

#                ans.....................


# class Car:
#     def __init__(self,model,colour):
#         self.model = model
#         self.colour = colour
#     def display(self):
#         print(f'ur car model is: {self.model} and ur car colour is : {self.colour}')

# c = Car('toyota','black')
# c.display()


        
    #  Constructor Practice.......................
    
    
    
    # Ek class Student banaen jisme name aur age constructor se milein.
# Ek method show_info banaen jo name aur age print kare.

# Do students ke objects banaen aur show_info method call karein.

#                anss.................


# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f'your name is {self.name} : your age is {self.age}')

# s1 = Student('hoor',22)
# s1.info()

# s2 = Student('eman',23)
# s2.info()


# Simple Inheritance.......................

# Ek class Animal banaen jisme ek method sound ho jo "Animal sound" print kare.
# Ek class Dog banaen jo Animal se inherit kare aur sound method override kare 
# taake "Bark" print ho.

# Dog ka object banaen aur sound method call karein.


 #  ansss................
            
# class Animal:
#     def sound(self):
#         print('animal sound')
# class Dog(Animal):
#     def sound(self):
#         print('bark')
        
# d = Dog()
# d.sound()
    
# List of Objects Practice...............


# Ek class Book banaen jisme title aur author ho.
# 3 books ke objects banaen aur unhein ek list mein daalein.
# List ko loop karke sab books ke details print karein.


 #    ans....................


# class Book():
#     def __init__(self,author,tittle):
#         self.author = author
#         self.tittle = tittle
#     def __str__ (self):
#         return(f'{self.author}:{self.tittle}')


# s1 = Book('jack','english')
# s2 = Book('frank','urdu')
# s3 = Book('max','math')

# s = [s1,s2,s3]

# for x in s:
#     print(x)


# Inheritance + Constructor practice................

# Ek class Person banaen jisme name aur age constructor mein milein.
# Ek class Employee banaen jo Person se inherit kare aur salary ka extra attribute le.

# Show method banaen jo sab kuch print kare.
# Employee ka object banaen aur method call karein.

        #   ans..................

# super methods..................


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age  = age
    
# class Employee(Person):
#     def __init__(self,name,age,salary):
#         super().__init__(name, age)
#         self.salary = salary
#     def show(self):
#         return(f'{self.name} : {self.age} : {self.salary}')

# emp = Employee('hoor','32',34000)
# print(emp.show())


# class  Vehicle:
#     def __init__(self,brand,model):
#         self.model = model
#         self.brand = brand
#     def show_infoo(self):
#         print(f'{self.brand}:{self.model}')
# class Car(Vehicle):
#     def __init__(self,brand,model,colour):
#         self.color = colour
#         super().__init__(brand,model)
        
#     def show_infoo(self):
#         print(f'{self.model}:{self.brand}:{self.color}')

# v = Car('boom',3,'gray')
# v.show_infoo()



# String Practice

# Q1: Ek string lo aur uska reverse print karo.

# s = ('hello')
# r = s[::-1]
# print(r)


# Check karo ke ek string palindrome hai ya nahi.

# n = 'nursesrun'

# s = n[::-1]
# if n==s:
#     print(True)
# else:
#     print(False)

# a = "A man a plan a canal Panama"
# s = a.lower().replace(' ','')

# if s ==s [::-1]:
#     print(True)
# else:
#     print(False)



# Count how many times each character appears in the string.


# sen = "apple orange apple banana apple orange"
# new_sen={}
# w = sen.split()
# for s in w:
#     if s in new_sen:
#         new_sen [s] += 1 
    
#     else:
#         new_sen[s] = 1

# print(new_sen)


# polymorphisam..............



# practice of Palindrome

# p = 'horsecar'
# d = p[::-1]
# if p==d:
#     print(True)
# else:
#     print(False)
    

# def func(f):
    
#     p = f[::-1]
#     if f==p:
#         print(True)
#     else:
#         print(False)
        
# func('racecar')
