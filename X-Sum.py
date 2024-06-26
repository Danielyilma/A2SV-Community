
def inp(): return(int(input()))

def inlt():return(list(map(int,input().split())))

def insr():
    s = input()
    return(list(s[:len(s) - 1]))

def invr(): return(map(int,input().split()))


def solution():
    m, n = inlt()
    matrix = []
    maxsum = []
    
    for i in range(m):
        matrix.append(inlt())

    for i in range(m):
        for j in range(n):
            diag1 = 0

            verD = i
            horD = n - j - 1
            dis = verD if verD < horD else horD
            x, y = i - dis, j + dis
            while x < m and y >= 0:
                diag1 += matrix[x][y]
                x += 1
                y -= 1

            verD = i
            horD = j
            dis = verD if verD < horD else horD
            x, y = i - dis, j - dis
            while x < m and  y < n:
                diag1 += matrix[x][y]
                x += 1
                y += 1
            
            maxsum.append(diag1 - matrix[i][j])
    
    print(max(maxsum))



def main():
    t = inp()

    while t:
        solution()
        t -= 1

main()
