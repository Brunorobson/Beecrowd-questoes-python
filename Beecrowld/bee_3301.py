H, Z, L = map(int, input().split())
if H < Z and L > Z or L < Z and H > Z:
    print('zezinho')
elif H > L  and L > Z or L < Z and H < L:
    print('luisinho')
elif Z > H and H > L or H < L and Z < H:
    print('huguinho')