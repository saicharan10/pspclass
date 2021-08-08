#Looping over a backwards.
'''
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)-1, -1, -1):
    print(colors[i])
'''

colors = ['red', 'green', 'blue', 'yellow']
for color in reversed(colors):
    print(color)
