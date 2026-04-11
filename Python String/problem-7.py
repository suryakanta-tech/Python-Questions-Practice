# 7. Take a comma-separated string like "apple,mango,banana" and
# split it into a list using .split(), then join it back with - using .join().

# convert into list
s = "apple,banana,grapes,mango"
print(s.split(','))
# again join it
x = '-'
seq = ('apple','banana','grapes','mango')
print(x.join(seq))
