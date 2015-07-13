import random
from datetime import datetime, timedelta

from loremipsum import get_sentence

LOGLEVELS = ('DEBUG', 'INFO', 'WARNING', 'ERROR')


def gen_aggregations(key):
    aggregations = {
        'loglevels': LOGLEVELS,
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
    def get_logfile_name():
        return random.choice(['Bulbasaur', 'Squirtle', 'Jigglypuff', 'Gloom'])

    def log_generator():
        for i in xrange(size):
            random_td = timedelta(microseconds=60 * 60 * 1000 -
                                  random.randint(i * 1000, (i + 1) * 1000))
            yield {
                '_id': str(random.randint(0, 10000000)),
                '_source': {
                    '@timestamp': (datetime.now() - random_td).isoformat(),
                    'file': '/var/log/{0}'.format(get_logfile_name()),
                    'loglevel': random.choice(LOGLEVELS),
                    'log_message': get_sentence(),
                }}

    return [x for x in log_generator()]
