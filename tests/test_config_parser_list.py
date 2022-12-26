from unittest import TestCase
from ConfigParserList import ConfigParser


class TestConfigParserList(TestCase):

    def test_list(self):
        str_list = ['A', "B", "C"]
        int_list = [1, 2, 3]
        d = {'SEC': {
            'int': 10,
            'float': 1.0,
            'liststr': str_list,
            'listint': int_list}
        }
        config = ConfigParser()
        config.read_dict(d)
        self.assertListEqual(config.getlist('SEC', 'liststr'), str_list)
        self.assertListEqual(config.getlistint('SEC', 'listint'), int_list)

