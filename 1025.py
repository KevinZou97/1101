# names = ['kevin','michael','raven']
# print(names)
#
# #1
# names[2]='evan' #改
# print(names)
#
# #2
# names.insert(0,'jason')
# names.insert(2,'jack')
# names.append('kris')
# print(names)
#
# #3
# del names[1]
# names.pop(2)
# names.remove('kris')
# print(names)

# cars =['bmw','audi','toyota','subaru']
# # #
# # # # cars.sort(reverse=True) #排列
# # #
# # # # print(sorted(cars))  #临时排列
# # #
# # # print(cars)
# # #
# # # cars.reverse() #倒序
# # #
# # # print(cars)
# # l = len(cars) #len长度，列表中元素的个数
# # print(len(cars))

# nums = [3,5,7,9]
#
# print(max(nums))
# print(min(nums))

# names = ['kevin','miachael','raven']
#
# for name in names:  # for loop  ->  for 临时变量 in 列表名 :
#     print(name.title()+", good evening")
#     print(name + ', have a nice day')
#
# print(names)

# players = ['charles','martina','michael','florence','eli']
#
# print("Here are the first three players on my team:")
# for player in players[:3]:
#     print(player.title())

# my_foods = ['pizza','carrot cake','kfc']
# friend_foods = my_foods#复制列表
#
# my_foods.append('cannoli')
# friend_foods.append('ice cream')
#
# print("My favorite foods are:")
# print(my_foods)
#
# print("\nMy friends' favorite foods are：")#制表符 \n 换行符
# print(friend_foods)

#Tuple
dimensions = (200,30,50)
print(dimensions[0])
print(dimensions[1])

dimensions = (200,30,22)#完全覆盖
for dimension in dimensions:  #遍历元组
    print(dimension)
print(dimensions)