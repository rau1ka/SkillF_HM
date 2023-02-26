import telebot
from config import TOKEN, keys
from extensions import ConvertionException, CryptoConverter, DeclensionByCases

bot = telebot.TeleBot(TOKEN)

keys = {
    'биткоин': 'BTC',
    'эфириум': 'ETH',
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB'
}

@bot.message_handler(commands=['start', 'help'])
def help(message:telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты> \ <в какую валюту перевести> \ <кол-во переводимой валюты> \n <Увидеть список доступных валют: /values>'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def help(message:telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

# @bot.message_handler(content_types=['text', ])
# def convert(message:telebot.types.Message):
#     quote, base, amount = message.text.split(' ')
#     r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
#     total_base  = json.loads(r.content)[keys[base]]
#     text = f'Цена {amount} {quote} в {base} - {total_base}'
#     bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Количество параметров не совпадает. Используйте формат:\n<имя валюты> ' \
           '<в какую валюту перевести> <количество переводимой валюты> \n')

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя:\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        inclined_quote = DeclensionByCases(quote, float(amount))
        inclined_base = DeclensionByCases(base, float(total_base))
        quote = inclined_quote.incline()
        base = inclined_base.incline()
        text = f'{amount} {quote} = {total_base} {base}'
        bot.send_message(message.chat.id, text)
        
    
bot.polling()

