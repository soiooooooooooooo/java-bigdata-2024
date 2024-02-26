# file: p31_review.py
# desc: 리뷰
#1 2 6 7  11 타임모듈말고 데이트ㅏ타임써서

#01
class UpgradeCalculator(Calculator):
    def minus(self,val):
        self.value -= val
#02
class MaxLimitCalculator(Calculator):
    def add(self,val):
        self.value += val
        if self.value > 100:
            self.value = 100
#06
>>> List(map(lambda x:x*3,[1,2,3,4]))
#07
>>> a = [-8,2,7,5,-3,5,0,1]
>>> max(a) + min(a)

#11