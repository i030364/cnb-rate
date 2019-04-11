from flask import Flask
from sys import argv
from cnbrates import cnbrates
import datetime

app = Flask(__name__)

if __name__ == '__main__':
    if len(argv) == 2:
        datum = argv[1]
    else:
        now = datetime.datetime.now()
        datum = str(now.day) + '.' + str(now.month) + '.' + str(now.year)
    cnbrates(datum)

