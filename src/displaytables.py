from save import Save
from util import add_paths


Save.verify_path(None)
add_paths()

from table import WindowTable


class TransactionTable(WindowTable):
    pass
