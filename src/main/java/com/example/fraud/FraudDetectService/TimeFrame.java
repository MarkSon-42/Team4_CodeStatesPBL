package com.example.fraud.FraudDetectService;

import java.time.LocalDateTime;

public class TimeFrame {

    LocalDateTime StartTime;

    //real data
    LocalDateTime EndTime ;

    TimeFrame(){
        this.StartTime = LocalDateTime.now().withSecond(0);
        this.EndTime = StartTime.plusMinutes(1);

    }
}
