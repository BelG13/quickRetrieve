import argparse as ap
import logging


argparser = ap.ArgumentParser()
argparser.add_argument(
    "-v",
    "--verbose",
    help="foo description",
    action="store_true"
)

args =argparser.parse_args()
print(args.foo)

