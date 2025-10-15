def tong(n):
    if n == 1:
        return 1
    else: 
        return n + tong(n-1)
print(tong(999))  

