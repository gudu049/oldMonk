# # a=float(input("enter a number"))
# # b=float(input("enter second number"))
# # c=input("what you want to do")
# # print("sum",a+b)

# # str1=("suvenp")
# # a=(str1[0:4-1:4])
# # print(a)

# a=int(input("enter a number: "))
# b=int(input("enter another number: "))
# c=input("what to do give the symbol: ")
# if(c=="+"):
#     print(a+b)
# if(c=="*"):
#     print(a*b)
# if(c=="-"):
#     print(a-b)
# if(c=="/"):
#     # try:
#     print(a/b)
#     # except:
#     #     print("An exception occurred")


# a=input("colour of light")

# if(a=="red"):
#     print("if you go you pay 5000 fine")
# if(a!="red"or"green"or"yellow"):
#     print("go home and sleep")


# a=("harichandan kar")
# # a.replce('a','')
# print(a.replace('a',''))

# a=int(input())

# for i in range(1,6):
#     for j in range(5):
#         print(i,end=" ")
#     print(end="\n")



#wrong approach
# for i in range(1,6):
#     if i%2==0: 
#        for j in (0,0,0,0,0):
#            print(j,end=" ")
#     else:     
#         for j in (1,1,1,1,1):
#            print(j,end=" ")
#     print(end="\n")


#right approach
# for i in range(1,6):
#     for j in range(1,6):
#      if i%2==0: 
#        print(0,end=" ")
#      else: 
#         print(1,end=" ")
#     print(end="\n")



# for i in range(1,9):
#    for j in range(i):
#         print("*",end=" ")
#    print()
     


# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()




# for i in range(1,6):
#     for j in range(5,0,-1):
#         if j>i:
#           print(" ",end="")
#         else:
#             print(j,end="")
#     print()


# for i in range(5,0,-1):
#     for j in range(1,6):
#         if i>j:
#           print(" ",end="")
#         else:
#             print(j,end="")
#     print()




# for i in range(1,6):
#     for j in range(1,6):
#         if i>j:
#           print(" ",end="")
#         else:
#             print(j,end="")
#     print()




# for i in range(1,6):
#     for j in range(1,i+1):
#         if j%2==0:
#             print("0",end="")
#         else:
#             print("1",end="")
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end="")
#     print()




# for i in range(1,6):
#     for j in range(1,):
#         if i%2==0 and j%2==0 :
#           print("*",end="")
#         elif i%2==1 and j%2==1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()






# n=int(input("enter a number"))
# for i in range(n,0,-1):
#     a=(i-1)
#     print(" "*a,end="")
#     for j in range(n,i-1,-1):
#         if i<=j:
#            print(j,end="")
        
#     print()



# for i in range(5,0,-1):
#     a=i-1
#     print(" "*a,end="")
#     for j in range(5,i-1,-1):
#         if i<=j:
#          print("* ",end="")
#     print()




# for i in range(1,6):
#     a=i-1
#     print(" "*a,end="")
#     for j in range(1,6):
#         if i<=j:
#             print("* ",end="")
#     print()



# n=int(input("enter a number"))
# for i in range(1,n+1):
#     a=n-i
#     print(" "*a,end="")
#     for j in range(1,n+1):
#         if i>=j:
#             print(j," ",end="")
#     print()
    


# for i in range(1,6):
#     a=5-i
#     print(" "*a,end="")
#     for j in range(1,i+1):
#         if j==1 or j==i:
#             print(1,"",end="")
#         else:
#             print(j,"",end="")
#     print()



# for i in range(1,6):
#     a=5-i
#     print(" "*a,end="")
#     for j in range(1,i+1):
#         if j==1 :
#             print(1,"",end="")
#         else:
#             print(j,"",end="")
#     print()


# for i in range(1,6):
#     a=5-i
#     print(" "*a,end="")
#     for j in range(1,i+1):
#         if j==1 or j==i:
#             print(1,"",end="")
#         else:
#             print(j,"",end="")
#     print()




