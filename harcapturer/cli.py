import argparse
import sys

def main(args) -> int:
    parser = argparse.ArgumentParser(description='CMD_DESCRIPTION',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--web-port', '-wp', type=int, default=8899,
                        help='The port number for the web server')

    parsed_args = parser.parse_args(args)

def app_main():
    sys.exit(main(sys.argv[1:]))

if __name__ == '__main__':
    app_main()
