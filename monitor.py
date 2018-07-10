import logging
import os
import sys

from trillian import TrillianLog


def main(argv):
    logging.basicConfig(level=logging.DEBUG)

    trillian_log = TrillianLog(**load_log_settings())

    validated_log_root = trillian_log.get_log_root()

    if trillian_log.full_audit(validated_log_root):
        print("Validated log root against all leaf data: {}".format(
            validated_log_root)
        )


def load_log_settings():
    url = os.environ.get('TRILLIAN_LOG_URL', None)
    if not url:
        raise RuntimeError(
            'No TRILLIAN_LOG_URL found in `settings.sh`. It should look like '
            'http://<host>:<post>/v1beta1/logs/<log_id>. On the demo log '
            'server, see http://192.168.99.4:5000/demoapi/logs/ to '
            'and look for the `log_url` field'
        )

    public_key = os.environ.get('TRILLIAN_LOG_PUBLIC_KEY', None)

    if not public_key:
        raise RuntimeError(
            'No TRILLIAN_LOG_PUBLIC_KEY found in `settings.sh`. On the demo log '
            'server, see http://192.168.99.4:5000/demoapi/logs/ to '
            'and look for the `public_key` field'
        )

    return {'base_url': url, 'public_key': public_key}


if __name__ == '__main__':
    main(sys.argv)
