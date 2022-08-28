import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from pprint import pprint

from chalicelib.db.database import Database


def main():
    current_dir = os.path.dirname(__file__)
    db_filename = 'tweets-collorctor.db'
    db_filepath = os.path.join(current_dir, db_filename)

    db = Database(db_filepath)
    tran = db.transaction()
    try:
        db.create_tables(tran)
        tran.commit()
    except Exception as e:
        pprint(e)
        tran.rollback()
    finally:
        db.close()


if __name__ == '__main__':
    main()
