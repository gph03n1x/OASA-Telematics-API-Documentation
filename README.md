## OASA Telematics API documentation

These are the docs for the API used in the OASA Telematics.

Most of the information was extracted from this [JS script](http://telematics.oasa.gr/js/script.js)
so if you want to help head over there first.

You can find the online docs [oasa-telematics-api.readthedocs.io](http://oasa-telematics-api.readthedocs.io/en/latest/)

### Fair use warning

Before using the API for any product, please contact OASA
in order to ask for permission or something.

#### Development

(Optional) Create a python virtual environment:

```shell script
python -m venv venv
```

Install the required packages:

```shell script
pip install -r requirements.txt
```

Build the documentation:

```shell script
cd docs/
make html
```

In order to view the changes in your browser open the `index.html` located
at `docs/build/html`.

If you want to clean completely the build run the following command:
```shell script
make clean
```