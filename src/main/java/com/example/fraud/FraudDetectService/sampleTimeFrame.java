package com.example.fraud.FraudDetectService;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class sampleTimeFrame {

    String dateTimeString = "2023-07-01 10:00:00";
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
    LocalDateTime dateTime = LocalDateTime.parse(dateTimeString, formatter);

}
