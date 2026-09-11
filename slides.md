---
layout: page
title: Slides
permalink: /slides/
---

<div class="post-list slide-list">
  {% for slide in site.data.slides %}
    <article>
      <h2 style="margin:0;"><a href="{{ slide.url | relative_url }}">{{ slide.title }}</a></h2>
      {% if slide.description %}<p>{{ slide.description }}</p>{% endif %}
    </article>
  {% endfor %}
</div>
