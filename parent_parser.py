import sys
import argparse
import requests

import url_requester

parser = argparse.ArgumentParser(description="Argparse parent to subparent template.")
parser.add_argument("-p", "--parent-arg", default="default", help="Parent argument", required=False)

subparsers = parser.add_subparsers(metavar='command')
subparsers.required = True

url_requester.create_parser(subparsers)
args = parser.parse_args()

request_session = requests.Session()

cmd_result = args.execute(request_session, args)
exit_code = 0 if cmd_result or cmd_result is None else 1
sys.exit(exit_code)