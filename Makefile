OSMOSIS=osmosis/bin/osmosis

# Get spatial data for Bangladesh.
bangladesh.pbf:
	curl -o $@ 'http://download.geofabrik.de/asia/bangladesh-latest.osm.pbf'

buildings.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<"  --tf accept-ways "building=*"  --write-pbf file="$@"

bridges.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<"  --tf accept-ways "bridge=*"  --write-pbf file="$@"

idp_camps.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --wkv keyValueList="idp:camp_site=spontaneous_camp,damage:event.dominica_earthquake_2015" --used-node  --write-pbf  file="$@"

huts.pbf: buildings.pbf
	osmosis --read-pbf-fast file="$<" --tf accept-ways "building=hut" --used-node --write-pbf file="$@"

trees.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --tf accept-nodes "natural=tree" --tf reject-ways --tf reject-relations --write-pbf file="$@"

schools_point.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --nkv keyValueList="amenity.school,amenity.university,amenity.college,amenity.kindergarten" --write-pbf file="$@"

schools_polygon.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --wkv keyValueList="amenity.school,amenity.university,amenity.college,amenity.kindergarten" --used-node --write-pbf file="$@"

medical_point.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --nkv keyValueList="amenity.hospital,amenity.doctors,amenity.doctor,amenity.clinic,amenity.health_post" --write-pbf file="$@"

medical_polygon.pbf: buildings.pbf
	osmosis --read-pbf-fast file="$<" --wkv keyValueList="amenity.hospital,amenity.doctors,amenity.doctor,amenity.clinic,amenity.health_post" --used-node --write-pbf file="$@"
  
roads.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<"  --tf accept-ways "highway=*" --used-node --write-pbf file="$@"

rivers.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --wkv keyValueList="waterway.river,waterway.stream,waterway.ditch" --used-node --write-pbf file="$@"
  
riverbanks.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --wkv keyValueList="waterway.riverbank" --used-node --write-pbf file="$@"

lakes.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --wkv keyValueList="natural.water,water.lake" --used-node --write-pbf file="$@"
 
beaches.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --wkv keyValueList="natural.beach" --used-node --write-pbf file="$@"

farms.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --wkv keyValueList="landuse.farm,landuse.farmland,landuse.farmyard" --used-node --write-pbf file="$@"
 
forest.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --wkv keyValueList="landuse.forest" --used-node --write-pbf file="$@"
 
grassland.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --wkv keyValueList="landuse.grass,landuse.grassland,natural.wood,natural.grassland" --used-node --write-pbf file="$@"
 
military.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<"  --tf accept-ways "landuse=military" --used-node --write-pbf file="$@"
 
orchards.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<"  --tf accept-ways "landuse=orchard" --used-node --write-pbf file="$@"

residential.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<"  --tf accept-ways "landuse=residential" --used-node --write-pbf file="$@"

village_green.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<"  --tf accept-ways "landuse=village_green" --used-node --write-pbf file="$@"

wetlands.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<"  --tf accept-ways "landuse=wetland" --used-node --write-pbf file="$@"

cities.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<"  --tf accept-nodes "place=city" --tf reject-ways --tf reject-relations --write-pbf file="$@"

hamlets.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<"  --tf accept-nodes "place=hamlet" --tf reject-ways --tf reject-relations  --write-pbf file="$@"

neighborhoods.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --nkv keyValueList="place.neighborhood,place.neighbourhood" --tf reject-ways --tf reject-relations  --write-pbf file="$@"

villages.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<"  --tf accept-nodes "place=village" --tf reject-ways --tf reject-relations --write-pbf file="$@"

placenames.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --nkv keyValueList="place.city,place.hamlet,place.neighborhood,place.neighbourhood,place.village" --tf reject-ways --tf reject-relations --write-pbf file="$@"


all_roads.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --wkv keyValueList="highway.unclassified,highway.tertiary,highway.residential,highway.service,highway.secondary,highway.track,highway.footway,highway.path,highway.classified,highway.primary,highway.trunk,highway.motorway,highway.construction,highway.proposed,highway.cycleway,highway.living_street,highway.steps,highway.road,highway.pedestrian,highway.construction,highway.bridleway,highway.platformhighway.proposed" --used-node --write-pbf file="$@"

main_roads.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --wkv keyValueList="highway.motorway,highway.trunk,highway.primary" --used-node --write-pbf file="$@"

paths.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --wkv keyValueList="highway.path,highway.trunk,highway.primary" --used-node  --write-pbf file="$@"

tracks.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<"  --wkv keyValueList="highway.track" --used-node --write-pbf file="$@"

aerodromes_point.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --nkv keyValueList="aeroway.aerodrome,aeroway.international" --write-pbf file="$@"

aerodromes_polygon.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<"  --wkv keyValueList="aeroway.aerodrome,aeroway.international" --used-node --write-pbf file="$@"

banks.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --tf accept-nodes "amenity=bank" --tf reject-ways --tf reject-relations --write-pbf file="$@"

fire_stations.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --tf accept-nodes "amenity=fire_station" --tf reject-ways --tf reject-relations  --write-pbf file="$@"

hotels.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --nkv keyValueList="tourism.hotel,amenity.hotel" --tf reject-ways --tf reject-relations  --write-pbf file="$@"

police_stations.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --nkv keyValueList="amenity.police,tourism.police" --tf reject-ways --tf reject-relations  --write-pbf file="$@"

restaurants.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --nkv keyValueList="amenity.restaurant,amenity.restaurants" --tf reject-ways --tf reject-relations --write-pbf file="$@"

train_stations.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --tf accept-nodes "railway=station" --tf reject-ways --tf reject-relations  --write-pbf file="$@"

helipads.pbf: bangladesh.pbf
	osmosis --read-pbf-fast file="$<" --wkv keyValueList="aeroway.helipad" --used-node --write-pbf file="$@"

PBF_EXPORTS = buildings.pbf schools_point.pbf schools_polygon.pbf medical_point.pbf medical_polygon.pbf rivers.pbf riverbanks.pbf lakes.pbf farms.pbf forest.pbf grassland.pbf military.pbf orchards.pbf residential.pbf cities.pbf hamlets.pbf neighborhoods.pbf villages.pbf placenames.pbf all_roads.pbf main_roads.pbf paths.pbf tracks.pbf aerodromes_point.pbf aerodromes_polygon.pbf banks.pbf hotels.pbf police_stations.pbf restaurants.pbf train_stations.pbf helipads.pbf

all: $(PBF_EXPORTS)

.PHONY: clean
clean:
	rm -rf *.pbf
