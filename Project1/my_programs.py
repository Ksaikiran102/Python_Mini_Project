def fib(n):
    """Fibonocci series for n"""
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def Swap():
    """Swapping Two Numbers
    using a Temp varible"""
    a=int(input("Enter First Number: "))
    b=int(input("Enter Second Number: "))
    a,b=b,a
    print("a=",a)
    print("b=",b)
def GCD():
    """ Greatest Common Divisior 
    for given two numbers"""
    a=int(input("Enter First Number: "))
    b=int(input("Enter Second Number: "))
    while a!=b:
        if(a>b):
            a=a-b
        else:
            b=b-a 
    print(f"GCD of Two numbers :{a}")
def Rev():
    """Reversing a Number"""
    n=int(input("Enter a number:"))
    result=0
    while n>0:
        digit=n%10
        result = result*10+digit
        n=n//10
    print(f"Reversed Number is:{result}")
def Sum():
    """Sum of a digit for a Number"""
    n=int(input("Enter a Number:"))
    result=0
    while n>0:
        digit=n%10
        result+=digit
        n=n//10
    print(f"Sum of Number:{result}")
def Vow():
    """Counting vowel in a Given String"""
    string=input("Enter a String:").lower()
    v="aeiou"
    #vowel=list(v)
    #s=list
    count=0
    for i in string:
        if i in v:
            count+=1
    print(f"Count is:{count}")
def Word():
    """Counting words in a Given Sentence"""
    Sen=input("Enter Sentence:")
    l=list(Sen)
    Count=1
    for i in range(len(l)-1):
        if l[i]==" " and l[i+1]!=" ":
            Count+=1
    print(Count)
def Title():
    """Making a String into Title Case"""
    string=input("Enter a String: ").title()
    print(f"Title Case of string is {string}")
def Palin():
    """Checking Weather Given String or Number is a Palindrome or Not"""
    while True:
        p=input("You want check Palindrome for (string/digit):").lower()
        if p=='string':
            string=input("Enter a string:")
            if(string==string[::-1]):
                print(f"{string} is a Palindrome")
            else:
                print(f"{String} is not a Palindrome")
            break
        elif p=="digit":
            digit=int(input("Enter a digit:"))
            d=digit
            rev=0
            while(d>0):
                b=d%10
                rev=rev*10+b
                d=d//10
            if digit == rev:
                print("{digit} is Palindrome")   
            else:
                print("{digit} is Not Palindrome")
            break   
        else:
            print("Invaild!! Please Choose String or Digit")
def Prime():
    """Checking Weather Given Number is Prime NUmber or Not"""
    n=int(input("Enter a number:"))
    if n<=1:
        print(f"Number:{n} is not a Prime Number")
    else:
        for i in range(2,n):
            if n%i==0:
                print(f"Number:{n} not a Prime Number")
                break
        else:
            print(f"Number:{n} is Prime Number")
def Fact(n):
    """Returns Factorial a Given Number"""
    while(n>0):
          if(n==0 or n==1):
            return 1
          else:
            return n*Fact(n-1)
    else:
        return "no negitive"
def Large():
    """Returns Largest Of a 3 Given Numbers"""
    n1,n2,n3=map(int,input("Enter three number n1,n2,n3: ").split(","))
    if n1==n2==n3:
        print("All Three are Equal")
    elif n1==n2 and n1>n3:
        print(f"n1={n1} and n2={n2} are equal and Greater than n3={n3}")
    elif n2==n3 and n2>n1:
        print(f"n2={n2} and n3={n3} are equal and Greater than n1={n1}")
    elif n1==n3 and n1>n2:
        print(f"n1={n1} and n2={n2} are equal and Greater than n2={n2}")
    elif n1>n2 and n1>n3:
        print(f"n1={n1} is Greater n2 and n3")
    elif n2>n1 and n2>n3:
        print(f"n2={n2} is Greater n1 and n3")
    elif n3>n1 and n3>n2:
        print(f"n3={n3} is Greater n1 and n2")
def Dup():
    """Removing Duplicates from Given List"""
    l=list(map(int,input("Enter Elements:").split(",")))
    print(f"List with Duplicates:",l)
    b=set(l)
    c=list(b)
    print(f"List After Removed Dupliates:",c)
def Decimal():
    """converting Decimal to Binary
    for given number     """
    n=int(input("Enter a Number:"))
    print(bin(n))
               
            
