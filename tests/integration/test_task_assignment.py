def test_assign_task_to_user(db, client):
    user = create_user("maria")
    task = create_task("Revisar informe")
    assign_task(user, task)
    assert task.assigned_to == user.id
