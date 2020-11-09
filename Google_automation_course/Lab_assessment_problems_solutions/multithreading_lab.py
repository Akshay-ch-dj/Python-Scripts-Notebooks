# "# %%""
# Python interactive mode for VScode
# If vir. environment changed use `ctrl+shift+p` > restart ipython kernel to
# restart the kernel


# 1. My solution

# !/usr/bin/env python

import subprocess
import os
from multiprocessing import Pool

# The source and destination paths in which data to transferred
src = "./data/prod"
dest = "./data.prod_backup"


def run(dir):
    print("Moving directory: {}".format(dir))
    subprocess.call(["rsync", "-arq", dir, dest])


if __name__ == "__main__":
    filesDir = [os.path.join(src, file) for file in os.listdir(src)]
    p = Pool(len(filesDir))
    p.map(run, filesDir)
