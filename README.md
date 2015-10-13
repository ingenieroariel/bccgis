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
