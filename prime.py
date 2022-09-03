#Assignment 1 : Using for loop please print all the prime numbers between 1-200 using FOR LOOP AND RANGE function
for number in range(1,200):
    if number>1:
        for i in range(2,number):
            if (number%i)==0:
                break
        else:
            print(number)
