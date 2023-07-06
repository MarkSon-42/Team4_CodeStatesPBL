package com.example.fraud.entity;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import org.springframework.web.bind.annotation.GetMapping;

import javax.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "AD_Info")
@Getter
@Setter
@ToString
public class ADInfo {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "media_type_id")
    private Integer media_type_id;

    private String name;

    @Column(name = "start_date")
    private LocalDateTime startDate;

    @Column(name = "end_date")
    private LocalDateTime endDate;

    @Column(name = "mod_date")
    private LocalDateTime modDate;

    private String definition;
    private Integer cost;
    private String advertiser;

    @Column(name = "click_cnt")
    private Integer click_count;

    private String url;

    @Column(name = "content_path")
    private String content_path;

}
