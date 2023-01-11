def maximumWealth(self, accounts: List[List[int]]) -> int:
    maximum = 0
    for cust in accounts:
        temp = 0
        for wealth in cust:
            temp += wealth
        if maximum < temp:
            maximum = temp

    return maximum
