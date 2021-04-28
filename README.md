# Flask - MongoDB

Simple app flask to create and access database from an API

use port : 3500

change IP address to connect to your machine (localhost if monDB is on your machine)

## Route

/ <= home

/all_data <= show all database

/createDB <= create a database

/createDB?dbname=PARAMETER1&colname=PARAMETER2


/show <= show data from spécific database

/show?dbname=PARAMETER1&colname=PARAMETER2

```example : http://52.168.123.57:3500/show?dbname=madb&colname=fakecollection```



