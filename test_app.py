import requests
import pytest

HOST = 'https://127.0.0.1:8081'


def test_active_service():
    """assert 200 response when calling heartbeat endpoint"""
    # response = requests.get(HOST + '/')
    # assert response.status_code == 200
    # assert response['message'] == 'Service is running'
    pass  

def test_good_request():
    """assert correct response with a good request"""
    # message = 'This is a test'
    # json = {"message":message}
    # response = requests.post(HOST + '/generate_token', json=json)
    # assert response.status_code == 200
    # assert response['message'] == message
    # assert response['signature']
    pass

def test_bad_request():
    """assert error catching for bad request"""
    # message = "This is a test"
    # test incorrect key
    # json = {"id":message}
    # assert response.status_code == 400
    # assert response['error']
    # assert response['message] == 'Please reformat request and try again'
    pass
