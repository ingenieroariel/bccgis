# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.contrib.postgres.fields import HStoreField

class AerodromesPoint(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.PointField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    highway = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_in = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aerodromes_point'


class AerodromesPolygon(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.MultiPolygonField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aerodromes_polygon'


class Road(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.LineStringField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    highway = models.CharField(max_length=255, blank=True, null=True)
    waterway = models.CharField(max_length=255, blank=True, null=True)
    aerialway = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all_roads'


class Bank(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.PointField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    highway = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_in = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banks'


class Building(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.MultiPolygonField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buildings'


class City(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.PointField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    highway = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_in = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities'
        verbose_name_plural = 'cities'


class Farm(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.MultiPolygonField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farms'


class Forest(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.MultiPolygonField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forest'


class Grassland(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.MultiPolygonField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grassland'


class Hamlet(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.MultiPolygonField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    highway = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_in = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hamlets'


class Helipad(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.MultiPolygonField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'helipads'


class Hotel(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.PointField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    highway = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_in = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotels'


class Lake(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.MultiPolygonField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lakes'


class MedicalPoint(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.PointField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    highway = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_in = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medical_point'


class MedicalPolygon(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.MultiPolygonField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medical_polygon'


class Military(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.MultiPolygonField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'military'


class Neighborhood(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.MultiPolygonField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    highway = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_in = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'neighborhoods'


class Orchard(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.MultiPolygonField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orchards'


class Path(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.LineStringField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    highway = models.CharField(max_length=255, blank=True, null=True)
    waterway = models.CharField(max_length=255, blank=True, null=True)
    aerialway = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paths'


class Placename(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.PointField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    highway = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_in = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'placenames'


class PoliceStation(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.PointField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    highway = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_in = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'police_stations'


class Residential(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.MultiPolygonField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'residential'


class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.PointField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    highway = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_in = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurants'


class Riverbank(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.MultiPolygonField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'riverbanks'


class River(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.LineStringField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    highway = models.CharField(max_length=255, blank=True, null=True)
    waterway = models.CharField(max_length=255, blank=True, null=True)
    aerialway = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rivers'


class SchoolPoint(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.PointField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    highway = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_in = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schools_point'


class SchoolPolygon(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.MultiPolygonField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schools_polygon'


class Track(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.LineStringField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    highway = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_in = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tracks'


class TrainStation(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.PointField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    highway = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_in = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'train_stations'


class VillageGreen(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.MultiPolygonField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'village_green'


class Village(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.PointField(db_column='wkb_geometry', blank=True, null=True)
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    highway = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_in = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    other_tags = HStoreField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'villages'
