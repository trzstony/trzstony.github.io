---
layout: page
title: Publications
permalink: /publications/
---

Selected and recent publications. Edit the list in `_data/publications.yml`.

{% if site.data.publications and site.data.publications.size > 0 %}
<ol>
  {% for pub in site.data.publications %}
    <li style="margin: 0 0 14px;">
      <div><strong>{{ pub.title }}</strong> ({{ pub.year }})</div>
      <div style="color: #6b7280;">{{ pub.authors }}</div>
      <div style="color: #6b7280;">{{ pub.venue }}</div>
      {% if pub.links %}
        <div style="margin-top: 6px;">
          {% if pub.links.paper %}<a href="{{ pub.links.paper }}">paper</a>{% endif %}
          {% if pub.links.code %}{% if pub.links.paper %} · {% endif %}<a href="{{ pub.links.code }}">code</a>{% endif %}
          {% if pub.links.bib %}{% if pub.links.paper or pub.links.code %} · {% endif %}<a href="{{ pub.links.bib }}">bib</a>{% endif %}
        </div>
      {% endif %}
    </li>
  {% endfor %}
</ol>
{% else %}
<p class="lede">No publications yet — add entries in <code>_data/publications.yml</code>.</p>
{% endif %}
