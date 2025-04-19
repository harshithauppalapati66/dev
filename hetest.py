from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start browser
driver = webdriver.Chrome()

# Open the running Flask app
driver.get("http://localhost:5000")
time.sleep(1)

# Check the content
assert "Hello Docker" in driver.page_source, "❌ Test Failed: Text not found"
print("✅ Test Passed: Found 'Hello Docker'")

driver.quit()
