package com.example.fraud.FraudDetectService;

import com.example.fraud.FraudDetectService.AddToBlackList;
import com.example.fraud.FraudDetectService.GetLogData;
import com.example.fraud.entity.LogData_Click_Cnt;
import com.example.fraud.mapper.LogDataMapper;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;

@Service
public class DetectFraudService {
    private final LogDataMapper logDataMapper;
    private final AddToBlackList addToBlackList;
    private final GetLogData getLogData;


    public DetectFraudService(AddToBlackList addToBlackList, LogDataMapper logDataMapper, GetLogData getLogData){
        this.logDataMapper = logDataMapper;
        this.addToBlackList = addToBlackList;
        this.getLogData = getLogData;
    }

    @Scheduled(fixedRate = 60000)
    public void FraudDetect(){

        addToBlackList.FindFraudAndAddToBlackList(getLogData.GetLogdata());

    }
}