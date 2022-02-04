""" Файл настроек. Для дальнейшей работы с проектом необходимо заполнить параметры в этом файле.

SCOPES — это перечень возможностей, которыми будет обладать сервис, созданный в скрипте (Google.Drive).
Примечание: если вы изменяете область доступа (SCOPES), удалите файл token.json.
Ссылка на официальную документацию: https://developers.google.com/identity/protocols/oauth2/scopes

Также для Google.Drive понадобятся учётные данные (credentials) для использования Google.Drive API.
Файл credentials нужно будет сохранить в формате JSON в пакете classes.
Ссылка на официальную документацию: https://developers.google.com/workspace/guides/create-credentials

yandex_token - ключ доступа (токен), полученный с полигона Яндекса.
Токен можно получить кликнув на полигоне на кнопку "Получить OAuth-токен"
Ссылка на Полигон Яндекса: https://yandex.ru/dev/disk/poligon/

vk_token - ключ доступа (токен) пользователя Вконтакте.
Ссылка на официальную документацию: https://dev.vk.com/api/access-token/getting-started

"""

SCOPES = ['']
yandex_token = ''
vk_token = ''