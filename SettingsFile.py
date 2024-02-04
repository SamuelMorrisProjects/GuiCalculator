import json
import os
path_to_default_assets= f"{os.path.dirname(os.path.realpath(__file__))}\Assets"
settings = json.load(open(path_to_default_assets+"\default_settings.json"))