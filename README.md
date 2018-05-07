# appium-excercise
Sample Framework on Appium using python 2.x

# Install allure as mentioned in below link:
https://docs.qameta.io/allure#_installing_a_commandline

# Run the pytest test using below command
python -m pytest test_purchase_flow.py --alluredir ./results

# To display the report from allure server use below command:
allure serve ./results/

# To display the report from local use below command:
allure generate