tellmethedate:
	@echo "hello"
	@date

# Get spatial data for Bangladesh.
bangladesh.pbf:
	curl -o $@ 'http://download.geofabrik.de/asia/bangladesh-latest.osm.pbf'

