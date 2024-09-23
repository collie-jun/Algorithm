# 두 수의 합
def solution(num1, num2):
    return num1 + num2

#두 수의 차
def solution(num1, num2):
    return num1 - num2

#두 수의 곱
def solution(num1, num2):
    return num1 * num2

#몫 구하기
def solution(num1, num2):
    return num1 // num2

#두 수의 나눗셈
def solution(num1, num2):
    return int((num1 / num2) *1000)

#숫자 비교하기
def solution(num1, num2):
    if num1 == num2:
        return 1
    else:
        return -1
    
#분수의 덧셈
import math

def solution(numer1, denom1, numer2, denom2):
    # 두 분수를 더한 후의 분자와 분모 계산
    numerator = numer1 * denom2 + numer2 * denom1  # 분자 계산
    denominator = denom1 * denom2  # 분모 계산
    
    # 분자와 분모의 최대공약수를 구함
    gcd_value = math.gcd(numerator, denominator)
    
    # 기약 분수로 만들기 위해 분자와 분모를 최대공약수로 나눔
    return [numerator // gcd_value, denominator // gcd_value]

#배열 두배 만들기
def solution(numbers):
    return list(map(lambda x: x * 2, numbers))

#나이 출력
def solution(num):
    return 2022-num+1 

#나머지 구하기 
def solution(num1, num2):
    return num1 % num2

#각도기
def solution(angle):
    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    elif angle == 180:
        return 4


#짝수의 합
def solution(n):
    total = 0
    for i in range(2, n+1, 2): #2부터 n까지 2씩 증가
        total += i
    return total

#배열의 평균값
def solution(numbers):
    return sum(numbers) / len(numbers)

#중복된 숫자 개수
def solution(array, n):
    return array.count(n)

#머쓱이보다 키 큰 사람
def solution(array, height):
    count = 0
    for h in array:
        if h > height:
            count += 1
    return count

#배열 자르기
def solution(numbers, num1, num2):
    return numbers[num1:num2+1] 
    # numbers 리스트에서 num1번째 인덱스부터 num2번째 인덱스까지 자른 부분을 반환
    # 슬라이싱 구문 numbers[num1:num2+1]에서 num1부터 num2까지 포함하기 위해 num2+1을 사용

#중앙값 구하기
def solution(array):
    return sorted(array)[len(array) //2]
    # sorted(array) 입력 배열을 오름차순으로 정렬된 배열로 변환
    # len(array)//2 중앙 인덱스를 계산
    #[] 중앙 인덱스로 중앙값을 추출

#짝수는 싫어요
def solution(n):
    return [ i for i in range(1, n+1) if i % 2 == 1 ]
    # [] 리스트를 출력
    # 1 부터 n 까지의 범위를 순회
    # i 가 홀수일 때만 리스트에 포함

#피자 나눠 먹기
def solution(n):
    return (n+6) // 7 

#옷가게 할인 받기
def solution(price):
    if(500000<=price):
        return int(price*0.8)
    elif(300000<=price<500000):
        return int(price*0.9)
    elif(100000<=price<300000):
        return int(price*0.95)
    else:
        return int(price)
    #소수점 아래는 버리고 정수로 반환하라는 조건이 있었음 주의
    
#아이스 아메리카노
def solution(money):
    return [(money // 5500), (money % 5500)]