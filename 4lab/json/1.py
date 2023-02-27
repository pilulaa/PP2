import json 

with open("sample-data.json", "r") as read:
    data = json.load(read)

    print("Interface Status")
    print("=====================================================================================")
    print("DN                                                       Description           Speed        MTU  ")
    print("--------------------------------------------------   --------------------      ------      ------")

    for i in range(18):
        for a, b in data["imdata"][s]['l1PhysIf']["attributes"].items():
            if a == 'dn':
                print(b, end="                                    ")
            if a == "mtu":
                print(b, end="")
            if a == "fecMode":
                print(b, end="       ")

        print("\n")