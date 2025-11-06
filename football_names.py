#!/usr/bin/env python
import players
import codecs
import random
import pprint
import csv

pp = pprint.PrettyPrinter(indent=4)

class PlayerDatabase(object):
    def __init__(self, player_list):
        self.player_list = player_list
        print(len(player_list))

    def get_player_list(self):
        return self.player_list

    def get_random_player(self):
        return random.choice(self.player_list)

class Player(object):
    def __init__(self, last_name):
        self.first_name = None
        self.last_name = last_name
        self.nationality = None
        self.appearances = None
        self.goals = None

    def __str__(self):
        return "<" + self.first_name + ", " + str(self.last_name) + ", " + str(self.nationality) + ", " + \
               str(self.appearances) + ", " + str(self.goals) + ">"

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_nationality(self, nationality):
        self.nationality = nationality

    def set_appearances(self, appearances):
        self.appearances = appearances

    def set_goals(self, goals):
        self.goals = goals

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name


def import_players_from_csv(file_name):
    return_list = []
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)

        for row in csv_reader:
            player = Player(row[1])
            player.set_first_name(row[0])
            player.set_nationality(row[2])
            player.set_appearances(row[3])
            player.set_goals(row[4])
            return_list.append(player)
    return return_list


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
    print(name_object['first_name'], name_object['last_name'])


def main():
    player_db = PlayerDatabase(import_players_from_csv('players.csv'))
    print(player_db.get_random_player())


if __name__ == '__main__':
    main()
