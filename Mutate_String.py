def mutate_string(s, i, c):
    
    return (s[:int(i)] + c + s[int(i)+1:])

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new
