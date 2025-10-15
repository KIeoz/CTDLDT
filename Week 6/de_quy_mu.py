def luy_thua(a, n):
    if n < 0:
        raise ValueError("Nhập số mũ không âm (n ≥ 0)")
    if n == 0:                
        return 1
    else:
        return a * luy_thua(a, n - 1)
print(luy_thua(1000000000000000000000000000000000000000000, 100))  
