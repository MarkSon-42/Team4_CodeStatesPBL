package com.example.fraud.FraudDetectService;

import com.example.fraud.entity.LogData_Click_Cnt;
import com.example.fraud.mapper.BlackListMapper;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class AddToBlackList {
    private final BlackListMapper blackListMapper;

    AddToBlackList(BlackListMapper blackListMapper){
        this.blackListMapper = blackListMapper;
    }

    public void FindFraudAndAddToBlackList(List<LogData_Click_Cnt> l){
        for(int i=0; i<l.size(); i++){
            if (l.get(i).getCnt() >= 500){
                blackListMapper.addBlackList(l.get(i).getIp_address());
                System.out.println("Add BlackList : ip address ===== " + l.get(i).getIp_address());
            }
        }
    }
}
