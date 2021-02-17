# -*- coding: utf-8 -*-

import os.path
from bowling import get_score
from collections import defaultdict


def tours(file_in):
    with open(file_in, 'r', encoding='utf8') as file:
        tour_block = {}
        for line in file:
            if '### Tour' in line:
                tour = int(line.split(' ')[2][:-1])
            elif 'winner is .........' in line:
                yield tour, tour_block
            elif line == '\n':
                tour_block = {}
            else:
                line = line[:-1]
                name, result = line.split('\t')
                tour_block[name] = result


def sorter_by_value(block):
    sorted_block = sorted(block.items(), key=lambda item: item[1], reverse=True)
    return sorted_block


class ToursParser:

    def __init__(self, file_in, file_out):
        self.file_errors = 'tournament_errors.txt'
        self.file_in = file_in
        if file_out:
            self.file_out = file_out
        else:
            self.file_out = 'tournament_result.txt'
        self.dummy_winner = 'Нет победителя!'
        self.member_games = defaultdict(int)
        self.member_wins = defaultdict(int)
        self.winners = {}
        self.tour_blocks = {}
        self.errors = {}

    def run(self):
        for tour, tour_block in tours(self.file_in):
            self.block_parse(tour, tour_block)

    def block_parse(self, tour, tour_block):
        members_scores = {}
        tour_block_new = {}
        errors = {}
        for name in tour_block:
            try:
                score = get_score(tour_block[name])
            except SyntaxError:
                errors[name] = tour_block[name]
            else:
                self.member_games[name] += 1
                members_scores[name] = score
                tour_block_new[name] = [tour_block[name], score]
        try:
            tour_block_winner = sorter_by_value(members_scores)[0][0]
        except IndexError:
            tour_block_winner = self.dummy_winner
        self.winners[tour] = tour_block_winner
        self.member_wins[tour_block_winner] += 1
        self.tour_blocks[tour] = tour_block_new
        if errors:
            self.errors[tour] = errors

    def tournament_result_out(self):
        if os.path.exists(self.file_out):
            os.remove(self.file_out)
        for tour in self.tour_blocks:
            with open(self.file_out, mode='a') as file:
                line = f'### Tour {tour}\n'
                file.write(line)
            for name in self.tour_blocks[tour]:
                with open(self.file_out, mode='a') as file:
                    game_result, score = self.tour_blocks[tour][name]
                    need_spaces = 24 - len(game_result)
                    divider = ' ' * need_spaces
                    line = f'{name}\t{game_result}{divider}{score}\n'
                    file.write(line)
            with open(self.file_out, mode='a') as file:
                winner = self.winners[tour]
                line = f'winner is {winner}\n\n'
                file.write(line)
        if self.errors:
            self.tournament_errors_out()

    def tournament_errors_out(self):
        if os.path.exists(self.file_errors):
            os.remove(self.file_errors)
        for tour in self.errors:
            with open(self.file_errors, mode='a') as file:
                line = f'### Tour {tour}\n'
                file.write(line)
            for name in self.errors[tour]:
                with open(self.file_errors, mode='a') as file:
                    err_result = self.errors[tour][name]
                    line = f'{name}\t{err_result}\n'
                    file.write(line)
            with open(self.file_errors, mode='a') as file:
                line = f'\n'
                file.write(line)

    def tournament_stat_out(self):
        if self.dummy_winner in self.member_wins:
            del self.member_wins[self.dummy_winner]
        print('╔' + '═' * 11 + '╤' + '═' * 16 + '╤' + '═' * 13 + '╗')
        print('║{member:^11}│{games:^16}│{wins:^13}║'.format(member='Игрок',
                                                             games='сыграно матчей',
                                                             wins='всего побед'))
        print('╠' + '═' * 11 + '╪' + '═' * 16 + '╪' + '═' * 13 + '╣')
        winners = sorter_by_value(self.member_wins)
        for name, wins in winners:
            print('║{member:^11}│{games:^16}│{wins:^13}║'.format(member=name,
                                                                 games=self.member_games[name],
                                                                 wins=wins))
        print('╚' + '═' * 11 + '╧' + '═' * 16 + '╧' + '═' * 13 + '╝')
