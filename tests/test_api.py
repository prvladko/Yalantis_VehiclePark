import json
import pytest

data = [({'first_name': 'Name1', 'last_name': 'Lastname1', 'created_at': '2018-01-01', 'updated_at': '2020-01-01'},
         400,
         'date',
         'The parameter created_at must be less than updated_at'),

        ({'first_name': 'Name2', 'last_name': 'Lastname2', 'created_at': 'incorrect_date', 'updated_at': '02-04-2022'},
         400,
         'created_at',
         "time data 'incorrect_date' does not match format '%d-%m-%Y'"),

        ({'first_name': 'Name2', 'last_name': 'Lastname2', 'created_at': '02-01-2020', 'updated_at': '2021-01-01'},
         400,
         'updated_at',
         "time data '01-01-2021' does not match format '%d-%m-%Y'"),

        ({'last_name': 'Lastname3', 'created_at': '05-05-2021', 'updated_at': '15-05-2022'},
         400,
         'first_name',
        'Missing required parameter in the JSON body or the post body or the query '
         'string'
         ),

        ({'first_name': 'Driver_without_created_date', 'last_name': 'Lastname3', 'updated_at': '15-05-2022'},
         400,
         'created_at',
         'Missing required parameter in the JSON body or the post body or the query '
         'string'
         ),

        ({'first_name': 'Driver_without_updated_date', 'last_name': 'Lastname3', 'created_at': '15-05-2022'},
         400,
         'updated_at',
         'Missing required parameter in the JSON body or the post body or the query '
         'string'
         ),
        ]


@pytest.mark.parametrize("data, expected_status_code, key_in_response, expected_response", data)
def test_create_course_incorrect_data(test_client, data, expected_status_code, key_in_response, expected_response):
    r = test_client.post('/create', data=data)
    response = json.loads(r.get_data(as_text=True))
    assert r.status_code == expected_status_code
    assert response['message'][key_in_response] == expected_response


def test_home_page(test_client):
    response = test_client.get('/')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['message'] == 'VehicleParkAPI home page'


def test_drivers(test_client):
    response = test_client.get('/drivers/driver')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert type(data['message']['drivers']) == list


def test_vehicles(test_client):
    response = test_client.get('/vehicles/vehicle')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert type(data['message']['vehicles']) == list
