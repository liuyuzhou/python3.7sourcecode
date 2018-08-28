from flask import Flask

# 创建Flask实例
app = Flask(__name__)

from server import views
