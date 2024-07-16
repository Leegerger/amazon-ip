import requests
js = requests.get("https://ip-ranges.amazonaws.com/ip-ranges.json").json()
rules =[
            "/ip firewall address-list remove [/ip firewall address-list find list=amazon]",
            "/ip firewall address-list"
        ] + \
        [f"add address={j['ip_prefix']} disabled=no list=amazon" for j in js['prefixes']]
with open("amazon.rsc",'w') as f:
    f.write("\n".join(rules))