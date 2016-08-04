from configparser import ConfigParser


""" A config parser that use the inbuild configParser but add
    the possibility to parse a list of value separated with comma
    and return a list from it
"""


class ConfigParserPerso(object):
    """ Inherit from configparser and modify the method get() to
        return a list if it catch [ at the beginning and ] at the end
    """
    def __init__(self):
        """ """
        pass

    def build_parser(self):
        """ Create the parser instance """
        self.config = ConfigParser()

    def read_config(self, infile):
        """ Read a config ini file
            Parameters:
            * infile: file containing the config options
            Returns:
            * return_config(): func() to return a dict()
        """
        self.build_parser()
        self.config.read(infile)
        return self.return_config()

    def return_config(self):
        """ Return a dictionary with k:v from section and option """
        d = dict()
        for section in self.config.sections():
            for option in self.config.options(section):
                d[option] = self.get_list_str(self.config[section][option])
        return d

    def get_list_str(self, value):
        """ Transform the value into list
            Return a list object if it is a list in string format
        """
        # Check if the string start and end with [] and then
        # assume it is a list and split value with the ,
        if (value[0] == "[") and (value[-1] == "]"):
            # Remove the [] and split the string on the ,
            return value[1:-1].split(',')
        else:
            return value


def main():
    """ """
    parser = ConfigParserPerso()
    values = parser.read_config('../config.ini')


if __name__ == '__main__':
    main()
