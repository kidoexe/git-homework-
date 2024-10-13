def LetsCount():
    sityva = input("sheiyvane sityva da vnaxot ramdeni asoa masshi: ")

    d = {}

    
    for i in sityva:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

   
    output = f'"{sityva}" -> {d}'
    print(output)
    
LetsCount()