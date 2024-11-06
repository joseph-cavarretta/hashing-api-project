## HMAC Token API
This API receives a request with a JSON payload consisting of a  
'message' string and returns an HMAC token generated from that string.  

## Endpoints
GET "/"  
    - Used to test that service is running  
    - Example request:  
        - curl --request GET --url http://127.0.0.1:8081/  
    - Example response:  
        - {
            "message":"Service is running!"
          }  
        
POST "/generate_token"  
    - Receives a request with a JSON payload  
        - Must include a 'message' key  
    - Returns an HMAC token generated from 'message' 
    - Example request:  
        - curl --request POST \  
          --url http://127.0.0.1:8081/generate_token \  
          --header 'Content-Type: application/json' \  
          --data '{
            "message": "This is the message"
            }'
    - Example response:
        - {  
            "message":"This is the message",  
            "signature":"ee9100a625e1a5c5c07cc1f78cefac583e5dd31b63b37914529ffe9c8e673dc8"  
          }  

## To Setup and Run  
Locally:  
    - In your virtual environment, install requirements.txt  
        - pip install -r requirements.txt  
    - Run python3 app/app.py to launch service  

Locally with docker:  
    - Make sure docker daemon is running  
    - Run sudo chmod +x scripts/build.sh  
    - Run sudo chmod +x scripts/run.sh  
    - Run source scripts/build.sh to build image  
    - Run source scripts/run.sh to launch service  

## Errors
    - Not including a 'message' key in POST request to /generate_token  
      returns a MessageError  

## Unit testing
Testing is implemented with pytest  
To run tests:  
    - Run pytest in /uplight directory  

NOTE:  
* Unit testing not currently implemented due to OpenSSL incompatibilities *  
* This is possibly a bug in the urllib3 library *