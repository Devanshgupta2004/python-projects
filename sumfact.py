
def fact_sum(*n):
    import math    
    sum1=0
    
    def fact(x):
        factor=math.factorial(x)
        return factor

    for i in n:
        sum1=sum1+fact(i)    
            
            
    return sum1
                

a=fact_sum(0,1,2,3,4,5,6)
print(a)


    