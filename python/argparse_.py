import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--foo')
parser.add_argument('-b', '--bar')
args = parser.parse_args()

if args.f == 'magic':
    print 'You nailed it!'

if __name__ == '__main__':
    pass
