# file: p14_review/py
# desc: 리뷰

#01
a = 'Life is too short, you need python'

if 'wife' in a : print('wife')
elif'python' in a and 'you' not in a: print('python')
elif'shirt' not in a: print('shirt')
elif 'need' in a: print('need')
else: print("none")
#shirt 출력

#02
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
       result += i
    i += 1

print(result) #166833 출력

#03
i = 0
while True:
    i += 1
    if i > 5: break
    print('*' * i)

#04
for i in range(1,101):
    print(i)

    
#05
A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for score in A:
    total += score # A학급의 점수를 모두 더한다
average = total / len(A) # 평균을 구하기 위해 총 점수를 총 학생수로 나눈다
print(average) #평균 79.0이 출력된다

#06
numbers =[1,2,3,4,5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n * 2)

numbers = [1,2,3,4,5]
result = [n*2 for n in numbers if n%2 == 1]
print(result) #[2,6,10] 출력