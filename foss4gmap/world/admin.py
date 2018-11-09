from django.contrib.gis import admin
from .models import WorldBorder, Suinanjiko
from leaflet.admin import LeafletGeoAdmin

class BorderAdmin(LeafletGeoAdmin):
  search_fields = ['name','fips','iso2', 'iso3']
  list_filter = ('name', )

class SuinanjikoAdmin(LeafletGeoAdmin):
  search_fields = ['jiko','pref','river']
  list_filter = ('pref', )

# admin.site.register(WorldBorder, admin.GeoModelAdmin)
#admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(WorldBorder, BorderAdmin)
admin.site.register(Suinanjiko, SuinanjikoAdmin)
