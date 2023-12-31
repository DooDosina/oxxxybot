
from telebot import TeleBot, types

bot = TeleBot(token='6610591093:AAHdhEr6MzWCdpxZ47Lr6i0n8mIdFfa2ITA', parse_mode='html') # создание бота


DEFINITOINS = {
    'кирилл': 'Kахилл, хлорофилл ,горилл, берилл, бацилл, вилл ,восстановил, решил, заплатил, соединил',
    'данила': 'пропустила превратила приступила сократила грозила отпустила руководила освободила изучила входила поразила',
    'герман': 'разгневан перегнан перемешан перерезан растерзан начертан набеган перебран разрезан нарезан',
    'даня': 'одурманя папаня юаня маманя аня ваня дурманя маня мишаня саня таня чеканя забарабаня горланя',
    'искандер': 'андер тандер эспандер экспандер хедхантер декантер брандер хантер',
    'катя': 'растратя батя татя истратя патя затратя потратя тратя взлохматя утратя сертификате окладе благодати',
    'маша': 'ошараша папаша мамаша чаша ералаша каша простокваша патронташа аркаша глаша даша любаша',
    'саша': 'ошараша папаша мамаша чаша ералаша каша простокваша патронташа аркаша глаша даша любаша',
    'алена': 'молодожёна гранёна золочёна клёна темно-зелёна плетёна копчёна матрёна настёна калёна светло-зелёна',
    'тимур': 'чересчур евротур гламур кур лемур шампур архитектур винокур трубадур ажур сур балагур понур',
    'арина': 'дедовщина вражина оленина инсулина господина аргентина антонина ангелина альбина алина ирина',
    'сережа': 'надёжа обнадёжа искорёжа лёжа схожа прохожа цветоложа тёша перехожа перемножа уничтожа',
    'женя': 'феня обесценя женьшеня беня веня деня ксеня сеня пельменя пеня оленя тюленя бюллетеня мена фена',
    'тема': 'окоёма водоёма проёма подъёма приёма артёма дёма кулёма сёма чернозёма дрёма объёма стрёма старпома',
    'катерина': 'рубина мужчина змеина мышина дружина лимузина пучина графина свинина сердцевина кувшина балерина',
    'вадим': 'пурим мейнстрим засим экстрим интим родим дадим глухим заговорим посетим превратим сократим грозим',
    'ксюша': 'клуша дорогуша баклуша агуша обезоружа руша стужа павлуша маркуша куша копуша завьюжа жужа',
    'ника': 'клубника шика улика гвоздика пика блика вика базилика брусника черника тика таджика многолика',
    'лена': 'спортсмена отмена бизнесмена замена эвглена гиена стена размена супермена кузена рекордсмена гобелена',
    'настя': 'дитя полушутя сплетя учтя возместя известя пыхтя слетя покрутя сместя сколотя шелестя отлетя раскрутя',
    'оля': 'моля пароля дозволя изволя алкоголя уволя воля кроля коля контроля николя самоконтроля соизволя',
    'андрей': 'дисплей ессей сенсей спидвей хайвей диджей кащей старлей ей-ей взашей прохиндей убей основней потемней посвежей податей пропастей',
}



@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):

    bot.send_message(
        chat_id=message.chat.id, 
        text='Привет, на связи Оксибот, пиши имя, сейчас зарифмуем!', 
    )
    sti = open('oxxxy_hello.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

@bot.message_handler()
def message_handler(message: types.Message):
    definition = DEFINITOINS.get(
        message.text.lower(), 
    )

    if definition is None:
        bot.send_message(
            chat_id=message.chat.id,
            text='😋 Пока подходящих рифм нет',
        )
        sis = open('nelovko.webp', 'rb')
        bot.send_sticker(message.chat.id, sis),

        return

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Вот твои рифмы:\n<code>{definition}</code>',
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Жду следующее имя',
    )

def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
