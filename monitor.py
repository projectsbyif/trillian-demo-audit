import logging
import sys

from trillian import TrillianLog
from print_helper import Print
from pprint import pprint


def main(argv):
    logging.basicConfig(level=logging.INFO)

    trillian_log = TrillianLog.load_from_environment()

    Print.status('Checking signature on signed log root')

    validated_log_root = trillian_log.get_log_root()

    Print.tick('Log root is signed correctly by public key')

    # * do full audit between hash[previous] and hash[current]
    # * do consistency check between hash[previous] and hash[current]

    Print.status('Rebuilding Merkle tree from {} entries to get root '
                 'hash'.format(validated_log_root.tree_size))

    Print.bullet('Looking for root hash: {}'.format(
        validated_log_root.root_hash))

    if trillian_log.full_audit(validated_log_root):
        Print.bullet('Calculated root hash:  {}'.format(
            validated_log_root.root_hash))

        Print.tick('Root hashes match, Merkle tree appears correct')

    Print.status('Showing latest log entry')

    Print.normal(str(trillian_log.latest().json()))

    print()


if __name__ == '__main__':
    main(sys.argv)
