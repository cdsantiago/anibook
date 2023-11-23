"""start up the app using configurations set"""
from anibook import create_app


anibook = create_app()

if __name__ == '__main__':
    anibook.run(host="localhost", port=1994, debug=True)
