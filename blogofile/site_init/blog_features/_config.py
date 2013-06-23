# -*- coding: utf-8 -*-
import os

######################################################################
# This is your site's Blogofile configuration file.
# www.Blogofile.com
#
# This file doesn't list every possible setting, it relies on defaults
# set in the core blogofile _config.py. To see where the default
# configuration is on your system run 'blogofile info'
#
######################################################################

######################################################################
# Basic Settings
#  (almost all sites will want to configure these settings)
######################################################################
## site_url -- Your site's full URL
# Your "site" is the same thing as your _site directory.
#  If you're hosting a blogofile powered site as a subdirectory of a larger
#  non-blogofile site, then you would set the site_url to the full URL
#  including that subdirectory: "http://www.yoursite.com/path/to/blogofile-dir"


f=open('_profile')
site.url = f.read().strip("\n")
f.close()
print "Profile "+site.url

#if you posts have different permalinks then 'site.url' set this
blog.old_url = "http://thexnews.com/" 

#### Blog Settings ####
blog = controllers.blog

## blog_enabled -- Should the blog be enabled?
#  (You don't _have_ to use blogofile to build blogs)
blog.enabled = True

blog.auto_permalink.enabled = True
# This is relative to site_url
blog.auto_permalink.path    = "/:title.html"

## blog_path -- Blog path.
#  This is the path of the blog relative to the site_url.
#  If your site_url is "http://www.yoursite.com/~ryan"
#  and you set blog_path to "/blog" your full blog URL would be
#  "http://www.yoursite.com/~ryan/blog"
#  Leave blank "" to set to the root of site_url
blog.path = "/"

## blog_name -- Your Blog's name.
# This is used repeatedly in default blog templates
blog.name = "The X News"

## blog_description -- A short one line description of the blog
# used in the RSS/Atom feeds.
blog.description = "IT-Блог со странным названием"

#Stuff for search engines, goes to <head> tag:
blog.title="Блог про Софт, Интернет, Ubuntu Linux, Wordpress"
blog.description_ext="Блог про Ubuntu Linux, Софт, Программирование на Python, Железо, Wordpress, Интернет - Решения проблем, Обзоры, Тесты - а также креатив, всякие идиотизмы и мудрые мысли"
blog.keywords="apple,железо,идиотизм,лытыдыбр,todo,интернет,минимализм,не прошло и года как димоныч вернулся,best,doom,mp3,rockbox,sandisk,sansa clip,аудиокниги,видео,перепрошивка,плагины plugin,плеер player,ubuntu,программы софт проги приложения,советы,софт,doom 2,doom 3,windows,ад,игры,сессия,скачать,ъ,special,ubuntu 10.04,windows 7,и.м.х.о.,оффтоп,firefox, файерфокс, аддоны, плагины, addons, plugins, extensions, расширения, менеджер закачек,addons,firefox 3,python,skype,велосипед,flash,linux,turbofilm.ru,workaround,youtube.com,тормоза лаги и глюки,удобство,sandisk sansa clip,flac,nokia,подкасты"

## blog_timezone -- the timezone that you normally write your blog posts from
blog.timezone = 'Europe/Riga'


blog.disqus.enabled=True
blog.disqus.name='blogdimy'

blog.posts_per_page = 10

blog.post_default_filters = {
    "markdown": "syntax_highlight, markdown, markdown_ext, wordpress_legacy",
    "md": "syntax_highlight, markdown, markdown_ext, wordpress_legacy",
    "textile": "syntax_highlight, textile",
    "org": "syntax_highlight, org",
    "rst": "syntax_highlight, rst",
    "html": "syntax_highlight, wordpress_legacy"
}


blog.min_tag_count_for_page = 3