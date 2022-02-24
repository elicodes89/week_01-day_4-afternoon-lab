

# Functions to complete:

## Get a list of uncompleted tasks



def get_uncompleted_tasks(list):

    status = []
    for value in list:
        if value["completed"] == False:
            status.append(value["description"])
    
    return status 
        
# uncomplete = get_uncompleted_tasks(tasks)
# print (uncomplete)

## Get a list of completed tasks
def get_completed_tasks(list):
    
    status = []
    for value in list:
        if value["completed"] == True:
            status.append(value["description"])
    
    return status 
        
# complete = get_completed_tasks(tasks)
# print (complete)
    

## Get tasks where time_taken is at least a given time

given_time = 15

def get_tasks_taking_at_least(list, time):
    
    taken_time = []

    for value in list:
        if value["time_taken"] >= time:
            taken_time.append (value["time_taken"])
        
    return taken_time

# at_least = get_tasks_taking_at_least(tasks, given_time)

# print (at_least)


## Find a task with a given description

our_job = "Walk Dog"


def get_task_with_description(list, description):

    is_task_correct = False
    
    for value in list:
        if value ["description"] == description:
            is_task_correct = True
    
    return is_task_correct

# the_task = get_task_with_description(tasks, our_job)

# print(the_task)





# Extention (Function): 

## Get a list of tasks by status
def get_tasks_by_status(list, status):
    pass

def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)



