---
layout: page
title: Research
permalink: /slides/research/
---

{% assign category = site.data.slides | where: "slug", "research" | first %}
<div class="post-list slide-list">
  {% for slide in category.slides %}
    <article>
      <h2><a href="{{ slide.url | relative_url }}">{{ slide.title }}</a></h2>
      {% if slide.description %}<p>{{ slide.description }}</p>{% endif %}
    </article>
  {% endfor %}
</div>
