import unittest
import uvicorn
from fastapi.testclient import TestClient
import main


class TestOnlineInference(unittest.TestCase):
    def test_predict(self):
        client = TestClient(main.app)
        response = client.post(
            url='predict/',
            json={"age": 0, "sex": 0, "cp": 0, "trestbps": 0,
                  "chol": 0, "fbs": 0, "restecg": 0, "thalach": 0,
                  "exang": 0, "oldpeak": 0, "slope": 0, "ca": 0, "thal": 0
                  }
        )
        self.assertEqual(response.status_code, 200)
        print(f'responce = {response.json()}')

    def test_something(self):
        client = TestClient(main.app)
        response = client.get("/health")
        self.assertEqual(response.status_code, 200)
        print(f'responce = {response.json()}')


if __name__ == '__main__':
    # uvicorn.run('main:app', port=8000, reload=True)
    unittest.main()
