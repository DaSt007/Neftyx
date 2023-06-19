import os

from flask import Flask, render_template

data = {
    1: {
        "title": "Shrek",
        "image": "https://i.imgflip.com/5koz7c.png?a467448",
        "description": "Odvážný Shrek (Mike Myers) pátrá se svým kamarádem, sympatickým a chvastounským oslem (Eddie Murphy) po krásné a divoké princezně Fioně (Cameron Diaz). Za její záchranu chce od intrikána Lorda Farquadda (John Lithgow) získat zpět svou milovanou bažinu. (Bontonfilm)",
        "rating": 0.52,
        "genres": [
            "Horror",
            "Fantasy",
            "Comedy",
        ],
        "year": 2001,
        "duration": 90,
        "director": "Vicky Jenson, Andrew Adamson",
        "cast": [
            "Mike Myers",
            "Eddie Murphy",
            "Cameron Diaz",
            "John Lithgow",
            "Vincent Cassel",
            "Jim Cummings",
            "Simon J. Smith",
            "Conrad Vernon",
            "Ian Abercrombie",
        ]
    },
    2: {
        "title": "Renfield",
        "image": "https://image.pmgstatic.com/cache/resized/w140/files/images/film/posters/167/061/167061195_0c6f91.jpg",
        "description": "Příběh Renfielda (Nicholas Hoult), Drákulova věčně oddaného a neustále ponižovaného služebníka.",
        "rating": 0.52,
        "genres": [
            "Horror",
            "Fantasy",
            "Comedy",
        ],
        "year": 2001,
        "duration": 90,
        "director": "Vicky Jenson, Andrew Adamson",
        "cast": [
            "Mike Myers",
            "Eddie Murphy",
            "Cameron Diaz",
            "John Lithgow",
            "Vincent Cassel",
            "Jim Cummings",
            "Simon J. Smith",
            "Conrad Vernon",
            "Ian Abercrombie",
        ]
    },
    3: {
        "title": "Shrek 2",
        "image": "https://image.pmgstatic.com/cache/resized/w140/files/images/film/posters/159/450/159450263_fdb61d.jpg",
        "description": "Když zlobr Shrek zachránil princeznu Fionu a překonal s ní mnohá protivenství, měli spolu podle pohádkových zákonů žít šťastně až do smrti.",
        "rating": 0.52,
        "genres": [
            "Horror",
            "Fantasy",
            "Comedy",
        ],
        "year": 2001,
        "duration": 90,
        "director": "Vicky Jenson, Andrew Adamson",
        "cast": [
            "Mike Myers",
            "Eddie Murphy",
            "Cameron Diaz",
            "John Lithgow",
            "Vincent Cassel",
            "Jim Cummings",
            "Simon J. Smith",
            "Conrad Vernon",
            "Ian Abercrombie",
        ]
    },
    4: {
        "title": "Super Mario Bros. ve filmu",
        "image": "https://image.pmgstatic.com/cache/resized/w140/files/images/film/posters/167/158/167158524_281a5e.jpg",
        "description": "Sourozenci Mario a Luigi sní o tom, že povedou nejlepší instalatérskou firmu v New Yorku, což jim zatím moc nevychází.",
        "rating": 0.52,
        "genres": [
            "Horror",
            "Fantasy",
            "Comedy",
        ],
        "year": 2001,
        "duration": 90,
        "director": "Vicky Jenson, Andrew Adamson",
        "cast": [
            "Mike Myers",
            "Eddie Murphy",
            "Cameron Diaz",
            "John Lithgow",
            "Vincent Cassel",
            "Jim Cummings",
            "Simon J. Smith",
            "Conrad Vernon",
            "Ian Abercrombie",
        ]
    }
}

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    @app.route('/')
    @app.route('/index')
    def index():
        global data
        return render_template('index.html', data=data)

    @app.route('/dva')
    def dva():
        return render_template('dva.html')
    
    @app.route('/detail')
    def detail():
        rating= "2%"
        comments= [
                {
                    "name":"Vasek",
                    "text":"neconeconeconeconeconeconeco"
                },
                {
                    "name":"Dan",
                    "text":"jineneconeconeconeconeconeconeco"
                },
            ]
        return render_template('detail.html', rating="2%", comments=comments)

    return app