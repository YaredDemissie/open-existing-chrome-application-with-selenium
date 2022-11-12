# Open Existing Chrome Application with Selenium
Connects to an existing chrome application

## Motivation
This code is intended to make it possible to run Selenium commands on an existing Chrome browser instead of a new instance of a Chrome Browser. Using an existing Chrome browser make it easier to use featuers such as password completion and page history. It also make it a lot easier to work with two-step authentication which can be difficult to deal with is there is a new browser instance with each code run. 

## Build Status
At the moment this code runs without any bugs.

## Tech/Framework used
Python 3.10.6 

## Features
Once the path to Chrome driver is specified, the code will automatically open the browser. The code also make it possible to utilize environment variables. 

## How to Use?
1. Install Python 3
2. Install pip
3. If you're on Windows, add Google Chrome to your path
4. Download a Chrome Driver that has the same version as your exisiting Chrome Browser. You can check your current Chrome Browser version by doing the following: **Open Chrome -> Settings -> 'About Chrome'.** Chrome Drivers are currently available here: **https://chromedriver.chromium.org/downloads** 
5. Note that most Chrome Browsers are updated automatically so it may be necessary to download a new Chrome Driver if you're planning to use the code over time.  
6. Clone the repository
7. Download Selenium and dotenv using pip
8. Replace **CHROME_DRIVER_PATH** in the code with the path where you've installed your Chrome Driver
9. **Close all Chrome Browser windows that are open**
10. Copy the path for the 'User Data' folder on you machine. For Windows users, it'll be something like the following (Make sure to change PLACE_HOLDER with the username on you machine): **C:\Users\<PLACE_HOLDER>\AppData\Local\Google\Chrome\User Data** For Mac users it will be soemthing like the following (Make sure to change PLACE_HOLDER with the username on you machine): **Users/<PLACE_HOLDER>/Library/Application Support/Google/Chrome/Default**
11. Go to the command line and write the follwing (After replaceing PLACE_HOLDER with the 'User Data' folder path inside of double quotes): **chrome.exe --remote-debugging-port=9250 --user-data-dir=PLACE_HOLDER** For Windows users, it's necessary to add Chrome to the path for this command to work.
12. Run the code by writing **python file.py** in the command line where in the path where the code is located

## Code Style
Standard

## Code Examples
**python file.py** or **python3 file.py**

## Contribute
You may add more features to the program

## API reference
NA

## Tests
NA

## License
MIT