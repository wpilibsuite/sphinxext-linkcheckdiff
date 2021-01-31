# sphinxext-linkcheckdiff
![ci](https://github.com/wpilibsuite/sphinxext-linkcheckdiff/workflows/ci/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Sphinx Extension to run diff-only linkchecks

## Installation

`python -m pip install sphinxext-linkcheckdiff`

## Requirements

- Sphinx >= 3

## Usage
Add `sphinxext.linkcheckdiff` to your extensions list in your `conf.py`

```python
extensions = [
   sphinxext.linkcheckdiff,
]
```

This will add a builder that can be ran using the `make linkcheckdiff` command in your terminal of choice.

## Options
These values are placed in the conf.py of your sphinx project.

* `linkcheckdiff_branch`
    * Required. The branch to diff against.

Note: linkcheckdiff is an extension of the linkcheck builder that ships with Sphinx. linkcheckdiff respects all of linkcheck's configuration options.


## Example Config

```python
linkcheckdiff_branch = "origin/main"
```
