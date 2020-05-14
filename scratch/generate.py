import random
base = 'randomStr'
variables = [{'basePwrd': base}, 'site', 'email', 'siteCreationYear', 'isLeisure', 'isWork']
# basic world keyring:
print('basic world keyring:')
random.shuffle(variables)
print(variables)

# level 1 world keyring: dynamic ordering function
print('level 1 world keyring: dynamic ordering function')
def sort(list):
    return list.sort()
def reverseSort(list):
    return list.sort(reverse=True)
dofList = [sort, reverseSort]
dof = random.choice(dofList)
print(dof)

# level 1 world keyring alt: mapping function
print('level 1 world keyring alt: mapping function')
def capitalize(str):
    return str.capitalize()
def leftShift(str):
    strList = list(str)
    strList.append(strList.pop(0))
    return ''.join(strList)

mapList = [capitalize, leftShift]
map = random.choice(mapList)
print(map)
