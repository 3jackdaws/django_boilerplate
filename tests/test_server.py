import pytest
from urllib.request import urlopen
import yaml
import sys
import os

root_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(root_dir)

@pytest.fixture
def app_host():
    with open('../docker-compose.yml') as fp:
        compose_config = yaml.safe_load(fp)
    port = compose_config['services']['app']['ports'][0].split(":")[0]
    return 'http://localhost:' + port

def test_connection(app_host):
    try:
        site = urlopen(app_host)
    except:
        assert False, 'Could not connect to application'
