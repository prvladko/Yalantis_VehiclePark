## ⚙️Installation

Clone the repository
```
git clone https://github.com/prvladko/Yalantis_VehiclePark.git
```

API requires [Python](https://www.python.org) version 3.9+

Create a virtualenv and activate it
```
$ python3 -m venv venv
$ .venv/bin/activate
Or on Windows cmd:

$ py -3 -m venv venv
$ venv\Scripts\activate.bat
```

Install the dependencies
```
pip install -r requirements.txt
```


##Start project file locally
```
cd src
python wsgi.py
```

Verify the deployment by navigating to your server address in
your preferred browser or via Postman

```
127.0.0.1:5000
```