
def sort(list):
    return list.sort()
def reverseSort(list):
    return list.sort(reverse=True)
def capitalize(str):
    return str.capitalize()
def leftShift(str):
    strList = list(str)
    strList.append(strList.pop(0))
    return ''.join(strList)
def doNothing(thing):
    return thing

functions = {'sort': sort, 'reverseSort': reverseSort, 'capitalize': capitalize, 'leftShift': leftShift, '': doNothing}


mapStr = input('mapping function:\n')
dofStr = input('dynamic ordering function:\n')
# basePwrd site email siteCreationYear isLeisure isWork
# basePwrd armorgames example@gmail.com 2005 t f
worldConstants = input('worldConstants: \n').split(' ')
# print(worldConstants)
ordered = functions[dofStr](worldConstants)
mapped = [ functions[mapStr](constant) for constant in worldConstants ]
print("password:")
print(''.join(mapped))
