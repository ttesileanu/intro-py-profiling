# Basic introduction to profiling in Python

This is a set of files I used to present a brief introduction to Python profiling, as part of the CCN Coding Club at the [Flatiron Institute](https://www.simonsfoundation.org/flatiron/).

## Pre-requisites
Apart from a standard Python 3 installation, some of the code uses the `line_profiler` and `snakeviz` packages. You can install these using either `pip`:

```sh
pip install line_profiler
pip install snakeviz
```
or `conda`:
```sh
conda install -c conda-forge line_profiler
conda install snakeviz
```

## How to use
The notebook [`profiling_intro.ipynb`](profiling_intro.ipynb) contains a brief introduction to benchmarking and profiling, and the differences between the two. It also showcases using the `line_profiler` and `snakeviz` in a notebook.

The Python scripts are meant to showcase how to profile from the command line. Some of the relevant commands to try can be found in [`useful_commands.sh`](useful_commands.sh).

## Other resources

A tutorial on Python profiling: https://jakevdp.github.io/PythonDataScienceHandbook/01.07-timing-and-profiling.html

More info on profiling: https://lyz-code.github.io/blue-book/python_profiling/

Documentation for `snakeviz`: https://jiffyclub.github.io/snakeviz/

Reference for `profile` module: https://docs.python.org/3/library/profile.html

Repository and documentation for `line_profiler`: https://github.com/pyutils/line_profiler

Profiling in `pytorch`: https://pytorch.org/tutorials/recipes/recipes/profiler_recipe.html

List of Jupyter built-in magics: https://ipython.readthedocs.io/en/stable/interactive/magics.html