# a=int(input("Enter a number :"))
# if a>0 and a%2==0:
#     print("Positive even")
# elif a>0 and a%2==1:
#     print("Positive odd")
# elif a<0:
#     print("Negetive")
# else:
#     print("Zero")

   

###########################################################################
# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(i,end="")
#     print()


# a=2
# for i in range(5,0,-1):
#     for j in range(1,a):
#         print(i,end="")
#     print()
#     a=a+1
   
# a=5
# for i in range(1,6):
#     for j in range(i):
#         print(a,end="")
#     print()
#     a=a-1

# 5
# 44
# 333
# 2222
# 11111
##############################################################################

# a=int(input("Enter a number :"))
# if a==0:
#     print("Zero")
# b=a/2
# c=int(b)
# if a>0:
#     print("Positive ",end="")
# elif a<0:
#     print("Negative ",end="")
# if 2*c!=a:
#     print("odd")
# elif 2*c==a:
#     print("Even")
# # elif b-c==0.0:
# #     print("Even")
# else:
#     print("enter a valid integer")



# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(j,end="")
#     print()


# a=1
# while a<=10:
#     b=1
#     while b<=10:
#         print(f"{a}x{b}={a*b}")
#         b=b+1
#     a=a+1


#############factorial of a number##############

# n=int(input("Enter a number :"))
# a=1
# for i in range(1,n+1):
#     a=a*i
# print(a)



# n=int(input("Enter a number :"))
# a=1
# b=1
# while a<=n:
#     b=b*a
#     a=a+1
# print(b)


##########check number is prime or not############

# n=int(input("Enter a number"))
# a=0
# for i in range(1,n+1):
#     if n%i==0:
#      a=a+1
# if a<=2:
#        print("prime")
# else:
#       print("not prime")



# n=int(input("Enter a number"))
# a=1
# b=0
# while a<=n:
#     if n%a==0:
#         b=b+1
#     a=a+1
# if b<=2:
#     print("prime")
# else:
#     print("not prime")


########### print prime number###############



# n=int(input("Enter a number"))
# for i in range(1,n+1):
#     a=0
#     for j in range(1,i+1):
#      if i%j==0:
#       a=a+1
#     if a<=2:
#       print(i)
        



# n=int(input("Enter a number"))
# a=1
# while a<=n:
#   b=1
#   c=0
#   while b<=a:
#       if a%b==0:
#         c=c+1
#       b=b+1
#   if c<=2:
#         print(a)
#   a=a+1




#########  palindrome  ##########
# n=int(input("Enter a number"))
# a=n
# rev=0
# while a>=1:
#     b=a//10
#     c=a%10
#     rev=(rev*10)+c
#     a=b
# if n==rev:
#     print("palindrome")
# else:
#     print("not")




# for i in range(1,6):
#     a=5-i
#     print(a*" ",end="")
#     for j in range(1,i+1):
#         if j==1 or i==j:
#             print(1," ",end="")
#         else:
#             print(j," ",end="")
        
#     print()



# for i in range(1,6):
#     a=5-i
#     print(a*" ",end="")
#     for j in range(1,i+1):
#         if j==0 or i==j:
#             print(1,end="")
#         else:
#             print(j,"",end="")
#     print()


########### reverse number pattern#############
# for i in range(5,0,-1):
#     print(i*" ",end="")
#     for j in range(5,i-1,-1):
#         print(j,end="")
    
#     for k in range(i+1,6):
#         print(k,end="")
#     print()

 



# for i in range(5,0,-1):
#      for j in range(i,6):
#           print(j,end="")
#      print()

#####################


############## arrow printing#############

# for i in range(1,6):
#     a=5-i
#     print(a*" ",end="")
#     for j in range(1,i+1):
#         print("* ",end="")
#     print()
# for k in range(10):
#     a=3
#     print(a*" ",end="")
#     for l in range(2):
#         print("* ",end="")
#     print()


# for i in range(1,16):
#     if i <6:
#      a=5-i
#      print(a*" ",end="")
#      for j in range(1,i+1):
#         print("* ",end="")
     
