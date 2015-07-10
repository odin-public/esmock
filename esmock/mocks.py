import random
from datetime import datetime


def gen_aggregations(key):
    aggregations = {
        'loglevels': ('DEBUG', 'INFO', 'WARNING', 'ERROR'),
        'files': ('/var/log/messages',)
    }

    return [
        {
            'key': k,
            'doc_count': 200
        }
        for k in aggregations.get(key, ('a',))
    ]


def gen_data(size):
    return [
        {
            '_id': str(random.randint(0, 10000000)),
            '_source': {
                '@timestamp': datetime.now().isoformat(),
                'file': '/var/log/messages',
                'loglevel': 'INFO',
                'log_message': 'Hello!',
            }
        }
        for x in range(size)
    ]
