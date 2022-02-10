A = [0] * 1000
top = 0  # уровень заполненостиx
x = int(input())
while x != 0:
    A[top] = x
    top += 1
    x = int(input())

for k in range(top-1, -1 , -1):
    print(A[k])