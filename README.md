# [Portfolio](https://zrd.github.io/portfolio/)

Source code for a sample personal portfolio using the [Pelican site generator](https://getpelican.com/).
It is ready to be hosted on [GitHub Pages](https://pages.github.com/). The [published
branch](https://github.com/zrd/portfolio/tree/gh-pages) is generated with [ghp-import](https://pypi.org/project/ghp-import/).

The general workflow is
```shell
# Cut a development branch to isolate changes from your working production code
git checkout -b feature-branch

# Do your feature development ...

# Build source from the content/ dir (default destination is output/)
pelican content
# Serve the site on http://localhost:8000/
pelican --listen
# Create (or overwrite if it exists) the gh-pages branch from the output/ dir
# in your feature-branch (note that changes don't need to be committed to be
# included in the build)
ghp-import output -b gh-pages
# Push from the local gh-pages branches to GitHub, which publishes the site
git push origin gh-pages 
```

The code in this repository only defines the site's content. The layout is defined at build time in a theme subdirectory.
