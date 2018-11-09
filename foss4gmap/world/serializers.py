from rest_framework_gis import serializers
from world.models import WorldBorder, Suinanjiko

class WorldBorderSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = WorldBorder
        geo_field = 'mpoly'
        fields = (
            'name',
            'area',
            'pop2005',
            'fips',
            'iso2',
            'iso3',
            'un',
            'region',
            'subregion',
            'lon',
            'lat',
        )

class SuinanjikoSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = Suinanjiko
        geo_field = 'geom'
        fields = ('__all__')
