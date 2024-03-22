b = int(input("Enter you bangla marks: "))
e = int(input("Enter you english marks: "))
m = int(input("Enter you math marks: "))
s = int(input("Enter you science marks: "))


def Avg(b, e, m, s):
    avg = (b + e + m + s) / 4
    if 0 <= avg <= 40:
        return "F"
    elif 41 <= avg <= 60:
        return "D"
    elif 61 <= avg <= 70:
        return "C"
    elif 71 <= avg <= 80:
        return "B"
    elif 81 <= avg <= 90:
        return "A"
    elif 91 <= avg <= 100:
        return "A+"

print(Avg(b, e, m, s))