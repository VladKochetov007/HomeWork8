from math import gcd

def gen(max_n: int = 5):
    # 1/5 1/4 2/5 1/3 ?
    for a in range(1, max_n+1):
        min_num = float('inf')
        min_pair = None
        for b in range(1, max_n+1):
            if gcd(a, b) == 1:
                min_num = min(min_num, a/b)
                min_pair = (a, b)
        yield min_pair

for a, b in gen(10):
    print(f"{a}/{b}")
