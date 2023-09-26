s = 'apple'

try:
    num = int(s)
except ValueError:
    raise ValueError("string can't be changed into integer")