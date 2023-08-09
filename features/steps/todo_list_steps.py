from behave import given, then, when
from todo_list import TodoList

# Add Task
@given("the to-do list is empty")
def step_given_empty_todolist(context):
    context.todo_list = TodoList()

@when("the user adds a task {task_title} with priority {task_priority}")
def step_when_user_add_task(context, task_title, task_priority):
    context.todo_list.addTask(task_title, task_priority)

@then("the to-do list should contain {task_title} with priority {task_priority}")
def step_then_todolist_have_user_add_task(context, task_title, task_priority):
    task = [str(task) for task in context.todo_list.tasks if task.title == task_title and task.priority == task_priority]
    assert task

# List all task in the to-do list
@given("the to-do list contains tasks")
def step_given_todolist_have_user_tasks(context):
    context.todo_list = TodoList()
    for row in context.table:
        context.todo_list.addTask(row["Task"], row["Priority"])

@when("user select list all tasks")
def step_when_user_select_listall_tasks(context):
    context.user_tasks = context.todo_list.showTasks

@then("output show all user tasks")
def step_then_output_show_user_tasks(context):
    for row in context.table:
        user_tasks = [str(task.title) for task in context.todo_list.tasks if task.title == row["Task"] and task.priority == row["Priority"]]
        assert user_tasks

# Mark a task as completed
@when("the user marks task {task_title} as completed")
def step_when_user_marked_task(context, task_title):
    context.todo_list.markedTaskCompleted(task_title)

@then("the to-do list should show task {task_title} as completed")
def step_then_todolist_have_task_marked(context, task_title):
    tasks = filter(lambda task: task.title == task_title, context.todo_list.tasks)
    assert tasks

# Clear the entire to-do list
@when("the user clears the to-do list")
def step_when_user_selected_clear_all_tasks(context):
    context.todo_list.clearTasks()

@then("the to-do list should be empty")
def step_then_todo_list_should_be_empty(context):
    assert not context.todo_list.tasks

# Delete Task By Id
@when("the user deletes task {task_title}")
def step_when_user_delete_task(context, task_title):
    task_index = next((index for index, task in enumerate(
        context.todo_list.tasks) if task.title == task_title), None)
    print(task_index)
    if task_index is not None:
        context.todo_list.deleteTask(task_index)

@then("the to-do list should not contain {task_title}")
def step_then_todolist_should_delete_task(context, task_title):
    task = [task for task in context.todo_list.tasks if task.title == task_title]
    assert not task