def swap_case(S):
    import string

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    
    

    T = []
    for i in range(len(S)):
        if S[i] in lower:
            T.append(S[i].upper())
        elif S[i] in upper:
            T.append(S[i].lower())
        else:
            T.append(S[i])
    return (''.join(T))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print (result)

