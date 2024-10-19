from flask import Flask, render_template
import time,datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    current_year=datetime.datetime.now().year
    return render_template('index.html',year=current_year)

@app.route('/blog')
def blog():
    blog_data=requests.get(url='https://api.npoint.io/c790b4d5cab58020d391').json()
    return render_template('blog.html', blog_posts=blog_data)

@app.route('/guess/<name>')
def guess(name):
    age_guess=requests.get(url=f'https://api.agify.io?name={name}').json()
    gender_guess=requests.get(url=f'https://api.genderize.io?name={name}').json()
    year = datetime.datetime.now().year
    return render_template('index.html',person_name=name, gender=f"I think you are {gender_guess['gender']}" , age=f"And maybe {age_guess['age']} years old",year=year)




if __name__ == "__main__":
    app.run(debug=True)


