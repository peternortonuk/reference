'''
https://docs.python.org/2/howto/argparse.html
'''
import argparse

parser = argparse.ArgumentParser()

# add a positional argument called square that will convert string to integer
# argparse treats options as strings, unless we tell it otherwise
parser.add_argument("square", type=int)

# add an optional argument but use keyword action=store_true
# if the option is specified then assign True otherwise assign False.
parser.add_argument("-v", "--verbose", action="store_true")

args = parser.parse_args()



# process the args
answer = args.square**2
if args.verbose:
    print "the square of {} equals {}".format(args.square, answer)
else:
    print answer


'''
try this at command prompt
python C:\dev\code\reference\python\argparse_.py 4 --verbose
python C:\dev\code\reference\python\argparse_.py 4 -v

still works if you flip the order
'''
