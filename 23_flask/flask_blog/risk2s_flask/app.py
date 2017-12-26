#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''Risk2S'''
# 使用 Python 的 Web 框架，做一个 Web 版本 留言簿 应用。
# 导入 Flask 类
from flask import Flask
# 模板继承
from flask import Markup,render_template,request,abort, redirect, url_for
# 创建Flask类的实例
app = Flask(__name__, static_folder='static', static_url_path='')
# 整合 WSGI 中间件
from werkzeug.contrib.fixers import LighttpdCGIRootFix
app.wsgi_app = LighttpdCGIRootFix(app.wsgi_app)

# 使用 route() 装饰器告诉 Flask 什么样的URL 能触发我们的函数
@app.route('/')
def indexss():
    return "heelo risk2s"
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('base.html', name=name)
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404
# 添加 Favicon
import os
from flask import send_from_directory
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')



#   if __name__ == '__main__': 确保服务器只会在该脚本被 Python 解释器直接执行的时候才会运行，而不是作为模块导入的时候。
if __name__ == '__main__':
    # 启用了调试支持，服务器会在代码修改后自动重新载入，并在发生错误时提供一个相当有用的调试器
    # 它 绝对不能用于生产环境
    app.debug = True
    # 用 run() 函数来让应用运行在本地服务器上
    # 让操作系统监听所有公网 IP
    app.run(host='0.0.0.0')