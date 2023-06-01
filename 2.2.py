n = input()
n = n.lower()
match n:
    case "zero":
        n = 0
    case "jeden":
        n = 1
    case "dwa":
        n=2
    case "trzy":
        n=3
    case "cztery":
        n=4
    case "pięć":
        n=5
    case "sześć":
        n=6
    case "siedem":
        n=7
    case "osiem":
        n=8
    case "dziewięć":
        n=9
print(n)