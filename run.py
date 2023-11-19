"""start up the app using configurations set"""
import pdb
from animotion import create_app



animotion = create_app()

if __name__ == '__main__':
    animotion.run(host="localhost", port=1994, debug=True)
