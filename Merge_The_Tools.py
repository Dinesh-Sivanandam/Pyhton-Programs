def merge_the_tools(s, k):
    # your code goes here

    chunks = len(s)/k

    for index in xrange(chunks):
        merge = ""
        T = s[index*k : (index+1)*k]
        for ch in T:
            if ch not in merge:
                merge += ch
        print merge

if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
    
