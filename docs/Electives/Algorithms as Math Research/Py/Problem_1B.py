import sys
import math

n = int(sys.stdin.buffer.readline())
out_m = 0
out_p = 0
arrX_p = []
arrX_m = []
arrY_p = [0]
arrY_m = [0]

for i in range(0, n, 1):
    line = sys.stdin.readline()
    x, y = map(float, line.split(' '))

    
    if y == 0:
        if x < 0:
            arrX_m.append(x)
        elif x > 0:
            arrX_p.append(x)
    elif x < 0:
        arrY_m.append(math.fabs(y))
    elif x > 0:
        arrY_p.append(math.fabs(y))

arrX_m = sorted(arrX_m)
arrX_p = sorted(arrX_p)
arrY_m = sorted(arrY_m)
arrY_p = sorted(arrY_p)



if len(arrX_m) > 1:
    l_m = arrX_m[-1] - arrX_m[0]
    out_m = l_m*arrY_m[-1]/2
if len(arrX_p) > 1:
    l_p = arrX_p[-1] - arrX_p[0]
    out_p = l_p*arrY_p[-1]/2

out = max(out_m, out_p)

sys.stdout.write(str(out))
