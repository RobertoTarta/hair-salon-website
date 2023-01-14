import sqlite3
from flask import Flask, render_template,redirect,url_for,flash,request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdjasfnsdflajfsdklsglsldf'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/hairCutting')  
def HairCutting():  
    return redirect('/')
@app.route('/beardShaving') 
def BeardShaving():  
    return redirect('/')
@app.route('/HairColoring') 
def HairColoring():  
    return redirect('/')
@app.route('/Manicure') 
def Manicure():  
    return redirect('/')
@app.route('/Pedicure')
def Pedicure():  
    return redirect('/')
@app.route('/AboutUs')
def AboutUs():  
    return redirect('/')
@app.route('/WhereToFindUs')
def WhereToFindUs():  
    return render_template('findUs.html')
@app.route('/OurHistory')
def OurHistory():  
    return redirect('/')    
@app.route('/ContactUs')
def ContactUs():  
    return render_template('contactUs.html')




@app.route('/appointments')
def appointments():
    return render_template('appointment.html')

@app.route('/appointments/<date>', methods=('GET', 'POST'))
def dateselector(date):
    date=date
    return render_template('posts.html',date=date)

@app.route('/appointments/unselected')
def unselected():
    flash('You did not select a date!')  
    return redirect(url_for('index'))

@app.route('/create/<date>')
def create(date):
    conn = get_db_connection()
    date=date
    posts = conn.execute('SELECT * FROM posts WHERE CONVERT(DATETIME, FLOOR(CONVERT(FLOAT, postsdate))) = ' + date).fetchall()
    conn.close()
    return render_template('posts.html', posts=posts)    

@app.route('/create/post', methods=('GET', 'POST'))
def creates():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        date = request.form['postsdate']
        time = request.form['poststime']
        service = request.form['service']


        if not firstName:
            flash('First Name is required!')
        elif not lastName:
            flash('Last Name is required!')
        elif not email:
            flash('Email is required!')
        elif not date:
            flash('Date is required!')
        elif not time:
            flash('Time is required!')
        elif not service:
            flash('Service type is required!')    
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (firstName, lastName, email, postsdate, poststime, service) VALUES (?, ?, ?, ?, ?, ?)',
                         (firstName, lastName, email, date, time, service))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html') 

if __name__ == '__main__':
        app.run(debug=True)

