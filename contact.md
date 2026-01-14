---
layout: page
title: Contact
permalink: /contact/
---

<ul>
  <li><strong>Email:</strong> Not listed publicly. Please reach out via GitHub.</li>
  <li><strong>Location:</strong> {{ site.data.profile.location | default: "(add in _data/profile.yml)" }}</li>
  <li><strong>Links:</strong>
    <span>
      {% if site.data.profile.website %}<a href="{{ site.data.profile.website }}">Website</a>{% endif %}
      {% if site.data.profile.github %}{% if site.data.profile.website %} · {% endif %}<a href="{{ site.data.profile.github }}">GitHub</a>{% endif %}
      {% if site.data.profile.google_scholar %}{% if site.data.profile.website or site.data.profile.github %} · {% endif %}<a href="{{ site.data.profile.google_scholar }}">Scholar</a>{% endif %}
      {% if site.data.profile.linkedin %}{% if site.data.profile.website or site.data.profile.github or site.data.profile.google_scholar %} · {% endif %}<a href="{{ site.data.profile.linkedin }}">LinkedIn</a>{% endif %}
    </span>
  </li>
</ul>
