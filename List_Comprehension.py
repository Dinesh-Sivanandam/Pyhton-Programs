if __name__ == '__main__':
    X = int(input())
    Y = int(input())
    Z = int(input())
    N = int(input())



ans = [[i, j, k] for i in range(X + 1) for j in range(Y + 1) for k in range(Z + 1) if i + j + k != N]
print (ans)
