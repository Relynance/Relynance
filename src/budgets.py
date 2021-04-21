import json


class Budget:
    def __init__(self, defaults="budget_default.json"):
        self.categories = {}
