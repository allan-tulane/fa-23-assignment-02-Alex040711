"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y



def subquadratic_multiply(x, y):
    # Convert to BinaryNumber if they aren't already
    if not isinstance(x, BinaryNumber):
        x = BinaryNumber(x)
    if not isinstance(y, BinaryNumber):
        y = BinaryNumber(y)
    
    # Get the binary vectors of x and y and pad them if necessary
    x_vec, y_vec = pad(x.binary_vec, y.binary_vec)
    
    # Base case: If they are single bits, just multiply
    if len(x_vec) == 1 or len(y_vec) == 1:
        return binary2int([str(int(x_vec[0]) * int(y_vec[0]))])

    # Split the numbers
    a, b = split_number(x_vec)
    c, d = split_number(y_vec)
    
    # Recursive calls
    ac = subquadratic_multiply(a, c)
    bd = subquadratic_multiply(b, d)
    ab_cd = subquadratic_multiply(binary2int(a.binary_vec + b.binary_vec), binary2int(c.binary_vec + d.binary_vec))
    
    # Compute (a+b)(c+d) - ac - bd
    middle_term = binary2int([str(int(bit) - ac.binary_vec[i] - bd.binary_vec[i]) for i, bit in enumerate(ab_cd.binary_vec)])
    
    # Combine results using the formula
    result = binary2int([str(bit) for bit in ac.binary_vec + ['0'] * (len(x_vec))] + [str(bit) for bit in middle_term.binary_vec + ['0'] * (len(x_vec) // 2)] + bd.binary_vec)
    
    return result



def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000

    
    

