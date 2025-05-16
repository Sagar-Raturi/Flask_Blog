from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '1e551a08ad2e9942c18480bdc42a8a00'
posts = [
    {
        'author': 'Corey Schaefer',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date posted': 'Arpil 20, 2023'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date posted': 'April 21, 2023'
    },
    {
        'author': 'John Smith',
        'title': 'Blog post 3',
        'content': 'Third post content',
        'date posted': 'April 22, 2023'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts =posts)

@app.route('/register', methods =['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods =['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='login', form=form)

@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
