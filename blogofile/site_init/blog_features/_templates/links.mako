<%inherit file="skeleton.mako" />

<div class="ptitle">
  <h3>${title}</h3>
</div>

<div class="round"><div class="gwtext">
  <div class="storycontent">
    % if not cloud:
      <ul class="index-link">
        % for link in links:
          <li><a href="${link['path']}">${link['name']}</a>
          % if 'desc' in link:
           <div>
            ${link['desc']}
           </div>
          %endif
          </li>
        % endfor
      </li>
    % else:
      % for link in links:
        <a href="${link['path']}" style="font-size:1.${link['size']}em">${link['name']}</a>        
      % endfor
    % endif



  </div>
</div></div>

