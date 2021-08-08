with open('data1.inp', 'r') as f:
    check = True
    d = dict()
    for line in f:
        line = line.strip()
        
        if line == 'PARTIES:':
            continue
        
        if line == 'VOTES:':
            check = False
            continue
        
        else:
            d[line] = d.get(line, 0) + 1
    
    lst = [(k, v) for k, v in d.items()]
    print(lst)
    lst.sort(key = lambda x: (x[1], x[0]))
    print(lst)