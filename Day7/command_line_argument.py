import argparse
import os

# # parser = argparse.ArgumentParser(description="basic argument parsing.")
# parser = argparse.ArgumentParser(description="Multiple Arguments Example")
#
# subparser = parser.add_subparsers(dest="command")
#
# # parser.add_argument("--city",type=str,default="Unknown", help="your city")
# # parser.add_argument("--verbose",action="store_true", help="Enable verbose mode")
# # parser.add_argument("name",type=str,help="your name")
# # parser.add_argument( "age", type=int, help="your age")
# # parser.add_argument("--mode", choices=['dev','prod','test'],default="dev", help="choose the mode")
# # parser.add_argument("--numbers", type=int, nargs="+", help="List of numbers")
# add_parser = subparser.add_parser("add", help="Add two numbers")
# add_parser.add_argument("num1", type=int, help="First number")
# add_parser.add_argument("num2", type=int, help="Second number")
#
# sub_parser = subparser.add_parser("subtract", help="Subtract two numbers")
# sub_parser.add_argument("num1", type=int, help="First number")
# sub_parser.add_argument("num2", type=int, help="Second number")
#
# args = parser.parse_args()
#
# if args.command == "add":
#     print(f"results: {args.num1 + args.num2}")
#
# elif args.command == "subtract":
#     print(f"results: {args.num1 - args.num2}")
#
# # print(f"mode:{args.numbers}")
#
# # if args.verbose:
# #     print("Verbose mode enabled")

# def postive_int(value):
#     ivalue = int(value)
#     if ivalue <= 0:
#         raise argparse.ArgumentTypeError(f"{value} is not a positive integer")
#     return ivalue
#
# parser = argparse.ArgumentParser(description="custom Arguments Example")
# parser.add_argument("number", type=postive_int, help="a positive integer")

parser = argparse.ArgumentParser(description="using environment variables examples.")

parser.add_argument("--config", default=os.getenv("CONFIG_PATH", "default.conf"), help="Path to config file")

args = parser.parse_args()
print(f"Using config: {args.config}")