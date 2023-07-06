package com.example.fraud.mapper;

import com.example.fraud.entity.ADInfo;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;

import java.util.List;

@Mapper
public interface ADInfoMapper {

    @Update("UPDATE AD_Info SET click_cnt = click_cnt - 1 WHERE id = '${adid}'")
    void AddCnt(@Param("adid") int adid);
    @Select("Select click_cnt from AD_Info where '${adid}'")
    int SelectCnt(@Param("adid") int adid);

    //메인 AD를 랜덤으로 1개 가져오는 쿼리
    @Select("Select * from AD_Info join Media_Type_Info on AD_Info.media_type_id=1 where type = \"main\" order by rand() limit 1")
    List<ADInfo> selectMainAD();

    @Select("Select * from AD_Info join Media_Type_Info on AD_Info.media_type_id=3 where type = \"sub\" order by rand() limit 3")
    List<ADInfo> selectSubAD();
}
