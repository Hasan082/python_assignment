def recursive(n):
    if n == 10:
        return None
    print(n)
    recursive(n + 1)
    print(n)


recursive(1)
