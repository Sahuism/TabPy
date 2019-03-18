import unittest
import subprocess
import os
import requests


class TestDeployModel(unittest.TestCase):
    _cwd: str

    def __init__(self, *args, **kwargs):
        super(TestDeployModel, self).__init__(*args, **kwargs)
        self._cwd = os.getcwd()

    def setUp(self):
        tabpy_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
        os.chdir(tabpy_root)

    def tearDown(self):
        os.chdir(self._cwd)

    def test_deploy_model_with_script(self):
        """
        Deploys a model using the provided deployment script.

        Has side effects - modifies state.ini file. Only run in clean, testing environment.
        :return:
        """
        # start TabPy server in the background
        process = subprocess.Popen(['python', os.path.join('tabpy-server', 'tabpy.py')])

        # run script
        exec(open(os.path.join('models', 'setup.py')).read())

        # query endpoint
        r1 = requests.get('http://localhost:9004/endpoints/PCA')
        r2 = requests.get('http://localhost:9004/endpoints/SentimentAnalysis')
        print(r1.json)
        print(r2.json)

        # kill process
        process.kill()
