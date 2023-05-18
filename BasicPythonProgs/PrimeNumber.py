from math import sqrt


def isPrime(n):
    if n>1:
        # for i in range(2,int(n/2)+1):
        for i in range(2,int(sqrt(n))+1):   #Instead of checking till n, we can check till √n because a larger factor of n must be a multiple of a smaller factor that has been already checked
            if n%i==0:
                print(n,"is not a prime number")
                break
        else:
            print(n,"is a prime number")

print(isPrime(11))
isPrime(9)






Number = 1

while (Number <= 100):
    count = 0
    i = 2

    while (i <= Number // 2):
        if (Number % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and Number != 1):
        print(" %d" % Number, end='  ')
    Number = Number + 1


