import urlparse
from blogofile.cache import bf
import re

blog = bf.config.controllers.blog


def run():
    write_pages()


def write_pages():
    site_re = re.compile(bf.config.site.url, re.IGNORECASE)

    
    for page in blog.pages:
        if page.permalink:
            path = site_re.sub("", page.permalink)
            blog.logger.info(u"Writing permapage for post: {0}".format(path))
        else:
            #Permalinks MUST be specified. No permalink, no page.
            blog.logger.info(u"Post has no permalink: {0}".format(page.title))
            continue

        
        bf.writer.materialize_template(
                "page.mako", path, {"post":page})
