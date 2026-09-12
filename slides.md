---
layout: page
title: Slides
permalink: /slides/
---

<div class="slide-categories">
  {% for category in site.data.slides %}
    <a class="slide-category" href="{{ category.url | relative_url }}">
      <span>{{ category.title }}</span>
      <span class="slide-category__arrow" aria-hidden="true">&rarr;</span>
    </a>
  {% endfor %}
</div>
