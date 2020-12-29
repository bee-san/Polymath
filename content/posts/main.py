from collections import defaultdict
import glob
import os

path = "/mnt/c/Users/brand/Documents/Projects/blog/content/posts"
filecounts = {}
wordcount = 0
for filename in glob.glob(os.path.join(path, "*")):
    print(filename)
    with open(filename, "r") as f:
        words = f.read().split(" ")
        for word in words:
            wordcount += 1
print(f"The wordcount is {wordcount}")
