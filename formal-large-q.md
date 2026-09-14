---
layout: page
title: The Low-Individual-Degree Test Without the Diagonal-Lines Test Is Not Quantum-Sound
permalink: /slides/research/formal-large-q/
---

<p class="lede">
  These slides present a counterexample that answers, over every odd-prime field
  F<sub>q</sub>, the large-field form of an open question posed in
  <a href="https://arxiv.org/abs/2009.12982"><em>Quantum soundness of the classical low individual degree test</em></a>.
</p>

## Research context

The 2020 paper proves quantum soundness for the full low-individual-degree test and asks whether its diagonal-lines subtest can be removed. It gives an obstruction at (m, d, q) = (2, 2, 4) and asks whether analogous examples exist for larger q. Our result constructs such a counterexample for every odd prime q: the axis-parallel and self-consistency tests can both be passed perfectly while the required global quantum-soundness conclusion remains bounded away from one.

This question matters because quantum-sound low-degree testing is a key ingredient in the line of work leading to <a href="https://arxiv.org/abs/2001.04383">MIP<sup>*</sup> = RE</a>. The 2020 paper's corrected low-individual-degree soundness theorem is sufficient to recover that result. MIP<sup>*</sup> = RE, in turn, yielded a refutation of Connes' embedding conjecture, a longstanding central problem in operator algebras.

The motivation in the 2020 paper is explicit:

> "Doing so would likely simplify the proof of MIP<sup>*</sup> = RE, as one could replace the complicated 'conditional linear functions' used in the proof with a simpler subclass known as 'coordinate deletion functions'."

Our counterexample shows that this direct simplification cannot work: deleting the diagonal-lines test without adding another compatibility mechanism destroys quantum soundness. Thus the result identifies a structural obstruction to this proposed simplification route. It does not rule out a different replacement for the diagonal-lines test.

**Manuscript status:** The manuscript is now available on arXiv: [arXiv link](https://arxiv.org/abs/2609.12346).

We use Manim for this presentation to make the counterexample and its key compatibility obstruction easier to see.

## Slides

<div class="slide-deck">
  <iframe
    src="{{ '/slides/FormalLargeQSlides.html' | relative_url }}"
    title="The Low-Individual-Degree Test Without the Diagonal-Lines Test Is Not Quantum-Sound animated slides"
    allow="autoplay; fullscreen"
    allowfullscreen
    loading="lazy">
  </iframe>
</div>

<p class="slide-deck__open">
  <a href="{{ '/slides/FormalLargeQSlides.html' | relative_url }}" target="_blank" rel="noopener">Open the presentation in a new tab</a>
</p>
