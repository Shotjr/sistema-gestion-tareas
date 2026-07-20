from selenium import webdriver

def test_create_task_ui():
    driver = webdriver.Chrome()
    driver.get("http://localhost:5000/login")
    driver.find_element("id","username").send_keys("juan")
    driver.find_element("id","password").send_keys("123")
    driver.find_element("id","login-btn").click()
    driver.find_element("id","new-task").click()
    driver.find_element("id","title").send_keys("Tarea automática")
    driver.find_element("id","save-btn").click()
    assert "Tarea automática" in driver.page_source
    driver.quit()
