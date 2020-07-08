from manager import Manager

if __name__ == '__main__':
    instructions = 'instructions/' + input("Please enter instruction filename: ")
    manager = Manager(8, 2, instructions)
    done = False
    while done == False:
        end = input('tick {}'.format(manager.tick_number))
        if end == 'end':
            manager.end_run()
        done = manager.tick()