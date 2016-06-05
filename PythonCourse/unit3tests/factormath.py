def factorize(number):
    def isPrime(number):
        for x in range(2,number):
            if number % x == 0:
             return False
        return True
    if number <0:
        raise ValueError
    elif type(number).__name__ != 'int' and type(number).__name__ !='long':
        raise TypeError
    x=2
    prime=[]
    while x < number+1:
        if isPrime(x) and number % x == 0:
            prime.append(x)
            number=number/x
        else:
            x=x+1
    count=0
    result=[]
    index=0
    for index in range(0,len(prime)):
        try:
            if prime[index]==prime[index+1]:
                count=count+1
            else:
                result.append((prime[index],count+1))
                count=0
        except IndexError as ie:
            result.append((prime[index],count+1))
    return result
def get_hcf(list1,list2):
    result=[(y[0],min(x[1],y[1])) for x in list1 for y in list2 if x[0]==y[0]]
    return result
def get_lcm(list1,list2):
    total=set(list1+list2)
    hcf_r=set(get_hcf(list1,list2))
    result=total-hcf_r
    result=list(result)
    result.sort()
    return result
def multiply(list1,list2):
    result=[]
    for x in list1:
        for y in list2:
            if(x[0]==y[0]):
                result.append((x[0],y[1]+x[1]))
                break
        else:
            result.append(x)
    for x in list2:
        for y in result:
            if(x[0]==y[0]):
                break
        else:
            result.append(x)
    result.sort()
    return result