#     else:
#        print(3*" ",end="")
#        for k in range(2):
#           print("* ",end="")
#     print()

#############################



################### Diamond printing######################
# for i in range(1,10):
#    if i<6:
#     a=5-i
#     print(a*" ",end="")
#     for j in range(1,i+1):
#         print("* ",end="")
#    else:
#        b=i-5
#        print(b*" ",end="")
#        for k in range(4,b-1,-1):
#          print("* ",end="")
#    print()

    
# n=int(input("please enter a odd number"))
# a=(n//2)+1
# for i in range(1,n+1):
#     if i<a+1 :
#         b=a-i
#         print(b*" ",end="")
#         for j in range(1,i+1):
#             print("* ",end="")
#     else:
#         b=i-a
#         print(b*" ",end="")
#         for k in range(a-1,b-1,-1):
#             print("* ",end="")
#     print()


######################################################

############# floyds triangle##########
# a=0
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(a+1,"",end="")
#         a=a+1
#     print()
#############

############ Hollow triangle##########

# n=int(input("enter a number :"))
# for i in range(1,n+1):
#     a=n-i
#     print(a*" ",end="")
#     for j in range(1,i+1):
#         if j==1 or i==j or i==n:
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()
#######################

############## butter fly###########333
# for i in range(1,8):
#     if i<5:
#      for j in range(1,i+1):
#         print("*",end="")
#     else:
#        b=9-i
#        for k in range(1,b):
#           print("*",end="")
#     print()



# n=int(input("enter a even number"))
# c=n//2
# a=n-2
# b=2
# for i in range(1,n):
#   if i<=c:
#     for j in range(1,i+1):
#         print("*",end="")
#     print(a*" ",end="")
#     for k in range(1,i+1):
#         print("*",end="")
#     a=a-2
#     print()
#   else:
#     for l in range(n-i,0,-1):
#         print("*",end="")
#     print(b*" ",end="")
#     for m in range(n-i,0,-1):
#         print("*",end="")
#     b=b+2
#     print()

############################################





# for i in range(1,5):
#     for j in range(1,i+2):
#         print("*",end="")


################ hollow square ##########
# n=int(input("Enter a number"))
# for i in range(1,n):
#     for j in range(1,n):
#         if i==1 or i==n-1 or j==1 or j==n-1:
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()
############################


################# hollow diamond###############################
# n=int(input("Enter a even number"))
# b=1
# c=n//2
# for i in range(1,n):
#    if i<=c:
#     a=c-i
#     print(a*" ",end="")
#     for j in range(1,c+1):
#         if j==1 or i==j:
#             print("* ",end="")
#         else:
#             print("  ",end="")
    
#    else:
#      print(b*" ",end="")
#      for k in range(n-1,i-1,-1):
#         if k==n-1 or k==i:
#           print("* ",end="")
#         else:
#           print("  ",end="")
#      b=b+1
#    print()
        

   
       
    
 ##### sub part  
# a=5
# for i in range(1,6):
#     for j in range(1,a):
#         if j==1 or i==a-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     a=a-1
#     print()



# for i in range (5,0,-1):
#     a=5-i
#     print(a*" ",end="")
#     for j in range(1,i+1):
#         if i==j or j==1:
#          print(1,"",end="")
#         else:
#            print("  ",end="")
#     print()

# a=1
# for i in range(6,10):
#     print(a*" ",end="")
#     for j in range(9,i-1,-1):
#         if j==9 or j==i:
#            print(1,"",end="")
#         else:
#             print("  ",end="")
#     a=a+1
#     print()

############################################################



#### for print 'x' type pattern######
# b=4
# for i in range(1,10):
#     if i<5:
#         a=i-1
#         print(a*" ",end="")
#         for j in range(5,0,-1):
#            if j==5 or i==j:
#              print("* ",end="")
#            else:
#              print("  ",end="")
#         print()
#     else:
#         print(b*" ",end="")
#         for k in range(5,10):
#             if k==5 or i==k:
#               print("* ",end="")
#             else:
#               print("  ",end="")
#         b=b-1
#         print()

   


