import argparse

arguments = []
parser = argparse.ArgumentParser()
# parser.add_argument("echo", help="This will print the first variable")
parser.add_argument("x", type=int, help="base")
parser.add_argument("y", type=int, help="the exponent")
parser.add_argument("-v","--verbose", help="Adding the verbosity", action="count", default=0)

args = parser.parse_args()

answer = args.x**args.y

if args.verbose >= 2:
    print("{} to the power {} equals {}".format(args.x,args.y,answer))
elif args.verbose >= 1:
    print("{}^{} == {}".format(args.x,args.y,answer))
else:
    print(answer)

