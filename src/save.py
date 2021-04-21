import os
import json


class Save:
    def __init__(self, verbose=False, data_dir="data"):
        self.verbose = verbose
        self.data_dir = data_dir

        self.init_structure()

    def vp(self, *args, **kwargs):
        if self.verbose:
            print(*[">>> Save - " + args[0]] + list(args[1:]), **kwargs)

    def init_structure(self):
        files = ["transactions.json", "userinfo.json", "keychain.json"]
        if not os.path.isdir(self.data_dir):
            os.mkdir(self.data_dir)
            self.vp("Creating root data folder")

        data = {
            "transactions": []
        }

        with open(f"{self.data_dir}/transactions.json", "w") as f:
            json.dump(data, f)

        # for file in files:
        #    open(f"{self.data_dir}/{file}", 'a').close()

    def save_transaction(self, origin, dest, name, category, amount):
        self.init_structure()

        with open(f"{self.data_dir}/transactions.json", "r") as f:
            data = json.load(f)

        data["transactions"].append("")

        print(json.dumps(data))


if __name__ == "__main__":
    s = Save(verbose=True)
    s.save_transaction("FARGO", "AMEX", "Credit Bill", "Bills", 500)
