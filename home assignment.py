# 1:- home assignmt  (percentage method)


# bonus = 15000
# percentage = 22%
# after 6 mnths incresed

# percentage convert into decimal
# 22/100 = 0.22

# b= int(input("enter ur bonus"))
# p = int(input('enter ur percentage'))
# new_bonus = b + b * p                 (formula 1)
# per=p/100                             (other formula)   
# new_bonus = per*b                         (o f)
# print(new_bonus)


#  2:- home assignmt  (replace method)

# a = 'Jaranwala Faislabad Lahore Karachi Multan'


# b = a.replace('J','j').replace('F','f').replace('L','l'). replace('K', 'k').replace('M','m')

# print(b)


    
# ls= ['lahore', 'multan' , 'karachi' , 'sindh' , 'quetta' , 'islamabad' , 'sharaqpur' , 'jaranwala' , 'gujranwala', 'jhelum']
# lp = []
# for a in ls:
#     p = a[0:1].upper() + a[1:-1].lower() + a[-1:].upper()
#     # lp.append(p)
#     lp.insert(0,p)
# #     print(p)
# print(lp)


# ls = ['noor' ,'hoor' , 'nehmal']
# lp = []
# for a in ls:
#     b = a[0:1].lower()  + a[1:-1].upper() + a[-1:].lower()
#     lp.insert(0,b)
#     print(b)
# print(lp)n




# # c = ('lahore', 'karachi','multan')           # Using Capitalize   

# l= list(c)
# print(l)
# p = l[0].capitalize() + ' ' + l[1].capitalize() + ' ' + l[2].capitalize()
# print(p)

# tup = tuple(p.split())
# print(tup)


# c = ('lahore', 'karachi','multan')              using for loop
# l = []
# for i in c:
#     p= i[0].upper() + i[1:].lower()
    
#     l.append(p)
# tup = (tuple(l))
# print(tup)


# c = ('lahore', 'karachi','multan')                  list comprehension

# p = [x[0].upper() + x[1:].lower() for x in c]

# print(p)
# print(tuple(p))


# c = ('lahore', 'karachi','multan')                       if-else
# l = []
# for x in c:
#     if x : 
#         p = x[0].upper() + x[1:].lower()
#     else:
#         p = x
#     l.append(p)
# tup = tuple(l)
# print(tup)
        
        
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

