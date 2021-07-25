def is_even():
    num = int(input("Enter your number: " ))
    if num%2 == 0:
        print(f'{num} is Even')
    else:
        print(f'{num} is Odd')
        
def is_palidrome():
    st = input("Enter your String: ")
    if st == st[::-1]:
        print(f'{st} is palindrome.')
    else:
        print(f'{st} is not a palindrome.')
    
def is_prime():
    num=int(input("enter your number: "))
    if num>1:
       for i in range(2,int(num/2)+1):
           if(num%i)==0:
              print(f'{num} is not prime')
              break
       else:
        print(f'{num} is a prime: ')
    else:
        print(f'{num} is not a prime: ')
        
def is_pos_neg():
    num=int(input("enter your number: "))
    if(num>0):
        print(f'{num} is positive: ')
    else:
        print(f'{num} is negative: ')
    
    
def greet_user():
    print("\n Hello user!!\n")
    print("*** Menu ***")
    options = ["check Odd Even","check palindrome","check Prime number","check Positive or negative"]
    for i in range(len(options)):
        print(f'{i+1}.{options[i]}')
    ch = int(input("\n Enter your choice: "))
    if ch == 1:
        is_even()
    elif ch == 2:
        is_palidrome()
    elif ch == 3:
        is_prime()
    elif ch == 4:
        is_pos_neg()
    else:
        print("\n Invalid Choice.\n Please try again")
greet_user()
