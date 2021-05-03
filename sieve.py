#Sieve of Eratosthenes (an even faster method)

#create list of values of length n + 1 where the first two values are false
def list_true(n):
    lst = list(range(n+1))
    for n in lst[0:2]:
        lst[0] = False
        lst[1] = False
    return lst

#function takes a list of booleans and a number p. Mark all elements 2p, 3p, . . . n false
def mark_false(bool_list, p):
    for a in bool_list:
        if bool_list[a] is False:
            continue
        for p in bool_list:
            p = 2
            while p<a:
                if a%p == 0:
                    bool_list[a] = False
                p += 1
        if bool_list[a] is not False:
            bool_list[a] = True
    return bool_list
print(mark_false(list_true(9),2))

#function returns the smallest element in a list which is not false and is greater than p.
def find_next(bool_list, p):
    x = 0
    cleared = False
    for bool in bool_list:
        if cleared:
            if bool:
                return x
        if x == p and bool:
            cleared = True
        x += 1
    return None
print(find_next(list_true(6),2))

#Return indices of True values
def prime_from_list(bool_list):
    y = [x for x, i in enumerate(bool_list) if i]
    prime_from_list = []
    for element in bool_list:
        if element == True:
            return y
    return prime_from_list
print(prime_from_list([False, False, True, True, False, True]))

def sieve(n):
    bool_list = list_true(n)
    p = 2
    while p is not None:
        bool_list = mark_false(bool_list, p)
        p = find_next(bool_list, p)
    return prime_from_list(bool_list)