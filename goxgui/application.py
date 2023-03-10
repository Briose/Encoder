
'''

    Bitcoin trading tool for MtGox

    Copyright (c) 2013 Sebastian Haberey <sebastian@parango.de>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
    MA 02110-1301, USA.

'''

from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QApplication, QIcon
from market import Market
from preferences import Preferences
from view import View
import logging
import sys
import traceback
import utilities


class Application(QApplication):
    '''
    The main application class where the main objects
    are set up and connected with each other.
    '''

    def __init__(self, *args):

        QApplication.__init__(self, *args)

        # initialize logging
        logging.basicConfig(filename='log.txt', level=logging.INFO,
            format='%(asctime)s %(message)s')
        logging.info('Starting application.')

        # initialize user preferences
        preferences = Preferences()

        # initialize model
        market = Market(preferences)

        # initialize view
        self.view = View(preferences, market)

        self.connect(self, SIGNAL('lastWindowClosed()'), self.__quit)

    def __quit(self):
        self.view.stop()


if __name__ == '__main__':

    try:

        test = utilities.get_platform()
        app = Application(sys.argv)
        app.setWindowIcon(QIcon(utilities.resource_path('bitcoin.png')))
        app.exec_()

    except Exception as e:
        logging.error(traceback.format_exc())
        raise