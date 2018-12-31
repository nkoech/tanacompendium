from django.contrib import admin

# Register your models here.
from .models import (WaterQuality,)


class WaterQualityModelAdmin(admin.ModelAdmin):
    """
    Water quality model admin settings
    """
    list_display = ['record_date', 'julian_day', 'day_frac', 'temperature', 'ph_units', 'stream_depth',
                    'sp_cond', 'turbidity_ntu', 'ph_mv', 'salinity_ps', 'comment', 'last_update', 'modified_by']
    list_display_links = ['record_date', 'stream_depth']
    list_filter = ['record_date', 'julian_day', 'stream_depth', 'turbidity_ntu', 'last_update', 'modified_by']

    class Meta:
        model = WaterQuality


admin.site.register(WaterQuality, WaterQualityModelAdmin)


