---
layout: default
---

<section class="hero" aria-label="Intro">
  <div class="hero__inner">
    <h1 class="hero__title">Hi! I'm {{ site.data.profile.name | default: site.title }}</h1>
    <p class="hero__subtitle">
      {{ site.data.profile.role }}{% if site.data.profile.affiliation %} · {{ site.data.profile.affiliation }}{% endif %}
    </p>

    <div class="hero__icons" aria-label="Links">
      {% if site.data.profile.github %}
        <a class="icon-link" href="{{ site.data.profile.github }}" aria-label="GitHub">
          <svg viewBox="0 0 24 24" aria-hidden="true">
            <path d="M12 .5C5.73.5.75 5.64.75 12c0 5.11 3.29 9.44 7.86 10.97.58.11.79-.26.79-.57v-2.02c-3.2.71-3.87-1.57-3.87-1.57-.52-1.35-1.27-1.71-1.27-1.71-1.04-.72.08-.71.08-.71 1.15.08 1.76 1.2 1.76 1.2 1.02 1.78 2.68 1.27 3.34.97.1-.75.4-1.27.72-1.56-2.55-.3-5.24-1.31-5.24-5.82 0-1.29.45-2.35 1.19-3.18-.12-.3-.52-1.52.11-3.17 0 0 .97-.32 3.18 1.21.92-.26 1.9-.39 2.88-.4.98.01 1.96.14 2.88.4 2.2-1.53 3.17-1.21 3.17-1.21.63 1.65.23 2.87.11 3.17.74.83 1.19 1.89 1.19 3.18 0 4.52-2.7 5.51-5.27 5.81.41.37.78 1.1.78 2.22v3.29c0 .31.21.69.8.57 4.56-1.53 7.85-5.86 7.85-10.97C23.25 5.64 18.27.5 12 .5Z"/>
          </svg>
        </a>
      {% endif %}

      {% if site.data.profile.google_scholar %}
        <a class="icon-link" href="{{ site.data.profile.google_scholar }}" aria-label="Google Scholar">
          <svg viewBox="0 0 24 24" aria-hidden="true">
            <path d="M12 3 1 9l11 6 9-4.91V17h2V9L12 3Zm0 14.02L5.27 13.5v3.08c0 1.8 3 3.92 6.73 3.92s6.73-2.12 6.73-3.92V13.5L12 17.02Z"/>
          </svg>
        </a>
      {% endif %}

      {% if site.data.profile.linkedin %}
        <a class="icon-link" href="{{ site.data.profile.linkedin }}" aria-label="LinkedIn">
          <svg viewBox="0 0 24 24" aria-hidden="true">
            <path d="M4.98 3.5C4.98 4.88 3.87 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1s2.48 1.12 2.48 2.5ZM0.5 23.5h4V7.98h-4V23.5Zm7 0h4v-7.8c0-2.05.39-4.04 2.93-4.04 2.5 0 2.53 2.34 2.53 4.17v7.67h4V15c0-4.05-.86-7.16-5.6-7.16-2.28 0-3.8 1.25-4.42 2.43h-.06V7.98h-3.8V23.5Z"/>
          </svg>
        </a>
      {% endif %}

      <a class="icon-link" href="{{ '/blog/' | relative_url }}" aria-label="Blog">
        <svg viewBox="0 0 24 24" aria-hidden="true">
          <path d="M4 4h16v2H4V4Zm0 4h10v2H4V8Zm0 4h16v2H4v-2Zm0 4h10v2H4v-2Z"/>
        </svg>
      </a>
    </div>
  </div>

  <div class="hero__down" aria-hidden="false">
    <a href="{{ '/about/' | relative_url }}" aria-label="Go to About Me">
      <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" style="fill: currentColor;">
        <path d="M12 16.5 5 9.5l1.4-1.4 5.6 5.6 5.6-5.6L19 9.5l-7 7Z"/>
      </svg>
    </a>
  </div>
</section>
