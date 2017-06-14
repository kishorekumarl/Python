def countPage():
    n=int(input("Enter the total page : "))
    count=0
    for i in range(n+1):
        i=str(i)
        count=count+i.count ("1")

    print(count)

def addEvenNumbers(num1,num2):
    n=0
    for i in list(range(num1,num2)):
        if (i%2==0):
           print("Even Number in the range: ", i)
           n+=i
    return print("addEvenNumbers   :",n)

def sumofDigit():
    n=int(input('Please enter a number: '))
    sum=0
    while(n!=0):
        sum=n%10+sum and n=n/10
        
        print(sum)

def func(n):
 
    return(n)
        
 
