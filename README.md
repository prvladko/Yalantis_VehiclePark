#  Yalantis Python School


## 💣Stack of technologies 

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
- [python-dotenv](https://pypi.org/project/python-dotenv/) - for production
- [pytest](https://docs.pytest.org/en/6.2.x/contents.html) - for tests

## ⚙️Installation

```
git clone https://github.com/prvladko/Yalantis_VehiclePark.git
```

API requires [Python](https://www.python.org) version 3.9+

Install the dependencies.

```
pip install -r requirements.txt
```

Start project file locally
```
python wsgi.py
```

Verify the deployment by navigating to your server address in
your preferred browser.

```
127.0.0.1:5000
```

## 🔍Actions

### - 📌 POST **/drivers/driver/**  -  ***endpoint to create a driver*** 

<details>
  <summary>👀DETAILS. Click to expand!</summary>

#### Parameters

Field | Type
------------ | -------------
***first_name*** | **reqired**, str
***last_name*** | **reqired**, str
***created_at*** | **reqired**, date('%d-%m-%Y'), example "21-04-2020"
***updated_at*** | **reqired**, date('%d-%m-%Y'), example "14-12-2021"


#### Example

  ```python
import requests

data = {'first_name': 'Driver1', 'last_name': 'Lastname1', 'created_at': '01-01-2018', 'updated_at': '30-01-2018'}
r = requests.post('http://localhost:5000/drivers/driver/', data=data)
  ```
</details>

### - 📌 POST **/vehicle/vehicles/**  -  ***endpoint to create a vehicle*** 

<details>
  <summary>👀DETAILS. Click to expand!</summary>

#### Parameters

Field | Type
------------ | -------------
***make*** | **reqired**, str
***model*** | **reqired**, str
***plate_number*** | **reqired**, str
***created_at*** | **reqired**, date('%d-%m-%Y'), example "21-04-2020"
***updated_at*** | **reqired**, date('%d-%m-%Y'), example "14-12-2021"


#### Example

  ```python
import requests

data = {'make': 'BMW', 'model': 'X5', 'plate_number': 'AA 1234 OO','created_at': '01-01-2018', 'updated_at': '30-01-2018'}
r = requests.post('http://localhost:5000/vehicle/vehicles/', data=data)
  ```
</details>

### - 📌 GET **/drivers/driver/** - ***endpoint to view all drivers***

### - 📌 GET **/vehicles/vehicle/** - ***endpoint to view all vehicles***

### - 📌 GET **/drivers/driver/{***driver_id***}** - ***endpoint for viewing detailed information about the driver***

### - 📌 GET **/vehicles/vehicle/{***vehicle_id***}** - ***endpoint for viewing detailed information about the vehicle***

### - 📌 PATCH **/drivers/driver/{***driver_id***}** - ***endpoint for update driver information***

<details>
  <summary>👀DETAILS. Click to expand!</summary>

#### Parameters

Field | Type
------------ | -------------
***first_name*** | **optional**, str
***last_name*** | **optional**, str
***created_at*** | **optional**, date('%d-%m-%Y'), example "21-04-2020"
***updated_at*** | **optional**, date('%d-%m-%Y'), example "14-12-2021"

**There must be at least one argument for a successful query**

#### Example
  
  ```python
import requests

data = {'first_name': 'Driver1', 'last_name': 'Lastname1', 'created_at': '01-01-2018', 'updated_at': '30-01-2018'}
r = requests.patch('http://localhost:5000/drivers/driver/1', data=data)
  ```

</details>

### - 📌 PATCH **/vehicles/vehicle/{***vehicle_id***}** - ***endpoint for update vehicle information***

<details>
  <summary>👀DETAILS. Click to expand!</summary>

#### Parameters

Field | Type
------------ | -------------
***make*** | **optional**, str
***model*** | **optional**, str
***plate_number*** | **optional**, str
***created_at*** | **optional**, date('%d-%m-%Y'), example "21-04-2020"
***updated_at*** | **optional**, date('%d-%m-%Y'), example "14-12-2021"

**There must be at least one argument for a successful query**

#### Example
  
  ```python
import requests

data = {'make': 'BMW', 'model': 'X5', 'plate_number': 'AA 1234 OO', 'created_at': '01-01-2018', 'updated_at': '30-01-2018'}
r = requests.patch('http://localhost:5000/vehicles/vehicle/1', data=data)
  ```

</details>

### - 📌 DELETE **/drivers/driver/{***driver_id***}** - ***endpoint to delete a driver***

### - 📌 DELETE **/vehicles/vehicle/{***vehicle_id***}** - ***endpoint to delete a driver***

### - 📌 GET **/drivers/drivers/filter_gte** - ***endpoint to display the list of drivers that were created after 10-11-2021***

<details>
  <summary>👀DETAILS. Click to expand!</summary>

#### Parameters

Field | Type
------------ | -------------
***first_name*** | **optional**, str
***last_name*** | **optional**, str
***created_at[gte]*** | **optional**, date('%d-%m-%Y'), example "10-11-2021"

#### Example

  ```python
import requests

data = {'first_name': 'Driver1', 'last_name': 'Lastname1', 'created_at[gte]': '10-10-2020'}
r = requests.get('http://localhost:5000/drivers/driver/filter_gte', data=data)
  ```

</details>

### - 📌 GET **/drivers/drivers/filter_lte** - ***endpoint to display the list of drivers that were created before 16-11-2021***

<details>
  <summary>👀DETAILS. Click to expand!</summary>

#### Parameters

Field | Type
------------ | -------------
***first_name*** | **optional**, str
***last_name*** | **optional**, str
***created_at[lte]*** | **optional**, date('%d-%m-%Y'), example "16-11-2021"

#### Example

  ```python
import requests

data = {'first_name': 'Driver1', 'last_name': 'Lastname1', 'created_at[lte]': '14-12-2021'}
r = requests.get('http://localhost:5000/drivers/driver/filter_lte', data=data)
  ```

</details>