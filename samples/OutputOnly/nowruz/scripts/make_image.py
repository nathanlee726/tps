import sys
from random import randint

lines = [line.strip() for line in sys.stdin.readlines()]


def is_av(x, y):
    global lines
    if x < 0 or y < 0:
        return False
    try:
        lines[x][y]
    except IndexError:
        return False
    return True


def main():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    res = [[2] * len(lines[0]) * 3 for tmp in range(len(lines) * 3)]
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if lines[x][y] == '.':
                res[3 * x + 1][3 * y + 1] = 0
                res[3 * x][3 * y] = 1
                res[3 * x][3 * y + 2] = 1
                res[3 * x + 2][3 * y] = 1
                res[3 * x + 2][3 * y + 2] = 1
                cnt = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if is_av(nx, ny) and lines[nx][ny] == '.':
                        cnt += 1
                        res[3 * x + 1 + dx[k]][3 * y + 1 + dy[k]] = 0
                    else:
                        res[3 * x + 1 + dx[k]][3 * y + 1 + dy[k]] = 1
                if cnt == 1:
                    res[3 * x + 1][3 * y + 1] = -1
            elif lines[x][y] == '#':
                for nx in range(3 * x, 3 * x + 3):
                    for ny in range(3 * y, 3 * y + 3):
                        res[nx][ny] = 3
    print "P3"
    print "{} {}".format(len(res[0]), len(res))
    print 255
    for x in range(len(res)):
        for y in range(len(res[0])):
            if res[x][y] == -1: #leaf
                sys.stdout.write("0 0 0 ")
            elif res[x][y] == 0: #tree
                sys.stdout.write("0 0 0 ")
            elif res[x][y] == 1: #treeside
                sys.stdout.write("128 128 128 ")
            elif res[x][y] == 2: #open
                sys.stdout.write("0 {} 0 ".format(randint(64, 128)))
            else: #block
                sys.stdout.write("73 56 41 ")
        print


if __name__ == "__main__":
    main()
