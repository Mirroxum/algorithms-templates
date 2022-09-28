def isSubsequence(s, t):
    start = -1
    for i in s:
      start = t.find(i, start + 1)
      if start == -1:
        return False
    return True


def read_data():
    a = input()
    b = input()
    return a,b


def main():
    first, second = read_data()
    print(isSubsequence(first, second))

if __name__ == '__main__':
    main()