# [Portfolio](https://zrd.github.io/portfolio/)

Source code for a sample personal portfolio using the [Pelican site generator](https://getpelican.com/).
It is ready to be hosted on [GitHub Pages](https://pages.github.com/). The [published
branch](https://github.com/zrd/portfolio/tree/gh-pages) is generated with [ghp-import](https://pypi.org/project/ghp-import/).

The general workflow is
1. Cut a development branch to isolate changes from your working production code
```
git checkout -b feature-branch
```
2. Do your feature development ...
3. Build source from the `content/` dir (default destination is `output/`). Note that changes don't need to be committed to be included in the build.
```
pelican content
```
4. Serve the site [locally](http://localhost:8000/) and test it out
```
pelican --listen
```
5. Create (or overwrite if it exists) the `gh-pages` branch from the `output/` dir in your `feature-branch`
```
ghp-import output -b gh-pages
```
6. Push from the local `gh-pages` branch to GitHub, which publishes the site
```
git push origin gh-pages
```

The code in this repository only defines the site's content. The layout is
defined in a theme subdirectory, for example `pelican-themes/pelican-blue/`.
Changes to the theme can be tracked in [a separate repository](https://github.com/zrd/portfolio-theme)
and included at  build time, as we're doing here.
