import os
import sys
import json
import os
from errors import MalformedConfig

CONFIG_LOCATION = "config.json"


class Save:
    def __init__(self):
        self.config = {}

        self.verify_path()

        self.load_config(CONFIG_LOCATION)

        self.init_structure()

    def vp(self, *args, **kwargs):
        if not "debug" in self.config:
            print(*[">>> Save - " + str(args[0])] + [str(y)
                  for y in list(args[1:])], **kwargs)
            return
        elif self.config["debug"]:
            print(*[">>> Save - " + str(args[0])] + [str(y)
                  for y in list(args[1:])], **kwargs)
            return

    def verify_path(self):
        if os.getcwd().split("\\")[-1].split("/")[-1] == "src":
            os.chdir("..")

    def init_structure(self):
        files = ["transactions.json", "userinfo.json", "keychain.json"]
        if not os.path.isdir(self.config["dirs"]["data"]):
            os.mkdir(self.config["dirs"]["data"])
            self.vp("Creating root data folder")

        data = {
            "transactions": []
        }

        with open(f'{self.config["dirs"]["data"]}/transactions.json', "w") as f:
            json.dump(data, f)

        # for file in files:
        #    open(f"{self.config["dirs"]["data"]}/{file}", 'a').close()

    def load_config(self, location):
        with open(location, "r") as f:
            conf = json.load(f)
            try:
                self.config["version"] = conf["version"]
                self.config["dirs"] = {}
                self.config["dirs"]["data"] = conf["dirs"]["data"]
                self.config["dirs"]["src"] = conf["dirs"]["src"]
                self.config["debug"] = conf["debug"]
            except KeyError as e:
                self.vp(e)
                raise MalformedConfig

    def save_transaction(self, origin, dest, name, category, amount):
        self.init_structure()

        with open(f'{self.config["dirs"]["data"]}/transactions.json', "r") as f:
            data = json.load(f)

        data["transactions"].append("")

        self.vp(json.dumps(data))

    def load_file(self, filename, method="r"):
        if not os.path.exists(filename):
            return False
        return open(f'{self.config["dirs"]["data"]}/{filename}', method)


if __name__ == "__main__":
    s = Save()
    s.save_transaction("FARGO", "AMEX", "Credit Bill", "Bills", 500)
