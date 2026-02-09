def Ticket_Pricing(n: int) -> int:
    if n < 5:
        return 0
    elif 5 <= n <= 17:
        return 10
    elif 18 <= n <= 64:
        return 20
    else:   # age 65 and above
        return 15
