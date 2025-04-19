from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Update the path to your local HTML file
file_path = "file:///C:/test-app/index.html"  # Change this path based on your OS

# Start Chrome
driver = webdriver.Chrome()  # Assumes chromedriver is in PATH
driver.get(file_path)

# Enter numbers
driver.find_element(By.ID, "num1").send_keys("3")
driver.find_element(By.ID, "num2").send_keys("4")

# Click add
driver.find_element(By.ID, "addBtn").click()

# Wait for result
time.sleep(1)

# Check result
result = driver.find_element(By.ID, "result").text
assert result == "7", f"Test Failed: Expected 7 but got {result}"
print("✅ Test Passed: 3 + 4 = 7")

# Close browser
driver.quit()
