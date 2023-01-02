const1 = int(input("Enter your lower constraint: "))
const2 = int(input("Enter your lower constraint: "))
primes=[]
emirPrimes = []
rev =0
if const1 == 0:
    const1 == 1
for i in range(const1, const2+1):
    factors = []
    for w in range (1, i+1):
        if (i % w) == 0:
            factors.append(w)
    if len(factors) == 2:
        primes.append(i)

primes=[*set(primes)]
primes.sort()


for i in range(0, len(primes)):
    factors = []
    if primes[i] > 10:
        rev_primes = str((primes[i]))[::-1]
        if int(rev_primes) != primes[i]:
            for a in range(1, int(rev_primes)+1):
                if (int(rev_primes)%a) == 0:
                    factors.append(a)
    if len(factors) == 2:
        emirPrimes.append(primes[i])
emirPrimes = [*set(emirPrimes)]
emirPrimes.sort()


print("There are " + str(len(emirPrimes)) + " emirPrimes between " + str(const1) + " and " + str(const2))
print("Those emirPrimes are: " + str(emirPrimes))