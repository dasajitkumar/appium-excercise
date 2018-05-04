import os
import re
import yaml
from selenium import webdriver

if 'SERVER_CONFIGURATION_PATH' in os.environ:
    server_configuration_path = os.getenv('SERVER_CONFIGURATION_PATH')
else:
    base_path = os.path.split(os.path.abspath(__file__))
    server_configuration_path = os.path.join(base_path[0],'server_configuration.yaml')


class RemoteInit(object):
    def __init__(self):
        """
        Initializing the device/emulator driver
        :param ip_address: ip address appium server
        :param port_no: port of appium server
        :param desire_capabilities: webdriver desire capabilities
        """
        server_data = yaml.load(open(server_configuration_path, 'r'))
        base_url = 'http://' + str(server_data['ip_address']) + ':' + str(server_data['port_no']) + '/wd/hub'
        self.driver = webdriver.Remote(base_url, server_data['desire_capabilities'])
