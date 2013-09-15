import os
import yaml
from collections import deque

def open_log(log_name):
    ''' Opens a specific log as an iterable deque.  
    The log file must be in the logs directory.  Atomic file operation. '''
    path = os.path.join(os.getcwd(), 'logs', log_name)
    f = open(path)
    with f:
        return iter(deque(f))


def list_log_names(extension):
    ''' Returns an iterator of all log files in the logs directory. '''
    path = os.path.join(os.getcwd(), 'logs')
    for file in os.listdir(path):
        if file.endswith(extension):
            yield file


def load_config(cfg):
    ''' Returns a config file as a loaded yaml object.  
    The config must be in the main directory. '''
    f = open(cfg)
    with f:
        return yaml.load(f)
