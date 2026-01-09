# Scripts for Generating Blog Post Figures

This directory contains Python scripts used to generate matplotlib figures for blog posts.

## Structure

Each post has its own subdirectory under `scripts/`, named after the post slug or title:

```
scripts/
  ├── buoyancy-beyond-3d/
  │   └── generate_figures.py
  ├── [other-post-name]/
  │   └── generate_figures.py
  └── README.md
```

## Usage

1. Navigate to the specific post's script directory:
   ```bash
   cd scripts/buoyancy-beyond-3d
   ```

2. Run the figure generation script:
   ```bash
   python generate_figures.py
   ```

3. Generated images will be saved to `assets/images/[post-name]/`

## Requirements

Make sure you have the required Python packages installed:
```bash
pip install matplotlib numpy
```

## Adding New Posts

When creating figures for a new post:

1. Create a new directory under `scripts/` with the post's slug/name
2. Create a `generate_figures.py` script in that directory
3. Follow the pattern in existing scripts:
   - Import matplotlib and numpy
   - Set up output directory (typically `../../assets/images/[post-name]/`)
   - Create functions for each figure
   - Use high DPI settings for publication-quality figures
   - Save figures with descriptive names

## Image Output

Generated images are saved to `assets/images/[post-name]/` and can be referenced in your markdown posts using:

```markdown
![Figure description]({{ site.baseurl }}/assets/images/buoyancy-beyond-3d/figure_name.png)
```
