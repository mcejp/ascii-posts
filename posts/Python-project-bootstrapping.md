---
layout: post
render_with_liquid: false
date: 2024-07-21
title: "Python project bootstrapping"
unlisted: true
---

The modern way: [use pyproject.toml
only](https://github.com/mcejp/perlin-numpy/blob/master/pyproject.toml)

### Avoid these outdated mechanisms

- distutils
- [setup.py](https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html)
- setup.cfg

## Sphinx API docs

Note: the most reliable way to have autodoc working is to install the
package in question in the environment where Sphinx is executed

1.  Set up Sphinx:

    sphinx-quickstart docs

2.  In docs/conf.py, add the `sphinx.ext.autodoc` extension

3.  Add docs/api.rst:

    ``` rst
    API reference
    =============

    .. automodule:: goeiedag
       :imported-members:
       :members:
       :undoc-members:
    ```

4.  Add `api` to `toctree` in docs/index.rst

### Publishing on Read the Docs

1.  Sign up on <https://about.readthedocs.com/>
2.  [Import a project](https://readthedocs.org/dashboard/import/)
3.  Add and adjust the .readthedocs.yaml file as per the wizard

Examples:

- <https://github.com/mcejp/goeieDAG>
- <https://github.com/mcejp/perlin-numpy>

## Releasing to PyPI

Prerequisities: the packages
[`build`](https://pypa-build.readthedocs.io/en/stable/index.html) and
`twine`

- update CHANGELOG.md and version in pyproject.toml

- execute the following commands

      mkdir -p dist
      rm dist/*.tar.gz dist/*.whl
      python -m build
      python -m twine upload --repository testpypi dist/*       # either
      python -m twine upload dist/*                             # or
