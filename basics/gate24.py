# #problem 38
# def count(child_dict,i):
#     if i not in child_dict.keys():
#         return 1
#     ans=1
#     for j in child_dict[i]:
#         ans+=count(child_dict,j)
#     return ans

# child_dict=dict()
# child_dict[0]=[1,2
#                ]
# child_dict[1]=[3,4,5]
# child_dict[2]=[6,7,8]
# print(count(child_dict,0))
###########################################################
#problem 41
# def fun(d,s1,s2):
#     if s1<s2:
#         d[s1],d[s2]=d[s2],d[s1]
#         fun(d,s1+1,s2-1)
#
# a=[1,2,3,4,5]
# fun(a,2,2)
# print(a)
# fun(a,1,2)
# print(a)

###############################################
#problem
# d=list(range(5))
# print(d)
# s1,s2=1,2
# d[s1],d[s2]=d[s2],d[s1]#simultaneous assigment
# print(d)
#
#################################################

