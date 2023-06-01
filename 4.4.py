def odwrotnosc(list):
    for i in list:
        temp = str(i)
        temp2 =""
        for i in range( len(temp)):
            temp2 = temp2 + temp[len(temp)-1-i]
        print(temp2)

odwrotnosc([123,217,240])

def przeciwne(list):
    for i in list:
        print(i * -1)

przeciwne([123,217,-240])
def kwadraty(list):
    for i in list:
        print(i **2)
kwadraty([123,217,-240])