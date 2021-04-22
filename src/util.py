def verify_budget(budget):
    if budget.type() == dict:
        for key, value in zip(list(budget.keys()), list(budget.values())):
            if type(key) == str and type(value) == dict:
                for k, v in zip(list(value.keys()), list(value.values())):
                    if k.type() == str and v.type() == int:
                        return True
    return False
