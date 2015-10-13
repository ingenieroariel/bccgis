OSMOSIS=osmosis/bin/osmosis

tellmethedate:
	@echo "hello"
	@date

# Get spatial data for Bangladesh.
bangladesh.pbf:
	curl -o $@ 'http://download.geofabrik.de/asia/bangladesh-latest.osm.pbf'

# Example layer as points
hospitals.pbf: bangladesh.pbf
	$(OSMOSIS) --read-pbf-fast file="$<" --nkv keyValueList="amenity.hospital,amenity.doctors,amenity.doctor,amenity.clinic,amenity.health_post" --write-pbf file="$@"

# Example layer as polygons
schools.pbf: bangladesh.pbf
	$(OSMOSIS) --read-pbf-fast file="$<" --wkv keyValueList="amenity.school,amenity.university,amenity.college,amenity.kindergarten" --used-node --write-pbf file="$@"
