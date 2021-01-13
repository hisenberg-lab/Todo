import sys
import os
from datetime import date

date_iso = date.today()

def helpp():
    usage ="""Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""
    sys.stdout.buffer.write(usage.encode('utf8'))

def ls():
    """ Method to print all pending todos"""
    if os.path.exists('todo.txt'):
         with open('todo.txt','r') as todo:
            # tasks = todo.readlines()
            tasks = list(filter(None, (task.rstrip() for task in todo)))
            # print(tasks)
            for num, task in reversed(list(enumerate(tasks, 1))):
                sys.stdout.buffer.write(f"{[num]} {task}\n".encode('utf8'))
    else:
        sys.stdout.buffer.write('There are no pending todos!'.encode('utf8'))

def add(args):
    """ Method to add a new task to todo.txt"""
    task = args
    if os.path.exists('todo.txt'):
        append_write = 'a'
    else:
        append_write = 'w'

    with open('todo.txt', append_write) as todo:
        todo.write(f"{task}\n")
    sys.stdout.buffer.write(f'Added todo: "{task}"'.encode('utf8'))

    
def dele(args):
    """ Method to delete a task """
    if os.path.exists('todo.txt') :
        num = int(args)
        with open('todo.txt', 'r') as todo:
            tasks = list(filter(None, (task.rstrip() for task in todo)))

        num_tasks = len(tasks)
        
        if (num <= 0 or num > num_tasks):
            sys.stdout.buffer.write(f'Error: todo #{num} does not exist. Nothing deleted.'.encode('utf8'))
            return
        else :
            os.remove('todo.txt')
            for i, task in enumerate(tasks):
                    with open('todo.txt', 'a') as todo:                                        
                        if i != num-1:
                            todo.write(tasks[i]+'\n')
            sys.stdout.buffer.write(f'Deleted todo #{num}'.encode('utf8'))

def done(args):
    """Method to mark a task as completed and add to done.txt """
    if os.path.exists('todo.txt') :
        num = int(args)
        with open('todo.txt', 'r') as todo:
            # tasks = todo.readlines()
            tasks = list(filter(None, (task.rstrip() for task in todo)))

        num_tasks = len(tasks)
        if num <= 0 or num > num_tasks:
            sys.stdout.buffer.write(f'Error: todo #{num} does not exist.'.encode('utf8'))
            return
        else:
            os.remove('todo.txt')
            for i, task in enumerate(tasks):
                    with open('todo.txt', 'a') as todo:
                        if i != num-1:
                            todo.write(tasks[i]+'\n')
            completed = tasks[num-1]
            with open('done.txt', 'a') as done:
                done.write(f'x {date_iso} {completed} \n')
            sys.stdout.buffer.write(f"Marked todo #{num} as done.".encode('utf8'))

def report():
    """Method to get the latest tally of pending and completed todos"""
    pending = 0
    completed = 0
    if os.path.exists('todo.txt'):
        with open('todo.txt', 'r') as todo:
            # tasks = todo.readlines()
            tasks = list(filter(None, (task.rstrip() for task in todo)))
        pending = len(tasks)
        # print(pending)

    if os.path.exists('done.txt'):
        with open('done.txt', 'r') as done:
            tasks = list(filter(None, (task.rstrip() for task in done)))
        # tasks = '\n'.join(tasks).split()
        completed = len(tasks)
        # print(tasks)
    sys.stdout.buffer.write(f"{date_iso} Pending : {pending} Completed : {completed}".encode('utf8'))

if __name__ == "__main__":
    if len(sys.argv)==1 or sys.argv[1]=='help':
        helpp()   
    elif sys.argv[1]=='ls':
        ls()
    elif sys.argv[1]=='add':
        if len(sys.argv) > 2:
            add(sys.argv[2])
        else:
            sys.stdout.buffer.write('Error: Missing todo string. Nothing added!'.encode('utf8'))
    elif sys.argv[1]=='del':
        if len(sys.argv) > 2:
            dele(sys.argv[2])
        else:
            sys.stdout.buffer.write("Error: Missing NUMBER for deleting todo.".encode('utf8'))
    elif sys.argv[1]=='done':
        if len(sys.argv)>2:
            done(sys.argv[2])
        else:
            sys.stdout.buffer.write("Error: Missing NUMBER for marking todo as done.".encode('utf8'))
    elif sys.argv[1]=='report':
        report()
    else:
        sys.stdout.buffer.write('Error: Argument not available. Use "./todo help"'.encode('utf8'))