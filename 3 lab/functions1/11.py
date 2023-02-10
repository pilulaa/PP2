def palindromme(str):
    x = len(str)
    q = False

    for i in range(0, int(x/2)):
        for j in range(int(x/2) - 1, x):
            if str[i] == str[j]:
                return True
    
    return q

s1 = palindromme("madam")
s2 = palindromme("paap")

print(s1)
print(s2)