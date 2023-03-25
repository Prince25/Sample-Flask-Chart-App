
## Installation and Usage

### Set up Virtual Environment (Optional)

1. Create the virtual environment
```shell
python -m venv venv
```

2. Activate it

Windows
```shell
venv\Scripts\activate
```

Linux
```shell
source venv/bin/activate
```

### Install Python Packages
```shell
pip install -r requirements.txt
```

### Run
```
python main.py
```

Go to the URL: http://127.0.0.1:5000/

For CSV data about electronics, go to: http://127.0.0.1:5000/electronics

For Excel data about financials, go to: http://127.0.0.1:5000/financial


## Technologies
- [Flask](https://flask.palletsprojects.com/)
- [Pandas](https://pandas.pydata.org/)
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/)
