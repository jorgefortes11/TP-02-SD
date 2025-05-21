tasks = []

def add_task(task_description):
    tasks.append(task_description)
    return f"Task added. ID: {len(tasks)-1}"

def list_tasks():
    if not tasks:
        return "No tasks available."
    return "\n".join([f"{i}: {t}" for i, t in enumerate(tasks)])

def remove_task(task_id_str):
    try:
        idx = int(task_id_str)
        if 0 <= idx < len(tasks):
            tasks.pop(idx)
            return "Task removed." 
        return "Invalid ID."
    except:
        return "Error removing task."
