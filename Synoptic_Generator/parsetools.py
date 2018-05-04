import os,sys

def makedirs(dirname, exist_ok=True):
    '''
    Simple replication of os.makedirs from Python 3.2
    '''
    if not os.path.exists(dirname):
        try:
            os.makedirs(dirname)
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
