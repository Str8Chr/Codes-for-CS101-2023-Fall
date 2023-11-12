def is_larger(a, b):
    if a.lower() > b.lower():
        return 1
    elif a.lower() < b.lower():
        return -1
    else:
        return 0
print(is_larger(input(), input()))