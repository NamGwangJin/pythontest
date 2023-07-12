# # tuple (튜플)
# t1 = 1,2,3,4,5
# t2 = 'hello', 3.14, -1, True
# print(t1)
# print(t2)
# for i in t1:
#     print(i)

# # set (집합)
# s1 = {1,2,3,4,5,6}
# s2 = {5,6,7,8,9,10}
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# for i in s1:
#     print(i)

# # dictionary (딕셔너리)
# d1 = { 'name':'John', 'age':23, 'city':'goyang', 'birthday':'20030617', 20:'20"s' }
# for x in d1:
#     print(x, d1[x])
# print('-'*30)
# for k, v in d1.items():
#     print(k, v)
# d2 = { 'list':[1,2,3,4,5], 'tuple':(1,2,3,4,5), 'set':{1,2,3,4,5}, 'dict':{'name':'ilsan', 'city':'Cheonan'}}
# print(f"{d2['list']} \n{d2['tuple']} \n{d2['set']} \n{d2['dict']['name']}")

# d3 = [ {'name':'john', 'age':23}, {'name':'jane', 'age':21}, {'name':'jason', 'age':35} ]
# for x in d3:
#     print(x['name'],x['age'])