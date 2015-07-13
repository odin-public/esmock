import random

import flask
from flask import Flask, request
from flask.ext.cors import CORS

from mocks import gen_aggregations, gen_data

app = Flask(__name__)
cors = CORS(app)


def esresponse(f):
    def wrapper(*args, **kwargs):
        body = {
            'took': random.randint(50, 150),
            'timed_out': False,
            '_shards': {
                'failed': 0,
                'successfull': 20,
                'total': 20,
            },
            'hits': {
                'hits': [],
                'max_score': 0,
                'total': 0
            }
        }

        body.update(f(*args, **kwargs))

        return flask.jsonify(**body)

    return wrapper


@esresponse
def data(size, data):
    d = gen_data(size)

    return {
        'hits': {
            'hits': d,
            'max_score': None,
        }
    }


@esresponse
def aggs(data):
    aggr_name = next(iter(data['aggs'].keys()))

    return {
        'aggregations': {
            aggr_name: {
                'buckets': gen_aggregations(aggr_name)
            }
        }
    }


@app.route('/<index>/_search', methods=['GET', 'POST'])
def search(index):
    try:
        size = int(request.args.get('size'))
    except:
        size = 10

    if size:
        return data(size, request.get_json())

    return aggs(request.get_json())


@app.route('/')
def index():
    return flask.jsonify(**{
        "status": 200,
        "name": "Karnak",
        "cluster_name": "somecluster",
        "version": {
            "number": "1.5.2",
            "build_hash": "62ff9868b4c8a0c45860bebb259e21980778ab1c",
            "build_timestamp": "2015-04-27T09:21:06Z",
            "build_snapshot": False,
            "lucene_version": "4.10.4"
        },
        "tagline": "You Know, for Search"
    })


def main():
    app.run(port=9200, debug=True)


if __name__ == '__main__':
    main()
