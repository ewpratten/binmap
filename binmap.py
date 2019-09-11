import argparse
import numpy as np
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("file", help="File to convert to image")
ap.add_argument("-w", "--width", help="Image wrap/width in px", default=100)
args = ap.parse_args()

args.width = int(args.width)

    

# Handle issues with file loading
try:
    with open(args.file, "rb") as fp:
        file = fp.read()
        fp.close()
except:
    print("File error")
    exit(1)


def divAt(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


img = divAt(file, args.width)
output = []

for row in img:
    ro = []
    for col in row:

        px = max(min(col, 255), 0)


        ro.append((0, px, 0))
    output.append(ro)

output = output[:-1]


oi = Image.fromarray(np.array(output, dtype=np.uint8))
oi.save("./output.png")