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
- VPN connection to TU Chemnitz (use Cisco client for that)

# First steps
## 1) Install psycopg2
1. Check your python version with ```python --version``` you should receive something like: ```Python 3.9.5```
2. Write down in you console ```pip install psycopg2```
3. Now we have required libary, next step we configure the connection✨

## 2) Configure your database connection
1. Open the database.ini 
2. Fill it with your given data at the first tutorial, where you initialized you postgresql database
3. Most of your username is the name of your database concatenate with ```_rw``` e.g. your databases name is ```example``` then your username is ```example_rw```
4. Also fill out your given password but the *host* with ```pgsql.hrz.tu-chemnitz.de``` is always the same
5. Going on to the test the connection to your database 🚀

## 3) VPN connection and connection test
1. Start the ```Cisco AnyConnect Secure Mobility Client```, if you haven't set up yet: follow this [instruction](https://www.tu-chemnitz.de/urz/network/access/vpn.html#client)
2. If the VPN connection is stable, you can navigate to the project folder and start the ```connection.py``` with ```python connection.py``` 
3. If everything is configured right you are getting a console output about:
  >Connecting to the PostgreSQL database...\
  PostgreSQL database version:\
  ('PostgreSQL 13.5 (Debian 13.5-1.pgdg100+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 8.3.0-6) 8.3.0, 64-bit',)\
  Database connection closed.
4. 🎇🎆Heureka!! You configured the database connection successfully 🎆🎇

