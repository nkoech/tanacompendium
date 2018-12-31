# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from tanacompendium.utils.abstractmodels import (
    AuthUserDetail,
    CreateUpdateTime,
)
from tanacompendium.utils.createslug import create_slug
from tanacompendium.utils.modelmanagers import (
    model_foreign_key_qs,
    model_type_filter,
    get_year_choices,
    get_datetime_now,
)
from datetime import datetime
from decimal import Decimal
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse


class WaterQuality(AuthUserDetail, CreateUpdateTime):
    """
    Water quality model
    """
    record_date = models.DateTimeField(unique=True, default=datetime.now)
    julian_day = models.SmallIntegerField()
    day_frac = models.DecimalField(max_digits=7, decimal_places=3, default=Decimal('0.0'), verbose_name='Fraction of Day')
    temperature = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, default=Decimal('0.0'), verbose_name='FTemperature (°C)')
    ph_units = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, default=Decimal('0.0'))
    stream_depth = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, default=Decimal('0.0'))
    sp_cond = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=Decimal('0.0'), verbose_name='Specific Conductance (uS/cm)')
    turbidity_ntu = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, default=Decimal('0.0'))
    ph_mv = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True, default=Decimal('0.0'))
    salinity_ps = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, default=Decimal('0.0'), verbose_name='Potential Soil Salinity')
    comment = models.TextField(blank=True, null=True)

    def __unicode__(self):
        str_format = '{0}'.format(self.record_date)
        return str_format

    def __str__(self):
        str_format = '{0}'.format(self.record_date)
        return str_format

    class Meta:
        ordering = ['-time_created', '-last_update']
        verbose_name_plural = 'Water Quality'



