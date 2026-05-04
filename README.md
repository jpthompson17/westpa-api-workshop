# WESTPA Python API workshop

This repository contains resources for the WESTPA Python API workshop (May 18-19, 2026).

## Quick start guide

Get the source code:

```sh
git clone https://github.com/jpthompson17/westpa.git
cd westpa
git checkout python-api
```

Create and activate a new development environment:
```sh
conda env create -f devtools/conda-envs/test_env.yaml -n westpa-dev
conda activate westpa-dev
```

Install WESTPA in development mode:
```sh
pip install -e ".[dev]"
```

Build and serve the reference documentation:
```sh
cd doc
make html
python -m http.server -d _build/html
```
