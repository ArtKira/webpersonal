
from flask import Flask, redirect, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY']='secret'
########rutas public ########
@app.route('/')
def index():
    return render_template('public/index.html')

@app.route('/about')
def about():
    return render_template('public/about.html')

@app.route('/contact')
def contact():
    return render_template('public/contact.html')

@app.route('/portfolio')
def portfolio():
    projects=[#creamos el direccionario para el portafolio son sus caracteristicas 
        {
            'name':'Primer proyecto',
            'description':'As we got further and further away, it [the Earth] diminished in size. Finally it shrank to the size of a marble, the most beautiful you can imagine. That beautiful, warm....',
            'image':'img/home-bg.jpg',
            'url':'http://google.com'
        },
        {
            'name':'Segundo proyecto',
            'description':'As we got further and further away, it [the Earth] diminished in size. Finally it shrank to the size of a marble, the most beautiful you can imagine. That beautiful, warm....',
            'image':'img/about-bg.jpg',
            'url':'http://google.com'
        }
    ]
    return render_template('public/portfolio.html', projects=projects)

################FORMULARIOS DE WTFORMS########################
class loginForm(FlaskForm):
    email=EmailField('Username', validators=[DataRequired(), Email()])#validamos los datos 
    password=PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField('Ingresar')

######### Auth ###########
@app.route('/auth/login',  methods=['GET', 'POST'])
def login():
    form=loginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        return render_template('admin/index.html', email=email)
    
    return render_template('/auth/login.html', form=form)

@app.route('/auth/register')
def register():
    return render_template('/auth/register.html')

@app.route('/welcome', methods=['GET', 'POST'])
def welcome(form):#obtenemos los datos del from con un request obtenemos el emial y password redirigimos a index
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        return render_template('admin/index.html', email=email)
    
    return redirect(url_for('login'))

@app.errorhandler(404)
def page_error_not_found(e):
    return render_template('errores/404.html'), 404

if __name__=='__main__':
    app.run(debug=True)

