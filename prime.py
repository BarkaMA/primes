from math import sqrt
print (' THE ARABIEN \n ### This program is used to find prime numbers  ###\n\n ')

primes = list()
last_digits_of_primes = ['1', '3', '7', '9']
choosing_method = input('select which method to use :\n    1) specify interval \n    \
2) specify the amount of primes to look for \n >>>')
# process by specifying interval
if choosing_method == 1:
    minimum_interval = input('the script will start digging for primes from :\n >>>')
    maximum_interval = input('to : \n >>>')
    all_ns = xrange(minimum_interval, maximum_interval + 1)
    for i in all_ns:
        last = list(str(i))
        if i > 10 and not(last[-1] in last_digits_of_primes):
            pass
        elif 2 <= i <= 100:
            c = 0
            for d in xrange(1, i):
                rem = i % d
                if rem is not 0:
                    c += 1
                if c == i - 2:
                    primes.append(i)
        elif i > 100:
            b = int(sqrt(i))
            c = 0
            for d in xrange(1, b + 1):
                rem = i % d
                if rem is not 0:
                    c += 1
                if c == b-1:
                    primes.append(i)
    print ('done ..\n\n ' + str(len(set(primes))) + ' prime numbers found\n listing them :\n ')
    print(primes)
# process by specifying amount
elif choosing_method == 2:
    minimum_interval = input('the script will look for primes starting from :\n >>>')
    amount = input('specify the amount of primes you are looking for\n >>>')
    limit = 1000000000
    all_ns = xrange(minimum_interval, limit)
    for i in all_ns:
        last = list(str(i))
        if i > 10 and not (last[-1] in last_digits_of_primes):
            pass
        elif 2 <= i <= 100:
            c = 0
            for d in range(1, i):
                rem = i % d
                if rem is not 0:
                    c += 1
                if c == i - 2:
                    primes.append(i)
        elif i > 100:
            b = int(sqrt(i))
            c = 0
            for d in range(1, b + 1):
                rem = i % d
                if rem is not 0:
                    c += 1
                if c == b - 1:
                    primes.append(i)
        if len(primes) == amount:
            break
    print ('done ..\n\n ' + str(len(set(primes))) + ' prime numbers found\n listing them :\n ')
    print(primes)
# process input warnings
else:
    print('\nERROR: <' + str(choosing_method) + '> is not an option, please rerun and stick to the menu')