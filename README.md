'# coincap-data

coincap-data is software designed to:

	Pull coin data
	using data from coinmarketcap.com API	
	for the top 100 coins
	and enter it into a mySQL database


Pre-requisites include: 

	1. A working mySQL database
	2. A user with access to said database
	3. A table in the database with the correct fields
	4. Pip installed (see below)
	5. mysql.connector installed (via pip, see below)


Some helpful SQL scripts can be found in the "SQL_scripts" file


To install pip and the mysql.connector lib:
	1. Command to install pip
		'sudo apt-get install pip'
	2. Command to install mysql.connector
		'pip install mysql-connector'


Copyright 2017, Chris Becin

This file is part of coincap-data.

coincap-data is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

coincap-data is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with coincap-data.  If not, see <http://www.gnu.org/licenses/>.

The author cannot be held accountable for lost data, broken machines, 
gaping memory holes, lost time, or any other consequences of using 
this software.

Use at your own risk!


