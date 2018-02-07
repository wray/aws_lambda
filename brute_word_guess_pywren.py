import pywren
import time
import itertools

chars = "abcdefghijklmnopqrstuvwxyziABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890^?!?$%&/()=?`'+#*'~';:_,.-<>|"

def brute_force_chars(pin):
    # Generating a list of all possible permutations of the charset above
    for guess in list(itertools.product(list(chars),repeat=len(pin))):
        if pin == len(pin)*'%c' % (guess):
            return guess        

def brute_force_split(pin,n):
    split = len(pin)//n

    l = [ pin[i*n:(i+1)*n] for i in range(split) ]

    print('Executing a lambda for each item in - ' + str(l))
              
    pwex = pywren.default_executor()
    # Executing async in parallel
    futures = pwex.map(brute_force_chars,l)
    return pywren.get_all_results(futures)

    
if __name__ == '__main__':
    """ This will beat locally with a pword size of 1009 """
    print('Provide a pword whose length is divisible by 2 to be brute-forced guessed')
    pin = input()
    t1 = time.time()
    guess = brute_force_split(pin,2)
    print('Found: ' + str(guess))
    t2 = time.time()
    print('Elapsed time was ' + str(t2-t1))
