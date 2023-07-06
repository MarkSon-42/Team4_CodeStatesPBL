package com.example.fraud.service;

import com.example.fraud.entity.ADInfo;
import com.example.fraud.mapper.ADInfoMapper;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class ADClickCntService {
    ADInfoMapper adInfoMapper;

    ADClickCntService(ADInfoMapper adInfoMapper){
        this.adInfoMapper = adInfoMapper;
    }

    public int MinusCnt(int ADID){
        adInfoMapper.AddCnt(ADID);

        return(adInfoMapper.SelectCnt(ADID));
    }

    public List<ADInfo> GetAdList(){
        List<ADInfo> result = new ArrayList<>();
        List<ADInfo> mainAd = adInfoMapper.selectMainAD();
        List<ADInfo> subAd = adInfoMapper.selectSubAD();

        result.addAll(mainAd);
        result.addAll(subAd);

        return result;

    }
}
