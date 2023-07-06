package com.example.fraud.entity;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import javax.persistence.Column;

@Getter
@Setter
@ToString
public class LogData_Click_Cnt {
    @Column(name = "ip_address")

    private String ip_address;
    private int cnt;
}
