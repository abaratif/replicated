# replicated

## Setup

    This project requires python2 and uses virtualenv for development.

### Running Locally
```
    git clone https://github.com/abaratif/replicated.git
    cd replicated
    virtualenv -p python3 VENV
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

