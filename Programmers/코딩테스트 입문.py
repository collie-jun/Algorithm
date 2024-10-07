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

#개미 군단
def solution(hp):
    big = hp // 5
    mid = (hp % 5) // 3
    small = ((hp % 5) % 3)
    return big + mid + small

#숨어있는 숫자의 덧셈
def solution(my_string):
    return sum (int(char) for char in my_string if char.isdigit())
#isdigit 각 문자가 숫자인지 확인 char.isidigit()은 해당 문자가 숫자인지 여부를 확인

#대문자와 소문자
def solution(my_string):
     return my_string.swapcase()
#swapcase 문자열 내의 모든 대문자를 소문자로, 소문자를 대문잘 변환

#가장 큰 수 찾기
def solution(array):
    max_value = max(array)
    max_index = array.index(max.value)
    return [max_value, max_index]


#n의 배수 고르기
def solution(n, numlist):
    return [ char for char in numlist if char % n ==0  ]

#새균 증식
def solution(n,t):
    return n << t
    # 비프시프트(<<,>>)
    # 왼쪽 시프트 연산자(<<):2를 곱한 것과 같은 효과 => n << m : n * 2의 m승
    # 오른쪽 시프트 연산자(>>):2로 나눈 것과 같은 효과 => n >> m : n/2의 m승

#문자열 뒤집기
def solution(my_string):
    return ''.join(reversed(my_string))
    #join() 문자열 메서드, 각 요소를 하나의 문자열로 합칠 때 사용
    #''은 구분자 빈 문자열을 사용하면 요소들 사이에 아무것도 넣지 않고 합침

#문자열 뒤집기
def solution(my_string):
    return my_string[::-1]
    #슬라이싱 [start:stop:step] 을 명시하여 부분을 추출
    #mylist[:] 전체 출력
    #[start:]는 시작 index 부터 끝까지 추출
    #[:end]는 처음부터 end 전까지 추출
    #[start:stop:step] step는 몇 칸씩 던너 뛰는지 설정
    #mylist[::2] 2칸씩 건너뛰기
    #mylist[::-1] 역순 출력

#짝수 홀수 개수
def solution(num_list):
    odd_num, even_num = 0,0
    for num in num_list:
        if num % 2 == 0:
            even_num += 1
        else:
            odd_num += 1
    return [even_num, odd_num]


#특정 문자 제거하기
def solution(my_string, letter):
    return my_string.replace(letter,'')
    #문자열.replace(바꿀 문자열, 새로운 문자열)

#가위 바위 보
def solution(rsp):
   return rsp.translate(str.maketrans('025', '502'))

def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)

#직각삼각형 출력하기
n = int(input())
for i in range (1,n+1):
    print("*"*i, end= "\n")

#점의 위치 구하기
def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0]>0][dot[1]>0]
    #python에서 불리언 값을 숫자처럼 사용 가능 true =1 , false = 0으로 사용 가능
    #리스트 quad 좌표가 어느 사분면에 있는지를 나타냄, 각 항목은 사분면의 번호
    #튜플은 여러 개의 값을 하나로 묶을 수 있는 자료형, 리스트와 비슷하지만 튜플은 변경할 수 없는 자료형

#피자 나눠 먹기
def solution(slice,n):
    if n % slice == 0:
        return n // slice
    else : 
        return n // slice +1
    
#주사위의 개수
def solution(box,n):
    return int((box[0]//n)*(box[1]//n)*(box[2]//n))

#약수 구하기
def solution(n):
    answer = []
    for i in range (1,n+1):
        if n % i == 0:
            answer.append(i)
        return answer
    #append() 함수는 리스트의 메서드로, 리스트의 끝에 새로운 요소를 추가할 때 사용
    
def solution(n):
    return[i for i in range(1,n+1)if n%i ==0 ]

#인덱스 바꾸기
def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1],s[num2] = s[num2],s[num1]
    return ''.join(s)


#최댓값 만들기
def solution(numbers):
    numbers.sort(reverse = True)
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])
    #list.sort(reverse=False) / list.sort(reverse=True)
    #오름차순 / 내림차순


#순서쌍의 개수
def solution(n):
    a = 0
    for i in range (1, n+1):
        if n % i == 0:
            a += 1
    return a

#편지
def solution(message):
   return 2 * len(message) 

#양꼬치
def solution(n,k):
    a = n // 10
    return (n*12000)+((k-a)*2000)

#배열 뒤집기
def solution(num_list):
    return num_list[::-1]

#배열의 유사도
def solution(s1, s2):
    return len(set(s1)&set(s2))
    #set()함수 => 리스트나 문자열을 집합으로 변환
    #&교집합을 구하는 방식

#자릿수 더하기
def solution(n):
    return sum([int(i) for i in str(n)])

#최댓값 만들기
def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0]*numbers[1]

#삼각형의 완성 조건
def solution(sides):
    sides.sort(reverse=True)
    if sides[0] < sides[1] + sides[2]:
        return 1
    else:
        return 2
    

#문자열 안에 문자열
def solution(str1, str2):
    if str2 in str1:
        return 1
    else:
        return 2
    
# 배열 원소의 길이
def solution(strlist):
    return [len(i) for i in strlist]
    #따로 공백으로 구별해주지 않아도 되는 문제

#제곱수 판별하기 
def solution(n):
    return 1 if (n ** 0.5)% 1 ==0 else 2
    #n**0.5는 n의 제곱근을 구하는 연산

#모음 제거
def solution(my_string):
    return ''.join([i for i in my_string if not (i in 'aeiou')])

#문자 반복 출력하기
def solution(my_string, n):
     return list(map(lambda n: n * 2, my_string))