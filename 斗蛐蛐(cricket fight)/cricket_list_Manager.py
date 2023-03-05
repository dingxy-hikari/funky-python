# import json
import json

cfp = open('cricket_list.json', 'r')
cricket_list = json.load(cfp)
cfp.close()


def cricket_list_write_in(name, hp, atk, dfn):
    global cricket_list
    t_list = []
    t_list.insert(name, hp, atk, dfn)
    cricket_list[(len(cricket_list) + 1)] = t_list


if __name__ == '__main__':
    cfp = open('cricket_list.json', 'w+')
    cricket_name = input()
    cricket_hp = input()
    cricket_atk = input()
    cricket_dfn = input()
    cricket_list_write_in(cricket_name, cricket_hp, cricket_atk, cricket_dfn)
    json.dump(cricket_list, cfp)
    cfp.close()



else:
    print(cricket_list)
