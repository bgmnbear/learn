'''
标识、相等性、别名
'''

lazybear = {'name': 'ehco', 'age': '21'}
whister = lazybear

print(whister == lazybear)
print(whister is lazybear)
print(id(whister), id(lazybear))

fake_lazybear = {'name': 'ehco', 'age': '21'}
print(fake_lazybear == lazybear)
print(fake_lazybear is lazybear)
print(id(fake_lazybear), id(lazybear))
