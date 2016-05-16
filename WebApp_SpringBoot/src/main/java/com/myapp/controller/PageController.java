package com.myapp.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Created by jiamingxie on 5/14/16.
 */


//@RestController
//@Controller
@RestController
public class PageController {

    @RequestMapping("/")
    public String home () {
        return "index";
    }
}
