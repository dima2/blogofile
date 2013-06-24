<%inherit file="base.mako" />
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html>  
  <head>${self.head()}</head>
  <body>
    <div id="megadiv">
      <div id="header">${self.header()}</div>
      <div id="wrapper">
        <div id="main">${next.body()}</div>
      </div>
      <div id="left"></div>
      <div id="sidebar">${self.sidebar()}</div>
      <div id="footer">${self.footer()}</div>
    </div>
  </body>
</html>

<%def name="head()">
  <%include file="head_ext.mako" args="title=bf.config.blog.title.decode('utf-8'), 
                                 description=bf.config.blog.description_ext.decode('utf-8'), 
                                    keywords=bf.config.blog.keywords.decode('utf-8')"/>
</%def>

<%def name="header()">
  <%include file="header.mako" args="random=10"/>
</%def>

<%def name="footer()">
  <%include file="footer.mako" />
</%def>

<%def name="sidebar()">
  <%include file="sidebar.mako" />
</%def>
