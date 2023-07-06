package com.example.fraud.FraudDetectService;

import com.example.fraud.entity.LogData_Click_Cnt;
import com.example.fraud.mapper.LogDataMapper;
import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;

@Service
public class GetLogData {

    private final LogDataMapper logDataMapper ;

    GetLogData(LogDataMapper logDataMapper){
        this.logDataMapper = logDataMapper;
    }

    public List<LogData_Click_Cnt> GetLogdata(){

        String dateTimeString = "2023-07-01 10:00:00";
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        LocalDateTime startTime = LocalDateTime.parse(dateTimeString, formatter);


        List<LogData_Click_Cnt> l = logDataMapper.getIpAndClickCnt1(startTime, startTime.plusMinutes(1));
        return l;
    }
}
