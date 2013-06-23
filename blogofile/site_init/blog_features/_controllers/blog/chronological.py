# Write all the blog posts in reverse chronological order
import os
from blogofile.cache import bf

blog = bf.config.controllers.blog


def run():
    write_blog_chron(posts=blog.posts, root=blog.pagination_dir.lstrip("/"))


def write_blog_chron(posts, root):
    page_num = 1
    post_num = 0
    html = []
    prev_link = None
    pages_total = len(posts) / blog.posts_per_page + 1
    
    while len(posts) > post_num:
        #Write the pages, num_per_page posts per page:
        page_posts = posts[post_num:post_num + blog.posts_per_page]
        post_num += blog.posts_per_page

        if len(posts) > post_num:
            next_link = blog.url + root + "/" + str(page_num+1)+".html"
        else:
            next_link = None

        page_dir = bf.util.path_join(blog.path, root, str(page_num))

        env = {
            "posts": page_posts,
            "next_link": next_link,
            "prev_link": prev_link,
            "current_page": page_num,
            "pages_total" : pages_total
        }
        
        if page_num==1:
            path = bf.util.path_join(blog.path, "index.html")
            prev_link= blog.url
        else:
            path = page_dir + ".html"
            prev_link= blog.url + path

        bf.writer.materialize_template("chronological.mako", path, env)
        page_num += 1

        
