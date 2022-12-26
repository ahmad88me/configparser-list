import configparser

class ConfigParser(configparser.ConfigParser):

    # Inspired by: https://stackoverflow.com/questions/335695/lists-in-configparser
    def getlist(self, section, option, sep=",", skip=['"', "'"]):
        """
        Get list of strings
        :param section:
        :param option:
        :param sep:
        :param skip:
        :return:
        """
        string_value = self.get(section, option)
        string_value = string_value.strip()
        if string_value.startswith("[") and string_value.endswith("]"):
            string_value = string_value[1:-1]
        values = []
        for item in string_value.split(sep):
            v = item.strip()
            for sk in skip:
                v = v.replace(sk, '')
            values.append(v)
        return values

    def getlistint(self, section, option, sep=",", skip=['"', "'"]):
        str_values = self.getlist(section, option, sep, skip)
        values = [int(v) for v in str_values]
        return values