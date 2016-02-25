from application import create_app
from flask.ext.script import Manager


app = create_app('config.cfg')
manager = Manager(app)


if __name__ == '__main__':
    manager.run()
