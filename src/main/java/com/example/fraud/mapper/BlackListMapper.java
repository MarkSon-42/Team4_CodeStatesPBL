package com.example.fraud.mapper;

import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

@Mapper
public interface BlackListMapper {
    @Insert("INSERT INTO BlackList (ipaddress) VALUES ('${ipaddress}') ON DUPLICATE KEY UPDATE ipaddress = '${ipaddress}'")
    void addBlackList(@Param("ipaddress") String ipaddress);
}
