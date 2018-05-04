from selenium import webdriver


class RemoteInit(object):
    def __init__(self, ip_address, port_no, desire_capabilities=False):
        """
        Initializing the device/emulator driver
        :param ip_address: ip address appium server
        :param port_no: port of appium server
        :param desire_capabilities: webdriver desire capabilities
        """
        base_url = 'http://' + str(ip_address) + ':' + str(port_no) + '/wd/hub'
        if desire_capabilities:
            self.driver = webdriver.Remote(base_url, desire_capabilities)
        else:
            self.driver = webdriver.Remote(base_url)
