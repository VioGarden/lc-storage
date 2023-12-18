def bestClosingTime(customers):
    high_score = curr_score = 0
    ans = -1

    for index, value in enumerate(customers):
        curr_score += 1 if value == "Y" else - 1
        if curr_score > high_score:
            high_score, ans = curr_score, index
    return ans + 1