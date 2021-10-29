# UPES Blackboard Ultra Automation using Python Selenium (For MacOS)

This is a small script written in python to automate the class login for students and teachers of UPES. This script helps us in:

1. Getting the classes list which are scheduled that particular day.
2. Help us to login into the UPES Blackboard Ultra

#
## How to run this script ?

1. Install Latest [Chrome Driver](!https://chromedriver.chromium.org/downloads) on your MAC and copy it to the path below

```
/usr/local/bin
```

2. Download the files from the repositry and add the paths of chromedriver and Chrome_Profile directory in script.py

```
33   chromedriver_path =  "/usr/local/bin/chromedriver"

39   options.add_argument("user-data-dir=/path_to_Chrome_Profile")
```

3. Add your BB Login credentials in script.py.
```
55    driver.find_element_by_id("user_id").send_keys("SAP@stu.upes.ac.in")

56    driver.find_element_by_id("password").send_keys("SAP_PASSWORD")
```

4. Configure the paths inside class.sh as well.

5. Give permissions to class.sh by
```
chmod 755 class.sh
```

6. Execute the below command to run the new class commands
```
source ./class.sh
```

7. Now you can get the menu for the script using the below commands.
```
class -h
class help
```
#
## NOTE:

1. We need to give permissions for the chromedriver for the first time in **system Preferences**

2. We need to accept cookies and allow permissions inside chrome for the first time of the script. And from next time, the Chrome_Profile directory stores the cookies 
