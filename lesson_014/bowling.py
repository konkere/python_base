# -*- coding: utf-8 -*-

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
    score = 0
    game_result_x2 = game_result.replace('X', 'X0').replace('-', '0')
    symbols = len(game_result_x2)
    if not symbols % 2 == 0:
        raise SyntaxError('Ошибка количества бросков во фрейме')
    elif symbols > 20:
        raise SyntaxError('Ошибка количества фреймов (не более 10)')
    for frame_step in range(0, len(game_result_x2), 2):
        throw_1 = game_result_x2[frame_step]
        throw_2 = game_result_x2[frame_step + 1]
        score += score_by_frame([throw_1, throw_2])
    return score
