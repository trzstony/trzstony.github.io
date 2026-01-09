---
layout: default
---

# Welcome to My Blog

{% for post in site.posts %}
  <article>
    <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
    <p class="post-date">{{ post.date | date: "%B %d, %Y" }}</p>
    {{ post.excerpt }}
  </article>
{% endfor %}
