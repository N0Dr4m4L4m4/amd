# Advanced management of data

Here is the repository for the project of advanced management of data.

## Technology
- Python for frontend (desktop application)
- PyQT for user interface
- PostgreSQL for backend processing
- UI-Prototyping could use something like [Figma](https://www.figma.com)
> All processing like validation of input data or algorithm has to be in the backend. The frontend is not able to validate or calculate some user input.  

## Requirements 
- Python 3.9.x
- psycopg2 for connection to postgresql database
- PyQt5 for UI-Elements
- VPN connection to TU Chemnitz (use Cisco client for that)

# First steps
## 1) Install Python, as well as psycopg2 and PyQT5
1. Check your python version with ```python --version``` you should receive something like: ```Python 3.9.5```, otherwise you have to [download](https://www.python.org/downloads/) and install Python first
2. Write down in you console ```pip install psycopg2```
3. Next step is to download the PyQt5 required libaries
4. Write in your console ```pip install pyqt5```
5. Now we have required libary, next step we configure the connection✨

## 2) Configure your database connection
1. Open the database.ini that is in frontend/app/ directory
2. Fill it with your given data at the first tutorial, where you initialized you postgresql database
3. Most of your username is the name of your database concatenate with ```_rw``` e.g. your databases name is ```example``` then your username is ```example_rw```
4. Also fill out your given password but the *host* with ```pgsql.hrz.tu-chemnitz.de``` is always the same
5. Going on to the test the connection to your database

## 3) VPN connection and start the application
1. Start the ```Cisco AnyConnect Secure Mobility Client```, if you haven't set up yet: follow this [instruction](https://www.tu-chemnitz.de/urz/network/access/vpn.html#client)
2. If the VPN connection is done, you can navigate to the project folder to frontend\app
3. Please make sure you are in the right working directory, if not an exception is thrown. It should be something like ```C:\user\amd\frontend\app\```
4. Write into the command line interpreter  ```python welcomeClass.py``` to start the application
5. If you see something the application is working well - _Hint:_ make sure your screen scaling in your computer settings is set to 100%, otherwise the GUI could be too big
6. Firstly, you have to log on with an existing username, otherwise you get the response, that the user doesn't exit. Existing users are: Mats, Axel, Robin, Sabine or Tina.
7. Have fun!
