import json
from util import verify_budget
from errors import MalformedBudget
from save import Save


class Budget:
    def __init__(self, fs, defaults="budget_default.json"):
        self.fs = fs
        with fs.load_file(defaults) as f:
            categories = json.load(f)
            if verify_budget(categories):
                self.categories = categories
            else:
                raise MalformedBudget


if __name__ == "__main__":
    Budget(Save())
