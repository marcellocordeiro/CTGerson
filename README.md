# CTGerson

@jgfn1

@ccal2

@marcellocordeiro

@EudsonSouza

@vvs17

CTGerson is a bus-security system concept made for the Systems and Software Engineering discipline of the Federal University of Pernambuco.

## Instructions

```[delete this] Arduino instructions and setup```

1. Download the repo

```console
git clone https://github.com/marcellocordeiro/CTGerson
```

2. Create and enter a virtual environment

```console
mkdir myenv
python3 -m venv myenv
source myenv/bin/activate
```

3. Update pip and install Django

```console
python3 -m pip install --upgrade pip
pip3 install Django
```

4. Run the web server

```console
python3 web/manage.py runserver
```

Cleaning the project's folder

```console
find . | grep -E "(.DS_Store|__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
```