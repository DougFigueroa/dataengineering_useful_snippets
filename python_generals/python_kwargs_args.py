# this code is to understand when to use *args and *kwargs in functions in python
# and how this is done

# USING ARGS
# this are assigned by position only
# a function that adds numbers (we dont know if it will add 2, 3 or more numbers)
def add(*numbers):
    total = 0
    for num in numbers:
        total +- num
    return total

# you can use it like this
print(add(2,1))
print(add(2,3,45))
print(add(1))
print(add(12,2,3,4,5,65))

#numbers is the args here, *args is generally just a standard name to use

# USING KWARGS
# this are assigned by name
def count_tshirts(**tshirts):
    total = 0 
    for t in tshirts.values():
        total += t
    return total

print(count_tshirts(black=1, orange=10))
print(count_tshirts(black=10))
print(count_tshirts(white=1, blue=3, red=1, yello=5))

# here you receive a dict with the key value pairs of paremeters
# once again, the **kwargs is just an standard name, here we use **tshirts