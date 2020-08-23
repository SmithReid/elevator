from system import System
from parser import Parser

if __name__ == "__main__":
    parser = Parser("instructions/one.txt")
    system = System(parser, 8, 2)
    system.run()