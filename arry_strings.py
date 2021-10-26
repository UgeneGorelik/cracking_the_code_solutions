NO_OF_CHARS = 256

#1.1
def is_unique_set(str):
    if not str:
        return True
    if len(set(str)) == len(str):
        return True
    return False


def is_unique_hash(str):
    if not str:
        return True
    str_hash = {}
    for ch in str:
        if ch in str_hash:
            return False
        else:
            str_hash[ch] = True
    return True

#1.2
def is_permutation(str1,str2):
    if not str1 or not str2:
        return True
    if len(str1)!= len(str2):
        return False

    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    for x in range(0, len(sorted_str1)):
        if sorted_str1[x]!=sorted_str2[x]:
            return False

    return True

#1.3
def can_make_palindrom(str):
    count = [0] * (NO_OF_CHARS)

    for x in str:
        num_of_char = ord(x)
        count[num_of_char]= count[num_of_char]+1
    odd = 0
    for x in count:
        if x % 2 == 1:
            odd+=1

    if odd > 1:
        return False

    return True

#1.5
def edit_distance_one(str1,str2):
    len1 = len(str1)
    len2 = len(str2)


    if abs(len1-len2) > 1:
        return False

    if len1 == len2:
        return check_replace(str1, str2)
    else:
        return check_insert(str1,str2)


def check_insert(str1,str2):
    len1 = len(str1)
    len2 = len(str2)

    count = 0
    x= 0
    y=0
    while x < len1 and y < len2:
        if str1[x] != str2[y]:
            count+=1
            if count >1:
                return False
            x+= 1
        else:
            x+=1
            y+=1
    return True




def check_replace(str1,str2):
    count=0
    for x in range(9,len(str1)):
        if str1[x]!=str2[x]:
            count+=1
        if count >1:
            return False
    return True

str1 = "pale"
str2 = "sd"

print(edit_distance_one(str1,str2))

