import os
import sys
import logging
import pathlib
import data_util.config

class TestUtil:
    DATA_UTIL_TEST_USE_INSTALLED_ENV = "DATA_UTIL_TEST_USE_INSTALLED"
    __instance__ = None

    @classmethod
    def instance(self,reload=False):
        if self.__instance__ == None or reload == True:
            self.__instance__ = TestUtil()
            pass
        return self.__instance__


    def __init__(self):
        self.__init_env__()
        pass

    def should_test_installed(self):
        return self.__test_installed__

    def __init_env__(self):
        self.__test_installed__ = False
        if TestUtil.DATA_UTIL_TEST_USE_INSTALLED_ENV in os.environ:
            self.__test_installed__ = True
            pass
        pass
    pass

def get_home_env():
    return None if not data_util.config.Configuration.get_home_env() in os.environ else os.environ[data_util.config.Configuration.get_home_env()]

def reset_home_env(value):
    if value == None:
       if data_util.config.Configuration.get_home_env() in os.environ:
            del os.environ[data_util.config.Configuration.get_home_env()]
            pass
       pass
    else:
        os.environ[data_util.config.Configuration.get_home_env()] = value
        pass
    pass

def get_test_home_path():
    return pathlib.Path(os.getcwd()) / "home_path"
    
if TestUtil.instance().should_test_installed():
    import data_util
else:
    src_path = pathlib.Path(os.path.dirname(__file__)).parent / "src" 
    sys.path.insert(0,str(src_path))
    import data_util

logging.warn(f'Using data_util from {os.path.dirname(data_util.__file__)}')