from itertools import product

def Maximize(K, M):
    N = []
    S = 0

    for _ in range(K):
        N.append(list(map(int, input().split()))[1:])

    for lst in product(*N):
        add = sum(list(map(lambda x: x*x, lst)))
        S = max (add % M, S)

    print(S)
        
if __name__ == '__main__':
    K, M = map(int, input().split())
    result = Maximize(K, M)