[![Build Status](https://ahmad88me.semaphoreci.com/badges/configparser-list/branches/main.svg?key=1b31676d-8fc4-438c-9232-e0c63babe633)](https://ahmad88me.semaphoreci.com/projects/configparser-list)
[![codecov](https://codecov.io/gh/ahmad88me/configparser-list/branch/main/graph/badge.svg?token=OK2EPNG23U)](https://codecov.io/gh/ahmad88me/configparser-list)


# configparser-list
Extends ConfigParser to support lists (`getlist`)

# Install
`pip install configparser-list`

# Tests
To run the tests:

```
python -m unittest
```

# Examples
## Example 1 uses `dict`
```
from ConfigParserList import ConfigParser


def list_from_dict():
    """
    This example sets the configuration from a dict and then fetchs a list
    :return:
    """
    str_list = ['A', "B", "C"]
    int_list = [1, 2, 3]
    d = {'SEC': {
        'int': 10,
        'float': 1.0,
        'liststr': str_list,
        'listint': int_list}
    }
    conf = ConfigParser()
    conf.read_dict(d)
    alpha = conf.getlist('SEC', 'liststr')
    ints = conf.getlistint('SEC', 'listint')
    print("list from config (dict): ")
    print(f"Alpha {alpha} is of type {type(alpha)}")
    print(f"Ints {ints} is of type {type(ints)}")
```

## Example 2 uses `str`
```
from ConfigParserList import ConfigParser

def list_from_string():
    """
    This example sets the configuration from a string and then fetchs a list
    :return:
    """
    conf_str = """
    [SEC]
    int=10,
    float=1.0,
    liststr=A, B, C
    listint=1, 2, 3
    """
    conf = ConfigParser()
    conf.read_string(conf_str)
    alpha = conf.getlist('SEC', 'liststr')
    ints = conf.getlistint('SEC', 'listint')
    print("list from config (string): ")
    print(f"Alpha {alpha} is of type {type(alpha)}")
    print(f"Ints {ints} is of type {type(ints)}")
```