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


if __name__ == '__main__':
    list_from_dict()

