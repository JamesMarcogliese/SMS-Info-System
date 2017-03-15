#!/usr/bin/python

"""Main script to chain together functions of the SIS.

"""

import sys
from sim900 import SIM900

def main():
    """Main entry point for the script."""
	
	while True:
	
	
    pass

if __name__ == '__main__':
	try:
		sim900 = SIM900()
		main()
	except KeyboardInterrupt:
		print "Killed by user"
		sim900.__del__()
		sys.exit(1)
	except:
		print "Other exception occured!"
		sim900.__del__()
		sys.exit(1)