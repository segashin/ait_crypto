# python3

import sys
import textbookRSA

####Function to calculate Poincare's approximation####
def extEucList(a, b):
    '''calculates continued fractions'''
    div = a // b
    rem = a % b
    res = [div]
    if rem == 0:
        return res
    return res + extEucList(b, rem)

def eucToRational(frac):
    '''calculates rational for the list of fractions
    in the form of (numerator, denumerator)'''
    if len(frac) == 0:
        return (0,1)
    elif len(frac) ==1:
        return (frac[0], 1)
    else:
        rem = frac[1:len(frac)]
        (num, szam) = eucToRational(rem)
        return (frac[0] * num + szam, num)
        
def getConvergents(frac):
    '''calculates convergents for a list of fractions'''
    con = []
    for i in range(len(frac)):
        con.append(eucToRational(frac[0:i]))
    return con
 
####General Arithmetics####
def bitlength(x):
    '''
    Calculates the bitlength of x
    '''
    assert x >= 0
    n = 0
    while x > 0:
        n = n+1
        x = x>>1
    return n
    
def isqrt(n):
    '''
    Calculates the integer square root
    for arbitrary large nonnegative integers
    '''
    if n < 0:
        raise ValueError('square root not defined for negative numbers')
    
    if n == 0:
        return 0
    a, b = divmod(bitlength(n), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y

def is_perfect_square(n):
    '''
    If n is a perfect square it returns sqrt(n),   
    otherwise returns -1
    '''
    h = n & 0xF;    
    if h > 9:
        return -1 
        
    if ( h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8 ):
        t = isqrt(n)
        if t*t == n:
            return t
        else:
            return -1   
    return -1

####Break RSA####  
with open("flag.crypt", "r") as f:
    lines = [line.strip() for line in f]
    exp = int(lines[0])
    mod = int(lines[1])
    flg = int(lines[2])
    
    sys.setrecursionlimit(10000)
    frac = extEucList(exp, mod)
    
    # Look for convergents in frac that satisfy the Wiener conditions
    for (u,v) in getConvergents(frac):
        # Fill your code here ...
        # u: numerator
        # v: denominator
        if v%2==1 and v!=0 and u!=0:
            if (exp*v-1)%u==0:
                try:
                    # If valid candidate found decrypt message
                    rsa = textbookRSA.TextbookRSA({'e':exp, 'd':v, 'n':mod})
                    solution = rsa.decrypt(flg)
                    print(solution.decode('utf-8'))
                except:
                    pass