# n=int(input("enter a even number"))
# c=n//2
# b=c-1
# for i in range(1,n):
#     if i<c:
#         a=i-1
#         print(a*" ",end="")
#         for j in range(c,0,-1):
#            if j==c or i==j:
#              print("* ",end="")
#            else:
#              print("  ",end="")
#         print()
#     else:
#         print(b*" ",end="")
#         for k in range(c,n):
#             if k==c or i==k:
#               print("* ",end="")
#             else:
#               print("  ",end="")
#         b=b-1
#         print()

##### correct version
# n=int(input("Enter a even number"))
# for i in range(1,n):
#     for j in range(1,n):
#         if i==j or i+j==n:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()



####################################################

############## pascal triangle###############
# b=[]
# for i in range(1,6):
#     a=[]
#     for j in range(1,i+1):
#         if j==1 or i==j:
#             a.append(1)
#             print(1,end="")
#         else:
#               x=0
#               y=1
#               for k in range(len(b)):
#                  if y<len(b):
#                   a.append(b[x]+b[y])
#                   print(b[x]+b[y],end="")
#                   x=x+1
#                   y=y+1

#     b=a
#     print(b)

#### original
# n=int(input("enter a number"))
# b=[]
# for i in range(1,n):
#     z=n-i
#     print(z*" ",end="")
#     a=[]
#     x=0
#     y=1
#     for j in range(1,i+1):
#         if j==1 or i==j:
#             a.append(1)
#             print(1,"",end="")
#         else:
#               a.append(b[x]+b[y])
#               print(b[x]+b[y],"",end="")
#               x=x+1
#               y=y+1
#     b=a
#     print()
#######################################

############ Concentric Square( not succsess) ###########

# a=1
# b=5
# for i in range(1,6):
#     for j in range(1,6):
#         if (i==a or i==b) or (j==a  or j==b):
#             print(b,"",end="")
#         elif (i==3 and j==3):
#             print(b-2,"",end="")
#         else:
#             print(b-1,"",end="")
#     print()


# n=6

# for i in range(1,n):
#     for j in range(1,n):
#         if 

##################################


############## sand watch ###############


# n=int(input("Enter a even number"))
# for i in range(1,n):
#     for j in range(1,n):
#         if i==1 or i==n-1 or i==j or i+j==n:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

######################

############## hollow diamond with cross ################
# b=1
# for i in range (1,10):
#     if i<6:
#         a=5-i
#         print(a*" ",end="")
#         for j in range(1,i+1):
#            if j==1 or i==j or (i==5 and j==3):
#             print("* ",end="")
#            elif  (i==4 and j==2):
#               print(" *",end="")
#            else:
#             print("  ",end="")
#         print()
#     else:
#         print(b*" ",end="")
#         for k in range(9,i-1,-1):
#          if k==9 or i==k:
#             print("* ",end="")
#          elif i==6 and k==8:
#             print(" *",end="")
#          else:
#             print("  ",end="")
#         b=b+1
#         print()

##################

############## hollow butterfly ##############
# for i in range(1,10):
#     for j in range(1,10):
#         if j==1 or j==9 or i==j or i+j==10:
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()
    
#############################


################ Hollow Diamond in a Square #############################
# a=0
# b=1
# for i in range(1,8):
#     for j in range(1,8):
#         if i==1 or i==7 or j==1 or j==7 :
#             print("* ",end="")
#         elif (i>1 and i<5) and (j==4-a or j==4+a):
#             print("* ",end="")
#         elif i>4 and (j==4-b or j==4+b):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     if i>1 and i<5:
#         a=a+1
#     if i>4:
#         b=b-1

#     print()

##### for n number####

# n=int(input("Enter a even number"))
# c=n//2
# a=0
# b=c-3
# for i in range(1,n):
#     for j in range(1,n):
#         if i==1 or i==n-1 or j==1 or j==n-1 :
#             print("* ",end="")
#         elif (i>1 and i<c+1) and (j==c-a or j==c+a):
#             print("* ",end="")
#         elif i>c and (j==c-b or j==c+b):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     if i>1 and i<c+1:
#         a=a+1
#     if i>c:
#         b=b-1

