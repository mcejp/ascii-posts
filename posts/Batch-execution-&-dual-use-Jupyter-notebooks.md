---
layout: post
render_with_liquid: false
date: 2026-04-14
title: "Batch execution & dual-use Jupyter notebooks"
unlisted: true
---

Basic use is simple enough:

    jupyter nbconvert --execute --to notebook my_notebook.ipynb

In practice, we often require the ability to execute the notebook with
variable parameters (like any other program). At the same time, we do
not want to forfeit the convenience of interactive execution and
parameter tweaking. Thus, *dual-use* notebooks.

### A pattern for dual-use notebooks

A dual-use notebook can be executed in 3 modes:

1.  interactive, with parameters specified inline in the cells that use
    them
2.  interactive, loading parameters from a file
3.  batch, loading parameters from a file

(techincally, nothing prevents batch execution with inline parameters,
but it's not the use-case we're interested in)

This choice must be made inside the notebook by uncommenting one of the
three options:

``` python
# 1) interactive mode with inline parameters
# PARAM_FILE = None
# 2) interactive mode with external parameters
# PARAM_FILE = "example1.yaml"
# 3) batch mode with external parameters
# PARAM_FILE = os.environ["PARAM_FILE"]

if PARAM_FILE:
    with open(PARAM_FILE) as f:
        PARAMS = yaml.safe_load(f)
    # print(PARAMS)
else:
    PARAMS = {}
```

example1.yaml:

``` yaml
---
seed: 42
```

After this, parameters are retrieved close to their use site like this:

``` python
# in mode 1, freely tweak the fallback value here
seed = PARAMS.get("seed", 0)
```

In mode 3, the parameter file must be specified by means an environment
variable.

    PARAM_FILE=example2.yaml \
        jupyter nbconvert --execute --to notebook \
        my_notebook.ipynb

Unsolved: how to get `sys.stdout` to show up in terminal

Tip: to clean up notebook before committing to version control:

    pipx run nb-clean clean \
        --remove-empty-cells \
        --preserve-cell-outputs \
        my_notebook.ipynb

### Alternative: Papermill

To be investigated -- should solve many of the issues:
[Papermill](https://papermill.readthedocs.io/en/latest/)
