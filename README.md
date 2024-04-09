____________________________________________________________________________________
Проект
______________________________________________________________________________________

[Discord-bot с возможностью прослушивать музыку и сохранять]
Область: [Анализ данных, Новый программный продукт]
Автор проекта:
[Полянский Яков Андреевич]
Группа:
[3.008.1.20]


 
Краткая аннотация проекта 
Основная идея проекта - создание музыкального бота в дискорде с возможностью создания плейлистов на основе тегов выводимых нейросетью, проект направлен на пользователей discorrd, результатом может быть удобный и функциональный бот


Описание проблемы 
Основная проблема, которую решает проект - невозможность сохранения понравившейся музыки при прослушивании музыки с помощью ботов в discord, хотя эта возможность была бы очень кстати тк на данной платформе в основном собираются друзья и невозможность проигрывания хотя бы части уже проигранных треков одной командой вызывает фрустрацию.
 
Как это работает?
На вход боту в текстовом канале поступает команда с префиксом, бот подключается к голосовому каналу в котором сидел пользователь, который отправил сообщение, затем при помощи youtube-dl и ffmpeg бот скачивает и преобразовывает в необходимый формат для обработки, затем бот транслирует трек в голосовой канал с помощью того же ffmpeg, при необходимости пользователь может прописать дополнительную команду для сохранения трека в плейлист сервера. В отдельный текстовый документ сохраняется url трека, а также теги, сгенерированные нейросетью. Впоследствии пользователь может попросить бота проиграть плейлист с выбранным тегом.
 
 
Дизайн проекта:
данные: 
●	каталог музыки youtube

библиотеки/инструменты:
●	discord.py
●	youtube-dl
●	ffmpeg
●	os
●	musicnn
●	PyNaCl
●	time
●	numpy
●	tensorflow
●	nest_asyncho
Ссылка на программный код:
https://colab.research.google.com/drive/1GmhNAyeupOTAJ8eHlgF5tOPxb5piHSDn?usp=sharing
Ссылка на добавление бота в дискорд
https://discord.com/api/oauth2/authorize?client_id=1065218715869794314&permissions=8&scope=bot%20applications.commands
токен бота: MTA2NTIxODcxNTg2OTc5NDMxNA.GkUWXj.pauI4XEllkCB8Ex7qinGAXV3hkNvI-yO62JtQ4

 
Варианты развития проекта:
Вариантов развития данного проекта целая куча. Можно добавить команду для создания пользовательских плейлистов, можно добавить возможность отправления как трека так и его тегов пользователю в личные сообщения,
можно добавить стандартный функционал ботов-помощников, и наконец можно улучшить user-experience, то есть упростить ввод команд, добавить вспомогательные сообщения, улучшить визуальное оформления в текстовом канале,
добавить функции паузы и “перемотки”, добавление функции проигрывания всего плейлиста, не учитывая теги, добавление возможности задавать порядок воспроизведения песен из плейлиста,и улучшение скорости работы




Используемые источники:
1.	https://github.com/ytdl-org/youtube-dl
2.	https://github.com/jordipons/musicnn
3.	https://discordpy.readthedocs.io/en/stable/index.html
4.	https://www.youtube.com/watch?v=cVjXJlBYEt8&t=4316s
5.	https://www.youtube.com/watch?v=mOI-j7evA5Q&t=474s


