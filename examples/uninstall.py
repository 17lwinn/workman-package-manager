import sys
import os
fil = sys.argv[1]
with open(list.txt) as f:
    for line in f:
        os.remove(line.rstrip('\n'))