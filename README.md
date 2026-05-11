# WESTPA Python API workshop

This repository contains resources for the WESTPA Python API workshop
(18–19 May 2026 at the University of Pittsburgh).


## Getting started

### Get the source code

If you have a GitHub account and are interested in [contributing](#contributing)
code or documentation changes, first  
[fork the WESTPA repository](https://github.com/westpa/westpa/fork)
(making sure to uncheck the "Copy the `westpa2` branch only" checkbox),
then create a local copy of your fork:
```shell
git clone https://github.com/<your_username>/westpa.git
```
   
Otherwise, start by cloning the WESTPA repo directly:
```shell
git clone https://github.com/westpa/westpa.git
```

Once you've downloaded the source code, switch to the `python-api` branch:
```shell
cd westpa
git checkout python-api
```

### Set up a development environment

1. Create and activate a new development environment:
   ```shell
   conda env create -f devtools/conda-envs/test_env.yaml -n <environment_name>
   conda activate <environment_name>
   ```

2. Install WESTPA in development mode:
   ```shell
   pip install -e ".[dev]"
   ```

3. Build and serve the reference documentation:
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
a new branch for your work, for example:
```shell
git checkout -b fix-<issue_number>
```
After making your changes, push the branch to your fork, and
[create a pull request](https://github.com/westpa/westpa/compare/python-api...)
with `python-api` as the destination branch.


## Links

- **WESTPA 2.0 Tutorials:** https://github.com/westpa/tutorials
- **Developer's Guide:** https://github.com/westpa/westpa/wiki/WESTPA-Developer%27s-Guide
