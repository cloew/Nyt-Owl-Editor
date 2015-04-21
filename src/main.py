from kao_resources import ResourceDirectory
from knot import KnotApplication

import sys

def main(args):
    """ Run the main file """
    localResources = ResourceDirectory(__file__)
    app = KnotApplication.load(localResources.getProperPath('app.knot-app'))
    app.run()

if __name__ == "__main__":
    main(sys.argv[1:])