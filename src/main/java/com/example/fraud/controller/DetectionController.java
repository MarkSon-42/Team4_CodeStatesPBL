package com.example.fraud.controller;

import com.example.fraud.FraudDetectService.DetectFraudService;
import com.example.fraud.entity.ADInfo;
import com.example.fraud.entity.LogData;
import com.example.fraud.service.ADClickCntService;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import java.util.List;

@RestController
@RequestMapping("/detection")
public class DetectionController {
    DetectFraudService detectFraudService;
    ADClickCntService adClickCntService;

    public DetectionController(DetectFraudService detectFraudService, ADClickCntService adClickCntService){

        this.detectFraudService = detectFraudService;
        this.adClickCntService = adClickCntService;

    }

    @PostMapping("/fraud")
    public boolean FraudDetect(HttpServletRequest request){
        String ipAddress = request.getRemoteAddr();
        detectFraudService.FraudDetect();
        return true;
    }

    @GetMapping("/hit")
    public int ogData(@RequestParam int adid){
        return(adClickCntService.MinusCnt(adid));
    }
    @GetMapping("/ADList")
    public List<ADInfo> GetAdList(){
        return adClickCntService.GetAdList();
    }
}
