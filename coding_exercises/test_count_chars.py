# Should return: count_chars("hello") → {'h': 1, 'e': 1, 'l': 2, 'o': 1}

def count_chars(s):
    seen = {}

    for char in s:
        if char not in seen:
            seen[char] = 0
        seen[char] += 1
    return(seen)

print(count_chars('hello'))
print(count_chars('blueberry'))
print(count_chars('eek'))

