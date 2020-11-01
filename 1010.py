# cars = ['audi','bmw','subaru','toyota']
#
# for car in cars:
#     if car != 'bmw':
#         print(car.upper())#方法upper让所有字母大写
#     else:
#         print(car.title())

    #如果临时变量取到了 bmw，则把所有英文大写。如果没有，则首字母大写

#Bool 布尔值
#True / False

# == 疑问句？  发问： 是xxx吗？
# = 陈述句。 定义变量：a里面是1
# != 否定疑问  发问：不是xxx吗？

# age = 11
#
# if age > 12:
#     print('Pass')
# else:
#     print('You cannot pass')
# #    >   <    >=    <=

#检查多个条件

# age_1 = 6
# age_2 = 30
#
# # if age_1 > 18 or age_2 > 18:
# #     print('Pass')
# # or 或 只要所有连接的条件中有一个满足，则结果为True。如果所有的都为False，结果才会是False
#
# if age_1 > 18 and age_2 > 18:
#     print('Pass')
# else:
#     print('You Cannot pass')
# #and 与  必须所有条件都为True，结果才为True。如果有任何一个为False，结果就是False

# 检查特定值是否包含在列表中：

# requested_toppings=['mushrooms','onions','pineapple']
#
# b = 'mushrooms' in requested_toppings
# b2 = 'cheese' not in requested_toppings
#
# print(b)
# print(b2)
#
# # in 可以检查指定字符串是否出现在列表之中  not in 是检查是否没出现在其中

# if结构

'''
if conditional_test:
    do code1
else： #conditional_test = False
    do code2
'''

# 4岁以下免费
# 4-18岁收半价
# 18岁以上全价

# age = 12
#
# if age < 4:
#     print('Free')
# elif age < 18:     #elif 是 else+if 的缩写，如果有多个条件，我们可以使用无限个elif去写
#     print('Half')
# else:               #else 只会出现在整个if结构的末尾，后面不跟条件，因为它概括了剩下所有的情况
#     print('Full')

# age = int(input())
# '''
# 设置变量 age 的值，再编写一个 if-elif-else 结构，根据 age 的值判断处于人生的哪个阶段。
#  如果一个人的年龄小于 2岁，就打印一条消息，指出他是婴儿infant。
#  如果一个人的年龄为 2（含）～4岁，就打印一条消息，指出他正蹒跚学步baby。
#  如果一个人的年龄为 4（含）～13岁，就打印一条消息，指出他是儿童child。
#  如果一个人的年龄为 13（含）～20岁，就打印一条消息，指出他是青少年young。
#  如果一个人的年龄为 20（含）～65岁，就打印一条消息，指出他是成年人adult。
#  如果一个人的年龄超过 65（含）岁，就打印一条消息，指出他是老年人old。
# '''
#
# requested_toppings =['mushrooms','green peppers','extra cheese']
#
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print('Sorry, we are out of green peppers.')
#     else:
#         print("Adding " + requested_topping + '.')

# requested_toppings =[]
#
# if requested_toppings:#if中直接填上列表名，如果列表为空，则返回False，列表不为空，返回True.
#     print('Making your pizza!')
# else:
#     print('Empty Pizza')

#所有的 空 字符串、 列表 、 字典 都是False.

available_toppings = ['mushrooms','pineapple','onions','green peppers','cheese']

requested_toppings =['mushrooms','french fries','cheese']

for requested_topping in requested_toppings:#这里的in是for循环的必要语句
    if requested_topping in available_toppings:#这里的in是发问，要求的东西，在不在提供的列表里
        print("Adding " + requested_topping + '.')
    else:
        print("Sorry,we don't have "+ requested_topping +'.')

#Today is 1101