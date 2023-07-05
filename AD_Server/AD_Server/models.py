from django.db import models


class AdInfo(models.Model):
    media_type = models.ForeignKey('MediaTypeInfo', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    mod_date = models.DateTimeField(blank=True, null=True)
    definition = models.CharField(max_length=500, blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    advertiser = models.CharField(max_length=45, blank=True, null=True)
    click_cnt = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    content_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AD_Info'



class Blacklist(models.Model):
    ipaddress = models.CharField(primary_key=True, max_length=45)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BlackList'