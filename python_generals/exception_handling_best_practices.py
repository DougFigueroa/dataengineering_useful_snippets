# Best practices for exception handling in Python

# 1: Dont use Try/Except and don't do anything with the exception

try:
    print('Try test')
except Exception as e:
    pass #DONT
print('Finished successfully')

# 2: Use asserts only for testing purposes