import re

content = 'Jerry is a good boy'
content1 = 'Tom is cat from (34_4) Baker Street'
res = re.match('^Je.*?\s.*\s(\w*)\s.*y$',content)
print(res.group(1))

# import re
#
# content = 'Kevin has 100 ' \
#           'dollars'
# import re
#
# content = """Kevin has 100
# dollars"""
# res = re.search('Ke.*?(\d+)\s.*s',content,re.S)
# print(res.group(1))
#
# content = """Kevin has 100 dollars;
# Kevin has 100 dollars;
# Kevin has 100 dollars;
# Kevin has 100 dollars;"""
#
# content = re.sub('\d+','250',content)
# print(content)

# import re
#
# content = "Kevin has 100 dollars"
# pattern = re.compile('Ke.*?(\d+)\s.*s',re.S)
# res = re.match(pattern,content)
# print(res.group(1))


# 1
count=0
while count <10:
    count+=1
    print(count)

#4
count=1
while count<=100:
  if  count%2 == 1:
      print(count)
  count+=1

#2
count=0
total=0

while count <=100:

     total +=count  # 每循环一次，total的count都需要累计加一次
     count=count+1  #每循环一次，count都需要增加1

print(total)  #输出结果


#5
import random

trycount = 0
computer = random.randint(1, 100)
# print(computer)

while trycount < 5:
    player = int(input("Num:"))
    if player > computer:
        print('too big')
        print('Please try again')
        trycount += 1
    elif player < computer:
        print('too small')
        print('Please try again')
        trycount += 1
    else:
        print('Congratulation!')
        break
