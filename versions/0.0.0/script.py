from manager import Manager

if __name__ == '__main__':
    instructions = 'instructions/' + input("Please enter instruction filename: ")
    manager = Manager(8, 2, instructions)
    manager.start_run()