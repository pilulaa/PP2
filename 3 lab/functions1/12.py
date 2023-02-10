def histogram(x):
    l = []

    for i in x:
        s = ''
        j = i
        while j > 0:
          s += '*'
          j = j - 1
        l.append(s)
    
    for i in l:
        print(i)

h1 = histogram([4, 9, 7, 1])