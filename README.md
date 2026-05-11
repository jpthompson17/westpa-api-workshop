# WESTPA Python API workshop

This repository contains resources for the WESTPA Python API workshop
(18–19 May 2026 at the University of Pittsburgh).


## Getting started

1. Clone this repository:
   ```
   git clone https://github.com/jpthompson17/westpa-api-workshop
   ```

2. If you're interested in [contributing](#contributing) code or documentation
   changes,
   [fork the WESTPA repository](https://github.com/westpa/westpa/fork)
   (make sure to uncheck "Copy the `westpa2` branch only"),
   and create a local copy of your fork:
   ```
   git clone https://github.com/<your_username>/westpa.git
   ```
   If not, clone the WESTPA repo directly:
   ```
   git clone https://github.com/westpa/westpa.git
   ```
   
3. Check out the `python-api` branch:
   ```shell
   cd westpa
   git checkout python-api
   ```

4. Create and activate a new Conda environment:
   ```
   conda env create -f devtools/conda-envs/test_env.yaml -n <env_name>
   conda activate <env_name>
   ```

5. Install WESTPA in development mode:
   ```shell
   pip install -e ".[dev]"
   ```

6. Build and serve the reference documentation:
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
```
git checkout -b fix-<issue_number>
```
After making your changes, push the branch to your fork, and
[create a pull request](https://github.com/westpa/westpa/compare/python-api...)
with `python-api` as the destination branch.


## Links

- **WESTPA 2.0 Tutorials:** https://github.com/westpa/tutorials
- **Developer's Guide:** https://github.com/westpa/westpa/wiki/WESTPA-Developer%27s-Guide
