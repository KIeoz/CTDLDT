import time
def fib_dp(n):
    if n <= 1:
        return n

    f = [0] * (n + 1)
    f[0], f[1] = 0, 1

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]
n = 10
for i in range(n):
    print(f"F({i}) = {fib_dp(i)}")
start = time.time()
result = fib_dp(n)        
end = time.time()         
print(f"Thời gian chạy: {end - start:.6f} giây")
