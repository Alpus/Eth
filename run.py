#!env/bin/python3.4

from app import manager
from app import app

@manager.command
def debug():
    app.run(debug=True)

if __name__ == "__main__":
	manager.run()