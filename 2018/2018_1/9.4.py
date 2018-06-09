"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://www.jtahstu.com
@time: 2018/1/11 11:33
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    # 3
    # return "It's alive!"
    # 4
    k = {}
    k['thing'] = request.args.get('thing')
    k['height'] = request.args.get('height')
    k['color'] = request.args.get('color')
    return render_template('home.html', **k)


app.run(port=5000, debug=True)
