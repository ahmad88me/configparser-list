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


if __name__ == '__main__':
    list_from_string()

