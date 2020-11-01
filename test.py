# num=[]
# i=2
# for i in range(2,100):
#    j=2
#    for j in range(2,i):
#       if(i%j==0):
#          break
#    else:
#       num.append(i)
# print()

'''
When a ball falls freely from 100 meters,
it jumps back to half of its original height every time it lands;
if it falls again, how many meters does it pass in the 10th landing?
How high is the 10th rebound?
'''

S = 100.0
H = S/2

for n in range(2,11):
   S += 2*H # + - * /   a += 1 -> a = a + 1
   H /= 2 #H/=2 ~ H = H /2

print('Total of road is ' + str(S))
print('The 10th is '+ str(H))
