package com.example.fraud.mapper;

import com.example.fraud.entity.LogData;
import com.example.fraud.entity.LogData_Click_Cnt;
import com.mysql.cj.log.Log;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Param;


import java.time.LocalDateTime;
import java.util.List;

@Mapper
public interface LogDataMapper {
    @Select("SELECT ip_address, COUNT(ip_address) AS cnt FROM Log_Data GROUP BY ip_address")
    List<LogData_Click_Cnt> getIpAndClickCnt();


    @Select("SELECT ip_address, COUNT(ip_address) AS cnt FROM Log_Data WHERE event_time >= #{startTime} AND event_time < #{endTime} GROUP BY ip_address")
    List<LogData_Click_Cnt> getIpAndClickCnt1(@Param("startTime") LocalDateTime startTime, @Param("endTime") LocalDateTime endTime);



}