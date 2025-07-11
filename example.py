
def to_base(num,base):
    if num==0:
        return "0"
    
    digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result=""

    while num>0:
        result= digits[num%base] +result
        num//=base
    
    return result

print(to_base(100,3))
print(int('100',2))