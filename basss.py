q = [['Dog','Tejas',5],[1,2,3,4]]
print(q[0][1])

print('The ' + str(q[0][-2]) + ' loves ' + str(q[0][0]) + ' very much. ')


q[0][0] = 'cat'
print(q[0][0:2])

a = (list(zip('123456')))

print(list(range(0,4)))
print(a)
z = ['a','b','for']
for i in range(len(z)):
    print('Index'+str(i)+'in variable'+z[i])
s = [1,2,3]
print(z.index('for'))
z.append('rat')
# z.insert(1,s)
z.extend(s)
print(z)