Feature: Todo List Management App
    Scenario: Add a task to the to-do list
        Given the to-do list is empty
        When the user adds a task "Buy groceries" with priority "High"
        Then the to-do list should contain "Buy groceries" with priority "High"

    Scenario: List all tasks in todo list
        Given the to-do list contains tasks
        | Task          | Priority |
        | Buy groceries | High     |
        | Pay bills     | Medium   |
        | Running       | Low      |
        When user select list all tasks
        Then output show all user tasks
        | Task          | Priority |
        | Buy groceries | High     |
        | Pay bills     | Medium   |
        | Running       | Low      |

    Scenario: Mark a task as completed
        Given the to-do list contains tasks
        | Task          | Priority | Status  |
        | Buy groceries | High     | Pending |
        When the user marks task "Buy groceries" as completed
        Then the to-do list should show task "Buy groceries" as completed
    
    Scenario: Clear the entire to-do list
        Given the to-do list contains tasks
        | Task          | Priority |
        | Buy groceries | High     |
        | Pay bills     | Medium   |
        | Running       | Low      |
        When the user clears the to-do list
        Then the to-do list should be empty

    Scenario: Delete a task from the to-do list
        Given the to-do list contains tasks
        | Task          | Priority |
        | Buy groceries | High     |
        | Pay bills     | Medium   |
        | Running       | Low      |
        When the user deletes task "Buy groceries"
        Then the to-do list should not contain "Buy groceries"