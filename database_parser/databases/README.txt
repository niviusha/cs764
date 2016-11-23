The .csv file correspond to the tables in the databases.
The database was obtained from: http://openflights.org/data.html
The database into which the table data was imported was named dummy.
Commands use to create the table and then import it into the database:

For the airport table:

create table Airport (id int primary key, name varchar(200), city varchar(200), country varchar(200), iata char(20), icao char(20), latitude decimal(8,7), longitude decimal(8,7), altitude decimal(7,6), timezone decimal(4,3), dst char(20), tz varchar(200));

mysqlimport --fields-terminated-by=, --local -u root -p dummy airport.csv

For the airline table:

create table Airline( id int primary key, name varchar(200), alias varchar(200), iata char(20), icao char(20), callsign varchar(200), country varchar(200), active char(20));

mysqlimport --fields-terminated-by=, --local -u root -p dummy airline.csv

For the route table:

create table Route( airline char(20), airline_id int, source_airport char(20), source_id int, dest_airport char(20), dest_id int, codeshare char(20), stops int, equipment int, foreign key (airline_id) references airline(id), foreign key (source_id) references airport(id), foreign key (dest_id) references airport(id));

mysqlimport --fields-terminated-by=, --local -u root -p dummy route.csv
