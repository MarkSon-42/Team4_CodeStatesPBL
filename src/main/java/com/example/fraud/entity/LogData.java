package com.example.fraud.entity;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import java.sql.Timestamp;
import java.time.LocalDateTime;


@Setter
@Getter
@ToString
public class LogData {

    private Timestamp event_time;
    private boolean is_click;
    private boolean is_view;
    private boolean is_slide;
    private int user_id;
    private int ad_id;
    private String ip_address;

}
