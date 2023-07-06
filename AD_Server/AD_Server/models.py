from django.db import models


# --------광고 정보를 저장하는 모델--------
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
    # 광고주 클릭 수 
    url = models.CharField(max_length=255, blank=True, null=True)
    # 광고와 연결된 URL
    content_path = models.CharField(max_length=255, blank=True, null=True)
    # 광고와 연결된 콘텐츠 파일의 경로를 나타냄
    
    
    
    
    class Meta:
        managed = False
        # 'managed'를 False로 설정하여 Django가 이 모델에 대한 
        # 데이터베이스 테이블 생성 및 삭제를 관리하지 않도록 함
        db_table = 'AD_Info'
        # 모델의 데이터가 저장될 데이터베이스 테이블의 이름을 지정




# -------- 블랙 리스트에 IP 주소를 저장하는 모델 --------

class Blacklist(models.Model):
    ipaddress = models.CharField(primary_key=True, max_length=45)
    # 아이피 주소를 나타내며, 이 모델의 PK로 설정됨.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BlackList'