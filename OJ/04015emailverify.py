def is_valid(addr):
    if addr.count('@') != 1:
        return False
    if addr[0] == '.' or addr[-1] == '.' or \
            addr[0] == '@' or addr[-1] == '@':
        return False
    if addr.split('@')[1].count('.') == 0:
        return False
    if addr[addr.find('@') + 1] == '.' or \
            addr[addr.find('@') - 1] == '.':
        return False
    return True


while True:
    try:
        addr = input().strip()
        if is_valid(addr):
            print('YES')
        else:
            print('NO')
    except EOFError:
        break
