# HeIn - Header Injection

## General capabilities
This package performs a header injection from API request, where a pair key: value is inserted in the Header.

## Installation
The user should install the package with the following command:<br>
pip install git+https://github.com/jamesmalmeida/HeIn

Be sure to be using Python 3.10

## Usage
After installing the package, the user can import the two built in functions with:<br>
from header_injection import HeaderInjection<br>
from header_injection import TestInjection

### HeaderInjection Function
The HeaderInjection function is callable, where the argment should be a FastAPI() initialization variable, such as:<br>
app = FastAPI()<br>
HeaderInjection(app)<br>
One can find a demonstration script to run with uvicorn ib this git, download the file main.py and run it as:<br>
uvicorn main:app --reload<br>
This should open a local http server to accept the requests.

### TestInjection Function
The TestInjection function performs the actual request, it is callable with two arguments, the first one should be the key and the second one the value, as shown bellow:<br>
TestInjection('Injected-Key','Injected-Value')<br>
This function will return the whole header, where it can be verified that the new key: value pair will be added.

**For now the code does not accept key and values with spaces.**<br>
There is also an example script in this git, refer to the file run-request.py. In this file you can eddit the key and value variables to perform a request.<br>
In addition, there is a run-request-sysarg.py, where the user can simply execute as:<br>
python run-request-sysarg.py Key Value<br>
Thus, one can set the key and values via command line.

