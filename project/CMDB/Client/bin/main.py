import os
import sys

BASE_DIR = os.path.dirname(os.getcwd())
#设置工作目录
sys.path.append(BASE_DIR)

from core import handler


if __name__ == '__main__':
