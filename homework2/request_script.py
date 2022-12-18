import json

import requests
from make_json_examples import make_json_examples
from human_model import HumanModel
import logging
import sys

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


if __name__ == '__main__':
    NUM_EXAMPLES = 10
    response = requests.get('http://127.0.0.1:8000/health')
    make_json_examples(NUM_EXAMPLES)
    print(f'health responce = {response.json()}')
    for i in range(NUM_EXAMPLES):
        with open(f'json_examples/example_{i}.json') as json_file:
            data = json.load(json_file)
            print(data)
            response_post = requests.post(f'http://127.0.0.1:8000/predict/', json=data)
            logger.info(f'predict number {i} responce = {response_post.json()}')
