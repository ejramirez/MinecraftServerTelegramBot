import logging, json, requests

with open("./bot_properties.json", "r") as f:
    properties_dict = json.load(f)
mcSvrStatEndpoint = properties_dict["resources"]["mcsrvstat_endpoint"]

