from my_programs import *
def fun(choice):
    if choice==1:
        print("-----------Swap Function------------")
        print("Test Case 1: swap(10, 20) -> (20, 10)")
        print("Test Case 2: swap(5, -1) -> (-1, 5)")
        print("Explanation: Uses tuple unpacking to swap values without a temp variable.") 
        Swap()
    elif choice==2:
        print("-----------GCD Function------------")
        print("Test Case 1: gcd(24, 36) -> 12")
        print("Test Case 2: gcd(15, 20) -> 5")
        print("Explanation: Finds the Greatest Common Divisor using repeated subtraction.")
        GCD()
    elif choice ==3:
        print("-----------Reverse Number Function------------")
        print("Test Case 1: reverse(12345) -> 54321")
        print("Test Case 2: reverse(1002) -> 2001")
        print("Explanation: Reverses the digits of a number.")
        Rev()
    elif choice==4:
        print("-----------Sum Of Number Function------------")
        print("Test Case 1: sum_digits(1234) -> 10")
        print("Test Case 2: sum_digits(999) -> 27")
        print("Explanation: Adds all digits of the given number.")
        Sum() 
    elif choice ==5:
        print("-----------Vowel Count Function------------")
        print("Test Case 1: count_vowels('hello') -> 2")
        print("Test Case 2: count_vowels('Python') -> 1")
        print("Explanation: Counts the vowels (a, e, i, o, u) in a string.")
        Vow()
    elif choice==6:
        print("-----------Word Count Function------------")
        print("Test Case 1: count_words('Hello World') -> 2")
        print("Test Case 2: count_words('Python is easy') -> 3")
        print("Explanation: Counts the number of words in a sentence.")
        Word()
    elif choice == 7:
        print("-----------Title Case Function------------")
        print("Test Case 1: title_case('hello world') -> 'Hello World'")
        print("Test Case 2: title_case('python programming') -> 'Python Programming'")
        print("Explanation: Converts the first letter of each word to uppercase.")
        Title()
    elif choice ==8:
        print("-----------Palindrome Function------------")
        print("Test Case 1: palindrome('madam') -> True")
        print("Test Case 2: palindrome(121) -> True")
        print("Explanation: Checks whether the given string or number is a palindrome.")
        Palin()
    elif choice==9:
        print("-----------Prime Check Function------------")
        print("Test Case 1: is_prime(7) -> True")
        print("Test Case 2: is_prime(10) -> False")
        print("Explanation: Checks whether a number is prime.")
        Prime()
    elif choice==10:
        print("-----------Factorial Function------------")
        print("Test Case 1: fact(5) -> 120")
        print("Test Case 2: fact(0) -> 1")
        print("Explanation: Calculates the factorial of a number using recursion.")
        n=int(input("Enter a Number:"))
        print(f"Factorial of Number is:{Fact(n)}")
    elif choice==11:
        print("-----------Decimal to Binary Function------------")
        print("Test Case 1: decimal_to_binary(10) -> 1010")
        print("Test Case 2: decimal_to_binary(25) -> 11001")
        print("Explanation: Converts a decimal number to its binary representation.")
        Decimal()
    elif choice ==12:
        print("-----------Largest of Three Function------------")
        print("Test Case 1: largest(10, 20, 30) -> 30")
        print("Test Case 2: largest(50, 10, 50) -> 50")
        print("Explanation: Finds the largest among three numbers.")
        Large()
    elif choice==13:
        print("-----------Remove Duplicates in a List  Function------------")
        print("Test Case 1: remove_duplicates([1,2,2,3]) -> [1,2,3]")
        print("Test Case 2: remove_duplicates([5,5,5,5]) -> [5]")
        print("Explanation: Removes duplicate elements from a list using a set.")
        Dup()
    elif choice==14:
        print("-----------Fibonacci Series Function------------")
        print("Test Case 1: Input = 5 -> 0 1 1 2 3")
        print("Test Case 2: Input = 8 -> 0 1 1 2 3 5 8 13")
        print("Explanation: Prints the first n Fibonacci numbers using the recursive fib() function.")
        n= int(input("Enter a number:"))
        for i in range(n):
            print(f"Fibonacci Series For Number is:{fib(i)}",end=" ")
    else:
        print("choice correct function")
while True:
    print("\n Choose Function")
    print("1.Swap Two Numbers")
    print("2.GCD of Two Numbers")
    print("3.Reverse a Number")
    print("4.Sum of Digits")
    print("5.Count Vowels in a String")
    print("6.Count Words in a Sentence")
    print("7.Convert String to Title Case")
    print("8.Check for Palindrome")
    print("9.Check for Prime Number")
    print("10.Find Factorial of a Number")
    print("11.Convert Decimal to Binary")
    print("12.Find the Largest of Three Numbers")
    print("13.Remove Duplicates from a List")
    print("14.Fibonacci")
    choice=int(input("Enter Choice:"))
    if choice==0:
        print("Thank You")
        break
    if choice<0 or choice>14:
        print("Invaild")
        continue
    while True:
        fun(choice)
        print()
        while True:
                print("1. Continue same function")
                print("2. Back to Functions Options")
                print("3. Exit")
                Option = int(input("Enter option: "))
                if Option == 1:
                    continue
                elif Option == 2:
                    break
                elif Option == 3:
                    print("Thank You")
                    exit()
                else:
                    print("Invalid Option")
    
