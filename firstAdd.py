# /bin/python
# this file is just a tetst
import sys
import string

def jieCheng(k):
    res = 1
    while(k != 0):
	res = k * res
        k = k - 1
    return res

if __name__ == '__main__':
    para = sys.argv[1]
    r = jieCheng(string.atoi(para))
    print(r)
