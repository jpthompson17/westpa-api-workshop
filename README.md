# WESTPA Python API workshop

This repository contains resources for the WESTPA Python API workshop
(May 18-19, 2026, at the University of Pittsburgh).


## Getting started

1. [Fork the WESTPA repository](https://github.com/westpa/westpa/fork). 
   Make sure to uncheck "Copy the `westpa2` branch only".

2. Create a local copy of your fork, and switch to the `python-api` branch:
   ```shell
   git clone https://github.com/<your_username>/westpa.git
   cd westpa
   git checkout python-api
   ```

3. Create and activate a new development environment:
   ```shell
   conda env create -f devtools/conda-envs/test_env.yaml -n westpa-dev
   conda activate westpa-dev
   ```

4. Install WESTPA in development mode:
   ```shell
   pip install -e ".[dev]"
   ```

5. Build and serve the reference documentation:
   ```shell
   cd doc
   make html
   python -m http.server -d _build/html
   ```


## Contributing

If you spot an issue in the code or documentation, or to request a change or
new feature, please [create an issue](https://github.com/westpa/westpa/issues) and
assign it to **jpthompson17**.

If you'd like to work on a fix, reassign the issue  to yourself, and create
a branch for your work, for example:
```shell
git checkout -b fix-<issue_number>
```
After making your changes, push the branch to your fork, and
[create a pull request](https://github.com/westpa/westpa/compare/python-api...)
with `python-api` as the destination branch.


## Links

- **WESTPA Tutorials:** https://github.com/westpa/tutorials
- **Developer's Guide:** https://github.com/westpa/westpa/wiki/WESTPA-Developer%27s-Guide
