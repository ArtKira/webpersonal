from flask import Blueprint, render_template

home_blueprint=Blueprint('', __name__)

########rutas public ########
@home_blueprint.route('/')
def index():
    return render_template('public/index.html')

@home_blueprint.route('/about')
def about():
    return render_template('public/about.html')

@home_blueprint.route('/contact')
def contact():
    return render_template('public/contact.html')

@home_blueprint.route('/portfolio')
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