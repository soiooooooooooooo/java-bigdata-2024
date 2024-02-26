# file: p30_standardLib.py
# desc: 표준 라이브러리(빌트인) 학습

import datetime

print(datetime.date(2024,2,26)) # 현재의 OS에 맞춰서 날짜형으로 변경

curr = datetime.datetime.now() # 현재의 년월일시분초를 알려줌
print(curr)