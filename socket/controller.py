from storage import add_task, list_tasks, remove_task

def handle_request(message):
    if message.startswith("ADD "):
        return add_task(message[4:])          
    elif message == "LIST":
        return list_tasks()                
    elif message.startswith("REMOVE "):
        return remove_task(message[7:])
    else:
        return "Invalid command."      
