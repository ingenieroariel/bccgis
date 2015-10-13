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
