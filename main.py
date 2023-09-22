jumsu = [90,45,64,9,17,29]
result=[]

for i in jumsu:
    if 71<=i:
        print('A')
        result.append("A")
    elif 41<=i:
        print('B')
        result.append("B")
    elif 11<=i:
        print('C')
        result.append("C")
    else :
        print('D')
        result.append("D")

print(result)

