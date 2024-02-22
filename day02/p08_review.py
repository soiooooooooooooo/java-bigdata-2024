# file: p08_review/py
# desc: 리뷰

#Q2
a = 13
print('a는 ', end='')
if  a % 2 ==0:
   print('짝수')
else:
   print('홀수')   

#Q3
   pin =  "881120-1068234"
   yyyymmdd = pin[:6]
   num = pin[7:]
   print(yyyymmdd)
   print(num)

#Q5
   a = "a:b:c:d"
   b = a.replace(":","#")
   print(b)

#Q6
   a = [ 1,3,5,4,2]
   a.sort()
   a.reverse()
   print(a)

#Q10
a = {'A':90,'B':80,'c':70}
result = a.pop('B')
print(a)
print(result)

