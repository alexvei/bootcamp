primes = []

def prime_check(num):
    global primes
    for i in range(2,num):
        if not num % i :
            return
        
    primes.append(num)
    

for i in range(2,21):
    prime_check(i)

print(primes)