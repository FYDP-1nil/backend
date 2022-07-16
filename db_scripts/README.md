### To create the tables locally, run the following 

* Make sure you have Postgres installed. If you don't, use this link to download Postgres.app
* Create a new db called `1nil`, use default configs
* By default, the port number is 5432, if it's different then change it in -p flag below
* Navigate to the db_scripts dir
* Run `/Applications/Postgres.app/Contents/Versions/14/bin/psql -p5432 "1nil"` to login to the psql shell
* Run the command `\i create_tables.sql`
* All done