#!/usr/bin/env python
import players
import codecs
import random
import pprint

pp = pprint.PrettyPrinter(indent=4)

def import_players(file_name):
    return_list = []
    input_file = codecs.open(file_name, encoding='utf-8')
    
    for line in input_file.readlines()[1:]:
        return_list.append({'first_name': line.strip().split(',')[0].split(' ')[0],
                            'last_name': ' '.join(line.strip().split(',')[0].split(' ')[1:])})
    input_file.close()
    return return_list


def list_player_names():
    return players.players_list


def get_random_player():
    return random.choice(players.players_list)


def get_player(index):
    return players.players_list[index]


def print_random_player():
    name_object = get_random_player()
    print name_object['first_name'], name_object['last_name']


def main():
     print_random_player()

if __name__ == '__main__':
    main()