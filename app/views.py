from flask import render_template, flash, redirect
from app import app, mysql
from .forms import MyForm

@app.route('/', methods=('GET', 'POST'))
@app.route('/index')
def index():
    form = MyForm()
    conn = mysql.connect()
    cursor = conn.cursor()
    

    if form.validate_on_submit():
        print form.name.data
        cursor.execute('INSERT INTO user (id, name) VALUES (NULL, \'%s\' )' % str(form.name.data))
        conn.commit()
        #This is stored procedure to call list of user
        cursor.execute('call test2()')
        data = cursor.fetchall()
        print data
        flash('REQUESTED DATA %s' % form.name.data)
        return str('You Input '+ form.name.data)
    return render_template('formku.html', title='DUmmy form', form=form)
