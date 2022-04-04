T_list = []
W = input()
count = 0
while True :
    T = input()
    if T == "END_OF_TEXT" :
        break
    T_list = T.split(" ")
    for i in range(len(T_list)):
        T_list[i] = T_list[i].lower()
    for i in T_list:
        if i == W :
            count += 1
print(count)
