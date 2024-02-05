from config.exchanges_config import exchanges

reqs = ["payload"]

indodax = exchanges["gateio"]["request"]

for req in reqs:
    indodax = type(indodax[req]) is str

print(indodax)