def bestClosingTime(customers):
    temp = 0
    for i in range(len(customers)):
        if customers[i] == "Y":
            temp += 1
    ans = 0
    cur_max = temp
    for j in range(len(customers)):
        if customers[j] == "Y":
            temp -= 1
            if temp < cur_max:
                ans = j + 1
                cur_max = temp
        else:
            temp += 1
    
    return ans