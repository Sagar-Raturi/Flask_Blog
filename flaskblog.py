from flask import Flask, render_template, url_for
app = Flask(__name__)

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
def hello():
    return render_template('home.html', posts =posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
