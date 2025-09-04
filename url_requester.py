def hello_google(session, args):
    url = args.url
    resp = session.get(url)
    if args.verbose:
        print(resp.text)
    else:
        print(resp.status_code)


def create_parser(parent_subparsers):
    description = "Subparser"
    parser = parent_subparsers.add_parser('requestor', help=description)

    subparsers = parser.add_subparsers(metavar='subcommand')
    subparsers.required = True

    show_description = "GET"
    show_parser = subparsers.add_parser('get', description=show_description, help=show_description)
    show_parser.add_argument("-v", "--verbose", action="store_true", help="Print text response")
    show_parser.add_argument("-u", "--url", help="Target URL")
    show_parser.set_defaults(execute=hello_google)