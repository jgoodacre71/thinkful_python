import sys

try:
    fizzbuzz_upper = int(sys.argv[1])
except:
    fizzbuzz_upper = 0

if fizzbuzz_upper <1:
    user_upper = raw_input("Please enter an upper limit for fizzbuzz > 0\n")
    try:
        fizzbuzz_upper = int(user_upper)
    except:
        print "Invalid value for upper limit"
        
if fizzbuzz_upper >= 1:
    print "Fizz Buzz counting to {}".format(fizzbuzz_upper)
    fizzbuzz = False

    for i in range(1,fizzbuzz_upper):
        fizzbuzz = False
        if i%3==0:
            print "Fizz"
            fizzbuzz = True
        if i%5==0:
            print "Buzz"
            fizzbuzz = True
        if not fizzbuzz:
            print i
