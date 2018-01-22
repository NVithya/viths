prime_num =''
for num in xrange(2,2000000):
    prime = True
    for i in xrange(2,num):
        if (num%i == 0):
            prime = False
            break 	
    if prime:
    	prime_num += str(num) + ','
c = prime_num.strip(',').split(",")
d = [int(x) for x in c]
print sum(d)










