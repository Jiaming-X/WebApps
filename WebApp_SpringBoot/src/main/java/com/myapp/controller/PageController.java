package com.myapp.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Created by jiamingxie on 5/14/16.
 */


//@RestController
//@Controller

/*
@RestController
public class PageController {

    @RequestMapping("/")
    public String home () {
        return "index";
    }
}
*/

import org.springframework.ui.Model;
import com.myapp.domain.Post;

import java.util.ArrayList;
import java.util.Date;


//@RequestMapping("/posts")
@Controller
public class PageController {

    @RequestMapping("/")
    public String home(){
        return "main_page";
    }

    @RequestMapping("/posts")
    public String list(Model model){
        model.addAttribute("pageTitle","My Custom Page Title");
        model.addAttribute("posts",createPosts());
        return "views/list";
    }

    private ArrayList<Post> createPosts(){
        // post 1
        Post post1 = new Post();
        post1.setTitle("My Blog Post 1");
        post1.setPosted(new Date());
        post1.setAuthor("Dan Vega");
        post1.setBody(getPostBody());

        // post 2
        Post post2 = new Post();
        post2.setTitle("My Blog Post 2");
        post2.setPosted(new Date());
        post2.setAuthor("JM Xie");
        post2.setBody("<p>This post didn't take long to write.");

        ArrayList<Post> posts = new ArrayList<Post>();
        posts.add(post1);
        posts.add(post2);

        return posts;
    }

    private String getPostBody(){
        String body = "<p>This is the body</p>";
        return body;
    }
}