#     print()
################################################################


################# prime number pyramid ########################
# n=int(input("Enter a number :"))
# a=[]
# for i in range(1,n):
#     c=0
#     for j in range(1,i+1):
#         if i%j==0:
#             c=c+1
#     if c==2:
#         a.append(i)
# b=len(a)
# c=1
# d=0
# while b>0:
#     b=b-c
#     d=d+1
#     c=c+1
# e=0

# for k in range(1,d+1):
#     z=d-k
#     print(z*" ",end="")
#     for l in range(1,k+1):
#         if e<len(a):
#            print(a[e],"",end="")
#            e=e+1
#         else:
#             print("* ",end="")
#     print()


################################################

################## Sierpinski Triangle ################
# n=int(input("enter a even number :"))
# d=n/2
# b=2
# c=1
# for i in range(1,n):
#     a=(n-1)-i
#     print(a*" ",end="")
#     for j in range(1,i+1):
#         if i==n-1 or j==1 or i==j or i==d:
#             print("* ",end="")
#         elif i>d and (j==b or j==i-c):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     if i>d:
#         b=b+1
#         c=c+1
#     print()


###########################################

############## iconic white point #############
# a=5
# b=10
# for i in range(1,30):
#     for j in range(1,15):
#         if i==1 and (j==6 or j==7 or j==8):
#             print(" *",end="")
#         elif i<3 and (j==5 or j==9  ):
#             print(" *",end="")
#         elif i>2 and i<7 and(j==5 or j==10):
#             print("* ",end="")
#         elif i==7 and(j==4 or j==10):
#             print(" *",end="")
#         elif i>7 and i<10 and (j==a or j==b):
#             print("* ",end="")
#         elif i==10 and (j==2 or j==13):
#             print("* ",end="")
#         elif i==11 and (j==1 or j==14 ):
#             print("* ",end="")
#         elif i>11 and(j==1 or j==14 or i==29):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     if i>7 and i<10:
#         a=a-1
#         b=b+1
#     print()
#########################################


############### old monk#################

# a=1
# b=2
# for i in range(1,36):
#     for j in range(1,30):
#         if (i==1 or i==5) and (j==13 or j==14 or j==16 or j==15):
#             print("* ",end="")
#         elif (i<6) and (j==12 or j==17):
#             print("* ",end="")
#         elif (i==6) and (j==12-a or j==16+a):
#             print(" *",end="")
#         elif (i==7) and (j==12-1 or j==17+1):
#             print("* ",end="")
#         elif ( i==9 or i==8 or i==10) and (j==10 or j==18):
#             print(" *",end="")
#         elif (i>10 and i<15) and(j==11-b or j==18+b):
#             print("* ",end="")
#         elif (i==15 or i==34 ) and (j==2 or j==26):
#             print(" *",end="")
#         elif (i>15 and i<34) and (j==1 or j==27):
#             print(" *",end="")
#         elif i==35 and(j>2 and j<26):
#             print(" *",end="")
#         else:
#             print("  ",end="")
#     if i>5 and i<8:
#         a=a+1
#     if i>10 and i<15:
#         b=b+2
#     print()
##############################################################

################## pyramid ##########
# i=1
# while i in range (1,6):
#     a=5-i
#     print(a*" ",end="")
#     j=1
#     while j in range(1,i+1):
#         print("* ",end="")
#         j=j+1
#     i=i+1
#     print()

############################

#############3 diamon in while #############
# b=1
# i=1
# while i in range(1,10):
#     if i<6:
#         a=5-i
#         print(a*" ",end="")
#         j=1
#         while j in range (1,i+1):
#             print("* ",end="")
#             j=j+1
#         print()
#         i=i+1
#     else:
#         print(b*" ",end="")
#         k=9
#         while k in range(9,i-1,-1):
#             print("* ",end="")
#             k=k-1
#         print()
#         i=i+1
#         b=b+1
####################################




        













