### 	coincap-data is software designed to:
###
###		Pull coin data
###		using data from coinmarketcap.com API	
###		for the top 100 coins
###		and enter it into a mySQL database
###
###
### 	Pre-requisites include: 
###	
###		1. A working mySQL database
###		2. A user with access to said database
###		3. A table in the database with the correct fields
###		4. Pip installed (see below)
###		5. mysql.connector installed (via pip, see below)
###
###
###	Some helpful SQL scripts can be found in the "SQL_scripts" file
###
###
###	To install pip and the mysql.connector lib:
####		1. Command to install pip
####			NEED TO ADD THIS
###		2. Command to install mysql.connector
###			'pip install mysql-connector'
###
###
###	Copyright 2017, Chris Becin
###
###	This file is part of coincap-data.
###
###	coincap-data is free software: you can redistribute it and/or modify
###	it under the terms of the GNU General Public License as published by
###	the Free Software Foundation, either version 3 of the License, or
###	(at your option) any later version.
###
###	coincap-data is distributed in the hope that it will be useful,
###	but WITHOUT ANY WARRANTY; without even the implied warranty of
###	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
###	GNU General Public License for more details.
###
###	You should have received a copy of the GNU General Public License
###	along with coincap-data.  If not, see <http://www.gnu.org/licenses/>.
###
###	The author cannot be held accountable for lost data, broken machines, 
###	gaping memory holes, lost time, or any other consequences of using 
###	this software.
###
###	Use at your own risk!
###
###



## User-defined variables (your input goes here)

# Define mySQL variables

mysql_host = 'MYSQL HOST IP HERE'
mysql_user = 'MYSQL USERNAME HERE'
mysql_password = 'MYSQL PASSWORD HERE'
mysql_database = 'MYSQL DATABASE HERE'
mysql_table = 'MYSQL TABLE HERE'

# Define how many coins to track (at time of writing, max around 800-850)

trackCount = 100


# Define how often to reload data in seconds (the site updates ~5 min)

numSeconds = 150

# Set to True for Silent Mode (default is to be noisy)

silentMode = False


## That's all folks - you don't need to define anything else




## Import all the libs

# Import libs to deal with URL, JSON, datetime

import urllib, json
import datetime 
import time


# Import libs to deal with mysql
# Note: mysql.connector must be instaled via pip

import mysql.connector


# Import library which can print parsed data

from pprint import pprint


### Testing: print the formatted output for testing

##pprint(data)



## Define a function to do all of this once in a while

def update():



## Pull down the JSON data from the URL, parse, and save to variable

# Define the URL to pull from

	url = "https://api.coinmarketcap.com/v1/ticker/?limit=" 

	maxRank = trackCount + 1
	
	rankStr = str(( maxRank - 1 ))
	
	strUrl = format(url, rankStr)

		
# Grab the data
	
	response = urllib.urlopen(strUrl)
	

# Read the data as a JSON object

	data = json.loads(response.read())


# Store values in python variable

	for i in range(0, maxRank-1):

		price_usd = data[i]["price_usd"]
		rank = data[i]["rank"]
		symbol = data[i]["symbol"]
		coin_id = data[i]["id"]
		volume_usd = data[i]["24h_volume_usd"]
		available_supply = data[i]["available_supply"]
		name = data[i]["name"]
		percent_change_1h = data[i]["percent_change_1h"]
		percent_change_24h = data[i]["percent_change_24h"]
		percent_change_7d = data[i]["percent_change_7d"]
		price_btc = data[i]["price_btc"]


# Make last_updated to mysql-friendly YYYY-MM-DD HH:MM:SS format

		last_updated = datetime.datetime.fromtimestamp(int(data[i]["last_updated"])).strftime('%Y-%m-%d %H:%M:%S')


# Define the full dataset as a variable (in SQL table column order

	 	dataset = (price_usd, rank, symbol, coin_id, volume_usd, available_supply, last_updated, name, percent_change_1h, percent_change_24h, percent_change_7d, price_btc)


# Print the values to make sure we are getting the right data

		if silentMode == False:
		
			print (dataset)
 
 

### Connect to MySQL and input data to table


## Connect to the database

		cnx = mysql.connector.connect(
		
		user = mysql_user, 
		password = mysql_password ,  
		host = mysql_host, 
		database = mysql_database )


# Set a cursor in the database to let us update it

		cursor = cnx.cursor()


## INSERT data into MySQL
		
# Define a few pieces of the SQL INSERT statement

		insert_into = "INSERT IGNORE INTO "				

		insert_fields = " (price_usd, rank, symbol, coin_id, volume_usd, available_supply, last_updated, name, percent_change_1h, percent_change_24h, percent_change_7d, price_btc) "
		
		insert_values =	"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"


# Combine the pieces into a single SQL statement

		add_data = insert_into + mysql_table + insert_fields + insert_values
		

# Do the INSERTing

		cursor.execute(add_data, (dataset))

                      
## Commit that shit, close the cursor & connection

		cnx.commit()
		cursor.close()
		cnx.close()



## Restart the whole thing every so often

	time.sleep(numSeconds)


## This loop will keep it alive forever

while True:

	update()
