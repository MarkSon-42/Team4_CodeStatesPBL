from django.db import models
# 광고 정보를 저장하는 모델
# 데이터베이스의 테이블을 나타낸다.

class AdInfo(models.Model):
    media_type = models.ForeignKey('MediaTypeInfo', models.DO_NOTHING, blank=True, null=True)
    # FK는 모델과의 관계를 생성하는 데 사용됨.
    # AnInfo 인스턴스당 하나의 media_type과의 일대다 관계를 나타낸다.

    name = models.CharField(max_length=45, blank=True, null=True)
    # CharField는 최대길이가 45인 문자열을 저장하는데 사용, 광고의 이름을 나타냄.

    start_date = models.DateTimeField(blank=True, null=True)
    # 광고 시작일
    end_date = models.DateTimeField(blank=True, null=True)
    # 광고 종료일
    mod_date = models.DateTimeField(blank=True, null=True)
    # 광고의 마지막 수정일
    definition = models.CharField(max_length=500, blank=True, null=True)
    # 광고의 설명
    cost = models.IntegerField(blank=True, null=True)
    # 광고 비용
    advertiser = models.CharField(max_length=45, blank=True, null=True)
    # 광고주 이름
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