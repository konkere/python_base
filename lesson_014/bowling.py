# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Throw(metaclass=ABCMeta):

    @abstractmethod
    def digit(self, throws) -> int:
        pass

    @abstractmethod
    def special(self) -> int:
        pass


class ThrowFirst(Throw):

    def __init__(self):
        self.throw = 0

    def digit(self, throws) -> int:
        return int(throws[self.throw])

    def special(self) -> int:
        return 20


class ThrowSecond(Throw):

    def __init__(self):
        self.throw = 1

    def digit(self, throws) -> int:
        return int(throws[self.throw])

    def special(self) -> int:
        return 15


class Frame:

    def __init__(self, state, throws) -> None:
        self.throws = throws
        self._state = state
        self.points = 0
        self.special_symb = ['X', '/']
        self.count()

    def change_state(self, state) -> None:
        self._state = state
        self.count()

    def count(self):
        symbol = self.throws[self._state.throw]
        sp_symbol = self.special_symb[self._state.throw]
        if symbol == sp_symbol:
            self.points = self._state.special()
        elif symbol.isdigit():
            number = self._state.digit(self.throws)
            self.points += number
            if self.points > 10 and number != 0:
                raise SyntaxError('Ошибка формата фрейма (кеглей не может быть больше 10)')
            elif self.points == 10:
                self.points = 15
        else:
            raise SyntaxError('Ошибка формата фрейма (неизвестные символы)')


def score_by_frame(throws):
    result_names = {
        'strike': 20,
        'spare': 15,
    }
    if throws[0] == 'X':
        return result_names['strike']
    elif throws[0].isdigit() and throws[1] == '/':
        return result_names['spare']
    elif throws[0].isdigit() and throws[1].isdigit() and (int(throws[0]) + int(throws[1])) < 11:
        frame_sum = int(throws[0]) + int(throws[1])
        return frame_sum
    else:
        raise SyntaxError('Ошибка формата фрейма')


def get_score(game_result):
    if '0' in game_result:
        raise SyntaxError('Ошибка формата результатов (недопустимый символ)')
    score = 0
    game_result_x2 = game_result.replace('X', 'X0').replace('-', '0')
    symbols = len(game_result_x2)
    if not symbols % 2 == 0:
        raise SyntaxError('Ошибка количества бросков во фрейме')
    elif symbols > 20:
        raise SyntaxError('Ошибка количества фреймов (не более 10)')
    throw_state_1 = ThrowFirst()
    throw_state_2 = ThrowSecond()
    for frame_step in range(0, len(game_result_x2), 2):
        throw_1 = game_result_x2[frame_step]
        throw_2 = game_result_x2[frame_step + 1]
        # score += score_by_frame([throw_1, throw_2])
        frame = Frame(throw_state_1, [throw_1, throw_2])
        frame.change_state(throw_state_2)
        score += frame.points
    return score
