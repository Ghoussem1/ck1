
# Question 1:
fname = input("First Name : ")
lname = input("Last Name : ")
print (lname + " " + fname)

# Question 2:
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

# Question 3:
num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")

# Question 4:
gh=[]
for x in range(2000, 3200):
    if (x%7==0) and (x%5==0):
        gh.append(str(x))
print (','.join(gh))

# Question 5:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))

# Question 6:
str1 = input("Please Enter your Own String : ")

str2 = ''

for i in range(len(str1)):
    if (i % 2 == 0):
        str2 = str2 + str1[i]

print("Original String :  ", str1)
print("Final String :     ", str2)

# Question 7:
amt = int(input("Enter Sale Amount: "))

if(amt>0):
    if amt<200:
       disc = amt*0.10
    elif amt<=200:
        disc=amt*0.30
    elif amt<500:
        disc=0.30 * amt
    else:
         disc=0.5 * amt

    print("Discount : ",disc)
    print("Net Pay  : ",amt-disc)
else:
    print("Invalid Amount")
