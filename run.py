
from dbmanager.factory import create_app


import os
import configparser


config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

if __name__ == "__main__":
    app = create_app()
    app.config['DEBUG'] = True
    app.config['MONGO_URI'] = 'mongodb+srv://admin:KblCB0vopEWESS9B@cluster0.qoc4o3y.mongodb.net/'

    app.run()