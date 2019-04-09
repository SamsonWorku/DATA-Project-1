
num = int(input("ENTER YOUR NUMBER:"))
print ('Numbers less than ', num, 'that are prime or not prime:')

primes = []

for cur in range(2,num+1):  
    prime=True
    for den in primes: 
        if not (cur % den):
            print (cur,'IS NOT A PRIME NUMBER')
            prime=False  
            break
    if prime==True:  
        print (cur, 'IS A PRIME NUMBER')
        primes.append(cur) 
print('and primes as a list ',primes)

