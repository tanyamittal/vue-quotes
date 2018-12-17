import time
def matrix_product(p):
    length = len(p)
    m= [ (-1)*length for _ in range(length)]
    s= [[-1] * length for - in range(length)]
    matrix_product_helper(p,1,length-1,m,s)
    return m,s
def matrix_product
