import sys

n = int(sys.stdin.buffer.readline())
out = 0
arrX = []
arrY = []

for i in range(0, n, 1):
  line = sys.stdin.readline()
  x, y = line.split(' ')
  arrX.append(int(x))
  arrY.append(int(y))

arrX = sorted(arrX)
arrY = sorted(arrY)

for i in range(0, n//2, 1):
  out += (arrX[n-i-1]
          - arrX[i]
          + arrY[n-i-1]
          - arrY[i])

sys.stdout.write(str(out))
