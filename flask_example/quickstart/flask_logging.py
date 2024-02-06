#use logger

from flask import Flask

app = Flask(__name__)

#logger example
app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')