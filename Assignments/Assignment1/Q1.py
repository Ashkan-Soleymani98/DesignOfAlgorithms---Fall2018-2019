prime = pow(10, 9) + 7

n = int(input())

facto = [1]
for i in range(1, n + 1):
    facto.append((facto[-1] * i) % prime)

# print(facto)

nums = map(int, input().split())

less = [(i - 1) for i in range(n + 1)]

sum = 1
for i, a in enumerate(nums):
    sum += (less[a] * facto[n - i - 1]) % prime
    for j in range(a + 1, n + 1):
        less[j] -= 1

print(sum % prime)