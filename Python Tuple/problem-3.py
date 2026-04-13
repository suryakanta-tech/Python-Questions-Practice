# 3.Convert a tuple to list and add a new item, then convert back to tuple.
x = ('India',3.14,'surya',99,444)

# convert into list
x = list(x)
print(x)

# add item
x.append('odisha')
print(x)

# convert into tuple
x = tuple(x)
print(x)
