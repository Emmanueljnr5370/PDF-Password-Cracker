import os
a = os.listdir('C:/Users/User/Desktop/Sci movies')
b = os.listdir('C:/Users/User/Desktop/Action movies')
x = set(a)
y = set(b)
z = x.intersection(y)
for x in a:
    if x in z:
        print(os.remove(f'C:/Users/User/Desktop/Sci movies/{x}'))
else:
    print('task completed!')        