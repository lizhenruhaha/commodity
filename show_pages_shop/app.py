from flask import request, render_template, session, escape, redirect, url_for
# 数据库连接文件
from datebases_connection_look import app, Info

app.secret_key = 'xdfcgyuhijokpl'

@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'GET':
        return render_template('home_page.html')
    else:
        trade_name = request.form['sh_name']
        session['name'] = trade_name
        return redirect(url_for('particulars_page_bottom'))

@app.route('/particulars_page_bottom')
def particulars_page_bottom():
    trade_name = escape(session['name'])
    trade_name = str(trade_name)
    totals = Info.query.filter_by(search_name=trade_name).order_by(Info.prices).all()
    return render_template('particulars_page_bottom.html', totals=totals)

@app.route('/particulars_page_top')
def particulars_page_top():
    trade_name = escape(session['name'])
    trade_name = str(trade_name)
    totals = Info.query.filter_by(search_name=trade_name).order_by(Info.prices.desc()).all()
    return render_template('particulars_page_top.html', totals=totals)

if __name__ == '__main__':
    app.run(host='192.168.1.146')
