""" Файл настроек. Для дальнейшей работы с проектом необходимо заполнить параметры в этом файле.

SCOPES — это перечень возможностей, которыми будет обладать сервис, созданный в скрипте (Google.Drive).
Примечание: если вы изменяете область доступа (SCOPES), удалите файл token.json.
Ссылка на официальную документацию: https://developers.google.com/identity/protocols/oauth2/scopes

yandex_token - ключ доступа (токен), полученный с полигона Яндекса.
Ссылка на официальную документацию: https://yandex.ru/dev/oauth/doc/dg/concepts/about.html

vk_token - ключ доступа (токен) пользователя Вконтакте.
Ссылка на официальную документацию: https://dev.vk.com/api/access-token/getting-started

"""

SCOPES = ['https://www.googleapis.com/auth/drive']
yandex_token = 'AQAAAABZBSFqAADLW6okIGFmsk-ik4_y_9gAbUY'
vk_token = '855d728adeb373e5cb6467524fffabfd531dd997478521cdcb93724e36a69c4dc9b54931e9445a802a76d'