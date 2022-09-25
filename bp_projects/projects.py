from flask import Blueprint, render_template

app_projects = Blueprint('projects', __name__,
                url_prefix='/projects',
                template_folder='templates/bp_projects/')

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/Jishnu Singiresu/')
def jishnu():
    return render_template("jishnu.html")

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/Edwin Abraham/')
def edwin():
    return render_template("edwin.html")

@app_projects.route('/Emaad Mir/')
def emaad():
    return render_template("emaad.html")

@app_projects.route('/Luka Van Den Boomen/')
def luka():
    return render_template("luka.html")