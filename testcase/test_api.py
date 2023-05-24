import pytest 
import os
import requests
from utils import loadfile_util

class TestApi:
    s = requests.session()

    def test_user_users(self):
        result = self.s.get('http://172.17.0.1:4000/user/users')
        assert result.status_code == 200
        # print(result.json())


    @pytest.mark.skip()
    @pytest.mark.parametrize(
        'data',
        loadfile_util.load_yaml(os.path.join(os.path.dirname(__file__),'../data/data.yaml'))
        )
    def test_user_create(self,data):
        result = self.s.post(
            url='http://172.17.0.1:4000/user/users',
            json=data
        )
        print(result.json())








if __name__ == '__main__':
    s = requests.session()
    result = s.get('http://127.0.0.1:4000/user/users')
    print(result.json())
    