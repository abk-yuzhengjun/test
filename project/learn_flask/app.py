from flask import Flask
import datetime
from copy import copy

app = Flask(__name__)


# 不可变tuple,str,number
# 可变list,dict,set

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/check')
def hello_world2():
    return 'It is working now %s' % datetime.datetime.now()


if __name__ == '__main__':
    app.run()
