# A Dictionary in python is the unordered and changeable collection of data values that holds key-value pairs.
# A Dictionary in python is declared by enclosing a comma-separated list of key-value pairs using curly braces({}).
#Syntax for python Dictionary
'''
student1={'Name':'saicharan','branch':'ECE','Section':'A','Roll_no':21}
print(type(student1))
print(student1)

student1={'Name':'saicharan','branch':'ECE','Section':'A','Roll_no':21,'Name':'cherry'}
print(student1)

student1={'Name':'saicharan','branch':'ECE','Section':'A','Roll_no':21}
print(student1['Name'])

student1={'Name':'saicharan','branch':'ECE','Section':'A','Roll_no':21}
print(student1['Roll_no'])

student1={'Name':'saicharan','branch':'ECE','Section':'A','Roll_no':21}
print("Before updating")
print(student1)

#'Member':'NCC'
student1.update({'Member':'NCC'})
print("After updating")
print(student1)

#Delete keys from the dictionary
student1={'Name':'saicharan','branch':'ECE','Section':'A','Roll_no':21}
print("Before deleting")
print(student1)

del student1['Name']
print("After deleting")
print(student1)

print(student1.items())

student1={'Name': 'saicharan', 'branch': 'ECE', 'Section': 'A', 'Roll_no': 21, 'Member': 'NCC'}
print("keys of student1 are")
print(student1.keys())
'''
student1={'Name': 'saicharan', 'branch': 'ECE', 'Section': 'A', 'Roll_no': 21, 'Member': 'NCC'}
for i in student1.keys():
    print(student1[i])
