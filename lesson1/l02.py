A=5
B=6
C=7

if A > B:
    print("A > B")
else:
    print("B >= A")

if A > B > C:
    print("A > B > C")
elif A > B < C:
    print("A > B < C")
elif A < B < C:
    print("A < B < C")

if A < B:
    if B < C:
        print("A < B < C")
    else:
        if B > C:
            print("A < B > C")
    