#!/bin/python
import os
import re
import pprint
from optparse import OptionParser
import logging

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  default="NONE",
                  help="Files to Find", metavar="FILE")
parser.add_option("-i", "--input",
                  dest="input",
                  help="string to replace: A Reg ex is used")
parser.add_option("-o", "--output",
                  dest="output",
                  default='',
                  help="string to become: default ''")
parser.add_option("-w", "--write",
                  dest="write",
                  default=False,
                  action='store_true',                  #-w does not need a parameter
                  help="Should I execute this command True/False")
parser.add_option("-d", "--debug",
                  dest="debug",
                  default=True,
                  action='store_false',
                  help="Default False: Default is True")
(options, args) = parser.parse_args()


if options.debug==True:
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('Debug Enabled')
else:
    logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


if options.debug==True:
    logger.debug(str.format('file    is {}',options.filename))
    logger.debug(str.format('from    is {}',options.input))
    logger.debug(str.format('to      is {}',options.output))
    logger.debug(str.format('write   is {}',options.write))
    logger.debug(str.format('file    is {}',options.filename))


logger.info('Starting')
for root, dirs, files in os.walk('.'):
      for f in files:
        if re.search(options.filename,f):
            logger.debug(str.format('Orig File {}',f))
            filename=str.format('{}/{}',root,f)
            newfilename=filename.replace(options.input,options.output)
            if options.write==True:
                logger.debug(str.format('mv {} to {}',filename,newfilename))
                os.rename(filename,newfilename)
            else:
                logger.debug(str.format('TEST: mv {} to {}',filename,newfilename))

logger.info("Program Finishing")
