 1. Open terminal: Look for terminal in the menu

 2. Check the date 
  ```
  date
  ```

 3. Create a folder called 'code'
 
  ```
  mkdir code
  ls
  ```
 4. Go into the folder and check that it is empty
 
  ```
  cd code
  ls
  ```
  
 5. Check that make is installed
 ```
 make
 ```
 6. Create a new makefile
 ```
 gedit Makefile
 ```
 7. Put a sample task in the makefile
 
 ```
 tellmethedate:
	    date
 ```
 8. Download data from OpenStreetMap for Bangladesh
 
 ```
bangladesh.pbf:
     curl -o $@ 'http://download.geofabrik.de/asia/bangladesh-latest.osm.pbf'
 ```
 
 9. Install QGIS in order to open the file
 ```
 sudo apt-get install qgis
 ```
 
 10. This file is too big, we have to make it smaller first before being able to open it in QGIS
 ```
 sudo apt-get install openjdk-7-jre
 wget http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.zip
 ```
 
 11. Unzip osmosis
 ```
 mkdir osmosis
 cd osmosis
 unzip ../osmosis-latest.zip
 ```

 12. Clone this repository
 ```
 sudo apt-get install git
 git clone https://github.com/ingenieroariel/bccgis.git
 ``` 

 13. Delete your files in the code folder that are not osmosis or bccgis.

 14. Move the osmosis folder in the bccgis folder.

 15. Every time you want to update your local copy, run the following:
 ```
 git pull
 ```

 16. To add hospitals and restaurants in QGIS, Click on add layers, then select All Files and locate the pbf you want to open. If you do not know whether it has points, polygons or lines, click on select all, and then delete the layers that are empty.

 17. To create all the layers ( schools, rivers, restaurants, roads), make sure to do a git pull again and then type:

 ```
 make clean
 make
 ```

 At this point the computer will start to download the country file for Bangladesh and extract all the important layers one by one. It will take about ten minutes and it is the perfect time to go and have tea.

 18. Export banks as an ESRI Shapefile using QGIS. Put it in a folder called export.

 19. Let's get a spatial database setup
 ```
 sudo apt-get install postgresql-9.3-postgis-2.1
 ```

 20. Create bcc database
 ```
 sudo su - postgres
 createuser -s bcc
 createdb -O bcc bcc
 \q
 exit
 ```

 21. Add postgis and hstore extensions to be able to load spatial data
 ```
 psql bcc
 CREATE EXTENSION postgis;
 CREATE EXTENSION hstore;
 \q
 ```

 22. Export sql using shp2pgsql
 ```
 cd ~/code/bccgis/export
 shp2pgsql banks.shp >> banks.sql
 ```

 23. Load the sql on the database.
 ```
 psql bcc -f banks.sql
 ```

 24. Check how many banks are in the database:
  ```
 psql bcc
 SELECT count(*) from banks;
 \q
 ```

 25. Get the first bank

 ```
 SELECT osm_id, name, geom FROM banks LIMIT 1;
 SELECT osm_id, name, ST_AsEWKT(geom) FROM banks LIMIT 1;
 ```

 26. Get all the banks that are one kilometer away from BCC

 ```
 SELECT * FROM banks 
  WHERE ST_DWithin(geom, 'POINT(90.374281 23.7784036)', 0.01);
 ```

 27. Update your code, and run make all to insert all the different tables in the database.

 28. Install pgadmin3 to access your database with a handy UI.

 ```
 sudo apt-get install pgadmin3
 ```
 
 29. Set a password for the bcc user.

 ```
 psql bcc
 ALTER ROLE bcc WITH PASSWORD 'bcc';
 \q
 ```

 30. Open pgadmin3 from the menu and connect to the server at localhost. Open the bcc database and navigate to the list of tables in the public schema until you see the bank table. Right click on that table and click on View Data -> View Top 100 Rows.

 31. Install python-pip before you can install Django

 ```
 sudo apt-get install python-pip
 sudo pip install Django
 ```

 32. Run the web server on the bccdjango project.
 In order to create this application, we ran django-admin startproject bccdjango in the teacher computer and then pushed the results to github.

 ```
 cd bccdjango
 python manage.py runserver
 ```
 Navigate to the web browser in the following url:
 http://localhost:8000/

 33. Now try to access the list of banks:
 We used python manage.py inspectdb to create a models.py file with information about banks and other type of layers and created a new app called osm using python manage.py startapp osm.

 ```
 git pull
 ``` 
 http://localhost:8000/banks

 34. Update the postgres python adapter:

 ```
 sudo apt-get install libpq-dev python-dev
 sudo pip install -U psycopg2 ipython
 ```
 35. Use the shell to iterate over bank names:

 ```
 python manage.py shell
 from osm.models import Bank

 Bank.objects.all().count()

 for bank in Bank.objects.all():
     print bank.name, bank.geom.x, bank.geom.y
 ```

 36. Install django-leaflet and django-geojson to be able to create a map.

 ```
 sudo pip install django-leaflet django-geojson
 ```
































