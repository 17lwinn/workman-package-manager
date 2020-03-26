import sys
import os
with open("list.txt") as f:
    for line in f:
        os.remove(line.rstrip('\n'))https://discord.gg/vmYvWX