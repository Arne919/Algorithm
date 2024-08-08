# 조합적 재귀적 정의
# r = 0 or n = r, 1
# 그외, (n, r) = (n-1, r-1) + (n-1, r)

memo = [[0] * 50 for _ in range(50)]
def comb(n, r):
    if r == 0 or n == r:
        memo[n][r] = 1
        return 1

    if memo[n][r] != 0:
        return memo[n][r]

    memo[n][r] = comb(n-1, r-1) + comb(n-1, r)
    return memo[n][r]

print(comb(5, 3))
print(comb(10, 4))
print(comb(40, 20))

for i in range(10):
    print(memo[i][:i + 1])


