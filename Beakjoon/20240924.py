#백준 11006

# def solution(case, num1, num2):
#     result = []
#     for i in range(case):
#         result.append([(num2 * 2)- num1, num2-num1])
#         return result

for _ in range(int(input())):
    num1, num2 = map(int, input().split())
    u = (num2 * 2) - num1
    t = num2 - u
    print(u, t)
