# replicated

## Setup

    This project requires python2 and uses virtualenv for development.

### Installing and Running Locally
```
    git clone https://github.com/abaratif/replicated.git
    cd replicated
    virtualenv VENV
    source VENV/bin/activate
    pip install -r requirements.txt
    python -m run
```

After running, verify that the server is up by visiting ``` http://localhost:5000/api/v1.0/spec ```

### Testing

Use nose2 to execute unit tests.
```
	nose2 -v
```

### API Spec

This project uses flask-swagger to provide a clear API specification. The API spec lives at the ```/api/v1.0/spec``` endpoint. For easy viewing, install the Swagger UI Console extension for Chrome.

## Usage

Once the API is spun up, POST requests can be sent to the ```/api/v1.0/keys``` endpoint. See the following curl command for an example.

### Example, Two Users with Keys

In this example, a request is made to obtain keys for two users, using the following curl command:

```
curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"users" : ["gvanrossum", "kennethreitz"]}' 'localhost:5000/api/v1.0/keys'
```

Below is the corresponding response.
```
{
  "code": "success", 
  "data": {
    "gvanrossum": [
      {
        "id": 7189340, 
        "key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDSbJq1XbEC3WmjUNyLchy57svUGespG3WMnf7WpxzLWsfsTrLuxjeogJ/+EznE8k0mgllGjbB9DdRlZf9AXfrUyO27Zse5uVVc4hww+5YANUE0sqDyJYWqrl65/Zm59Eqv4WeLjg16Ory14vUKAm3/KVvvpesmP/F/1gRYzcV3L5TSz7UQzXvdm+arL9UUq0XiIHGdcnkNWOnh2BcXc2uxyijsyUMpWbwtk6TW82AVepxTg2qZ2jWs/5rdHDnS+jbgih+0OQHXHoUTl37XP2QM/KMwkJqBa1KW1BHhyAoRO7Vx7Q4GegDVgkD031qzTXfvsGsXPyFNYK653enI5UTL"
      }
    ], 
    "kennethreitz": [
      {
        "id": 20116054, 
        "key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDSkZaNWJpkvIvJSDHpYiBAwyNAEgKGStitUQUf1iBeYecvQb1Jszgfh47EuLYJOz8Ab6avJbHEjafUMWH7E2tSlsYRcWFAdkTwdIG6jvTLhZHmGM3wgWHUqgwEflcTBsqH9Eg+PViOU5CDQrJJxARCwLIKqgAvObzTHjk5oWzJ33LZJ/Y/OJUrKH8I72xZw3wGcY/yblBgKV+/IKfaM9EgafgKuhtGtNHY+o8gkMsLBhbWR5X608vPG9KrYs9lXTuL+rOq1iRb+YEjOXynudpCtILCGZgd4blCNz4JoBq8L/02vhutD0IquVUfR9AoRzgUmC84Lp3mxJT6hDCb+RlV"
      }, 
      {
        "id": 23104123, 
        "key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDK4xIPRGfHYCxjQUGdFK4ORcljTo6tMrCNsprh/WKnJNNSWquu0ASx2M8OYy05YVHaakT0zmTBpwPc56wK6LHaPFZSF3eUfOXck3WuNGpTlWdiogFax+oJXc5uW9VJL0JaHWtYY98Ay36idwA91ac806WThEdIcYU6Q/ARcc+4SRnQXMR6dEf+tX5EaOfU/o6Gyn6EwCKeb2C2fGXcvc+GNzCSGVxWxnXxm3wn1jOmX8fMpVlyh8aqzObApl6BI+hJO6W3NjIIe67TyHtdZkU1eWXZRpNTqA58uOycNV9nrCXMYMfBo+chbO8kL0ZlD02AdD9+UHSPD8g5f715Hk4f"
      }, 
      {
        "id": 24330972, 
        "key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCjfCIDU1uzRPTc3V/JdTYtmXW/XCJSfyyIs7HmWx8HtPZEYEOzJrHxMExEca96XSLRlUEEscWszlwgvmaUWJb+cBs2hlEXeuNvh/CXOKEUJo0JaGFstO7X7U9UBHBJO/ibTv3LwwnhV1IfcE77uHnHSMihpnLfrd68dzX9lD99G8EtExD0LKhVsRMNp7ap9TYpsxCenna85N632Z6igW5rFTAVsy4LDUW0hcNeNvkIo5NDCYNHAzdDZ3jfvQSChlE3rZGRkbXA8hCHTQwABWs3ZoG4LTy4EaFyx1F5SJsw3VvmT9csSGYKSKY72/uAvhpyuZDPBOdAT4QM0Kq7r6Wh"
      }, 
      {
        "id": 24514479, 
        "key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCgdNG4uSkbmPL28oYiAi0UN47sPyJ7k8RocmODzg2J0WCetnES1oQ6hLBCjun3lAFUs+DpEfvgqO3zjZrfONZrg9DSxj124uHCXI1dG5/QaftbiPx3OqOz3uA7rG9F0VxzWkXcevqsQPi2nODCsG+kxa8swmlSktSn47s0azR4Hw081j4q2CRP/gZwjNdIyVIRQtO0jrXkIsHL72zmdATgpSx4WdFxaMlWIfAvF8Xp7JuQXrTn3EaEG/0Iwpkyyd7UnpDFCGYWqEfWn1vI4OI9WCD6qywfQCATs7XgiWbmOHI+Ni6mz1RUn8a3QiCw8WoioTwkwpPLMLaWNOR3EnW9"
      }
    ]
  }
}
```
### Example, one user with no keys

If a user does not have any public keys, an empty array will be returned for that user.

```
curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"users" : ["abaratif"]}' 'localhost:5000/api/v1.0/keys'
```

```
{
  "code": "success", 
  "data": {
    "abaratif": []
  }
}

```

### Example, invalid username

If a user does not exist on github, an error will be returned.

```
curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"users" : ["abaratif_is_cool"]}' 'localhost:5000/api/v1.0/keys'
```

```
{
  "code": "invalidInput", 
  "error": "Not Found", 
  "message": "Invalid input"
}
```


