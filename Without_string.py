Read an integer n.

Without using any string methods, try to print the following:
123...N

Note that "" represents the values in between.

if __name__ == '__main__':
    value=int(input())
for number in range(value) :
    print(number+1, end="")
