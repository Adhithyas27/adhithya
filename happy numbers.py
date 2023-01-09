def _is_happy_num(n):
    past = set()
    while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
    return True
print(_is_happy_num(7))
print(_is_happy_num(932))
print(_is_happy_num(6))

