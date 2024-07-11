# NOMAD binary parser Proof-of-concept

A parser/schema to read .mat binary files into NOMAD datasets 

## Where the contents of this repo come from

```
$ python3 --version
        Python 3.10.11
$ python3 -m venv 12345
$ source 12345/bin/activate
$ cd 12345/
$ pip install --upgrade pip
$ pip install cruft
$ cruft create https://github.com/FAIRmat-NFDI/cookiecutter-nomad-plugin

        choose mostly defaults (except for project name, and selection of parser and schema components)

$ cd nomad-mwe12345/        
$ pip install -e '.[dev]' --index-url https://gitlab.mpcdf.mpg.de/api/v4/projects/2187/packages/pypi/simple

Create a simple example file: tests/data/struct.mat (see tests/data/Makefile)
nomad parse tests/data/struct.mat --show-archive
```

## Status

- [x] Matching: Recognition of files by extension (`*.mat` in our case) by NOMAD
- [x] Raw parsing: Read information from the mainfile and convert them into intermediate representation (Python data type)
- [x] Schema: Create a data structure for the data archive
- [x] Schema activation: Make use of the schema from the parser
- [ ] Archive export: YAML with the contents of the original Matlab file
- [ ] Inclusion into a NOMAD Oasis, interactive use from the web interface, noninteractive use from the REST API
