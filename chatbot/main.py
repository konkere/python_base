#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bot import TlgrmBot, tlgrm_bot_logger
from aiogram import Dispatcher, executor, types


chatter = TlgrmBot()
dp = Dispatcher(chatter.bot)


@dp.message_handler(commands=chatter.commands.keys(), chat_id=chatter.config.chat_id)
async def commands(message: types.Message):
    """
    Функия обработки команд бота вида:
        /command
        /command@BotUsername
    """
    received_command = message.text[1:]
    interlocutor_name = message.from_user["first_name"]
    bot_response = f'{chatter.commands[received_command]}, {interlocutor_name}'
    await message.reply(bot_response)
    tlgrm_bot_logger.debug(f'Полученная команда и ответ бота:\n\t{received_command} → {bot_response}')


@dp.message_handler(chat_id=chatter.config.chat_id)
async def echo(message: types.Message):
    """
    Функция "Эхо", отправляющая полученное сообщение обратно
    """
    received_message = message.text
    bot_response = message.text
    await message.reply(received_message)
    tlgrm_bot_logger.debug(f'Полученное сообщение и ответ бота:\n\t{received_message} → {bot_response}')


if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception as exc:
        tlgrm_bot_logger.critical(exc)
