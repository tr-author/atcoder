A, B, N = map(int, input().split())

print(int(A * min(B - 1, N) / B) - A * int(min(B - 1, N) / B))
