jumsu = [90,45,64,9,17,29]
result=[]
for jumsu in jumsu:
    if 71<=jumsu:
        print('A')
        result.append("A")
    elif 41<=jumsu:
        print('B')
        result.append("B")
    elif 11<=jumsu:
        print('C')
        result.append("C")
    else :
        print('D')
        result.append("D")

print(result)

