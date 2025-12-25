def pattern1(N):
    for i in range(N):
        for j in range(N):
            print("*", end=" ")
        print()

#pattern1(3)
#pattern1(5)

def pattern2(N):
    for i in range(N):
        print("*" * (i + 1))

#pattern2(3)

def pattern3(N):
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

#pattern3(5)

def pattern4(N):
    for i in range(1, N + 1):
        for j in range(1, i+1):
            print(i, end=" ")
        print()

#pattern4(5)

def pattern5(N):
    for i in range(N):
        for j in range(N, i, -1):
            print("*", end=" ")
        print()
        
#pattern5(5)

def pattern6(N):
    for i in range(N):
        for j in range(N, i, -1):
            print(N-j+1, end=" ")
        print()

#pattern6(5)

def pattern7(N):
    for i in range(N):
        for j in range(N -i -1):
            print(" ", end=" ")
        for j in range(2*i + 1):
             print("*", end=" ")
        for j in range(N -i -1):
            print(" ", end=" ")
        print()
            
#pattern7(5)

def pattern8(N):
    for i in range(N):
        for j in range(N):
            print(" ", end=" ")
        for j in range(N, 1, -2):
             print("*", end=" ")
        for j in range(N):
            print(" ", end=" ")
        print()
pattern8(5)