import sys
from argparse import ArgumentParser
from optics.general import fileutil


def parse_args(argv):
    parser=ArgumentParser()
    parser.add_argument('--inputdirectory', required=True, help='Directory with zip files')
    parser.add_argument('--outputdirectory', required=True, help='Directory to unzip files to')
    return parser.parse_args(argv)


def main(argv):
    args=parse_args(argv)
    only_zip=fileutil.list_only_zip_files(fileutil.listdir(args.inputdirectory))
    for item in only_zip:
        fileutil.unzip_file(item, args.outputdirectory)


if __name__ == '__main__':
    main(sys.argv[1:])