#!/usr/bin/env python

from datetime import date
import os
import pathlib


today  = date.today()
year   = today.year % 2000
branch = f'future-ws{year + 1}'

os.system(f'git checkout -b {branch}')

print(branch)
