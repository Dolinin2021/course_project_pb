import json
from google_drive import GoogleDrive
from ya_disk import YandexDisk
from vk_classes import VkUser
from settings import vk_token, yandex_token
from const import main_menu, documentation
from pprint import pprint


def program_interface():
    """
    Функция, реализующая интерфейс программы.

    Exceptions
    ----------
    ValueError - возникает при несоответствии типов
    (при вводе ожидался тип int, а был принят на вход тип str),
    либо при отсутствии значения на этапе ввода данных,
    либо при несоблюдении принятого формата ввода данных.

    TypeError - возникает при передаче пустого значения
    служебной переменной или аргумента в какой-либо метод,
    либо цикл.

    UnboundLocalError - возникает при текущем обращении к методам,
    которые требуют в качестве аргумента переменную,
    но на момент обращения эта переменная не была объявлена.

    """

    log_photos_list = []
    log_albums_list = []

    temp_photos_list = []
    temp_albums_list = []
    google_drive_files_list = []

    temp_photos_set = set()
    disk_files_set = set()
    delete_files_set = set()

    vk_client = VkUser(vk_token, '5.131')
    yandex_disk = YandexDisk(yandex_token)
    google_disk = GoogleDrive()


    print('Вас приветствует программа по работе с файлами компании Python Software.\n'
        'Ознакомьтесь с главным меню перед тем, как продолжить.')
    print(main_menu)


    while True:

        print()
        user_input = input('Введите команду: ')
        print()

        if user_input == '/docs':
            print(documentation)

        elif user_input == '/program_interface_doc':
            print(program_interface.__doc__)

        elif user_input == '/VkUser_doc':
            print(VkUser.__doc__)

        elif user_input == '/_error_validator_doc':
            print(VkUser._error_validator.__doc__)

        elif user_input == '/users_get_doc':
            print(VkUser.users_get.__doc__)

        elif user_input == '/get_albums_doc':
            print(VkUser.get_albums.__doc__)

        elif user_input == '/get_photos_doc':
            print(VkUser.get_photos.__doc__)

        elif user_input == '/YandexDisk_doc':
            print(YandexDisk.__doc__)

        elif user_input == '/_error_validator_doc':
            print(YandexDisk._error_validator.__doc__)

        elif user_input == '/get_files_list_doc':
            print(YandexDisk.get_files_list.__doc__)

        elif user_input == '/create_directory_yandex_disk_doc':
            print(YandexDisk.create_directory_yandex_disk.__doc__)

        elif user_input == '/_download_files_doc':
            print(YandexDisk._download_files.__doc__)

        elif user_input == '/download_files_yandex_disk_doc':
            print(YandexDisk.download_files_yandex_disk.__doc__)

        elif user_input =='/delete_files_yandex_disk_doc':
            print(YandexDisk.delete_files_yandex_disk.__doc__)

        elif user_input == '/GoogleDrive_doc':
            print(GoogleDrive.__doc__)

        elif user_input == '/get_files_google_drive_doc':
            print(GoogleDrive.get_files_google_drive.__doc__)

        elif user_input == '/create_directory_google_drive_doc':
            print(GoogleDrive.create_directory_google_drive.__doc__)

        elif user_input == '/download_files_google_drive_doc':
            print(GoogleDrive.download_files_google_drive.__doc__)

        elif user_input == '/delete_files_google_drive_doc':
            print(GoogleDrive.delete_files_google_drive.__doc__)

        elif user_input == '/back':
            print(main_menu)

        elif user_input == '/exit_not_save':
            print()
            print('Python Software, 2021. Все права защищены.')
            break

        try:

            if user_input == '/get_photos':

                album_id = str(input('Введите индентификатор альбома (wall, profile, saved): '))
                print()

                rev = int(input('Введите порядок сортировки (1 — антихронологический, 0 — хронологический): '))
                print()

                user_ids = str(input('Введите имя пользователя (или пользователей через запятую, без пробелов) (screen_name): '))
                print()

                count = int(input('Введите количество запрашиваемых фотографий: '))
                print()

                owner_id = vk_client.users_get(user_ids)

                for id in owner_id:
                    photo_info = vk_client.get_photos(album_id, rev, id['id'], count)
                    temp_photos_list.append(photo_info)
                    if photo_info is None:
                        print('Нет данных для сохранения.')

                    else:
                        for log_photos in photo_info:
                            log_photos_list.append({'file_name': log_photos['file_name'], 'size': log_photos['size']})

                    print('\nСписок файлов пользователя (пользователей):\n')
                    pprint(temp_photos_list)

            elif user_input == '/get_albums':

                user_ids = str(input('Введите имя пользователя (или пользователей через запятую) (screen_name): '))
                print()

                count = int(input('Введите количество запрашиваемых альбомов: '))
                print()

                owner_id = vk_client.users_get(user_ids)
                for id in owner_id:
                    albums_info = vk_client.get_albums(id['id'], count)
                    if albums_info is None:
                        print('Нет данных для сохранения.')

                    else:
                        temp_albums_list.append(albums_info)
                        log_albums_list.append(albums_info)
                        print()
                        print('\nСписок альбомов пользователя:\n')
                        pprint(temp_albums_list)
                        temp_albums_list.clear()

            elif user_input == '/create_directory_yandex_disk':
                path = str(input('Введите имя создаваемой папки: '))
                create = yandex_disk.create_directory_yandex_disk(path)

            elif user_input == '/download_photos_yandex_disk':
                get_files_list = yandex_disk.get_files_list()
                for get in get_files_list:
                    disk_files_set.add(get['file_name'])

                path = str(input('\nВведите имя папки, куда следует загрузить файл: '))

                for info in temp_photos_list:
                    for value in info:
                        if value['file_name'] in disk_files_set:
                            delete_files_set.add(value['file_name'])

                for file_name in delete_files_set:
                    delete = yandex_disk.delete_files_yandex_disk(f"{path}/{file_name}")

                for load in temp_photos_list:
                    download = yandex_disk.download_files_yandex_disk(path, load)

                disk_files_set.clear()
                delete_files_set.clear()
                temp_photos_list.clear()

            elif user_input == '/create_directory_google_drive':
                name = str(input('Введите имя создаваемой папки: '))
                create = google_disk.create_directory_google_drive(name)

            elif user_input == '/get_files_google_drive':
                get = google_disk.get_files_google_drive()
                pprint(get)

            elif user_input == '/download_photos_google_drive':
                folder_id = str(input('Введите идентификатор папки: '))
                get_files_list_on_google_disk = google_disk.get_files_google_drive()

                for get in get_files_list_on_google_disk:
                    google_drive_files_list.append(
                        {
                            'id': get['id'],
                            'file_name': get['name']
                        }
                    )

                for info in temp_photos_list:
                    for value in info:
                        temp_photos_set.add(value['file_name'])

                for value in google_drive_files_list:
                    if value['file_name'] in temp_photos_set:
                        delete_files_set.add(value['id'])

                for fileId in delete_files_set:
                    delete = google_disk.delete_files_google_drive(fileId)

                for load in temp_photos_list:
                    download = google_disk.download_files_google_drive(folder_id,load)

                google_drive_files_list.clear()
                temp_photos_list.clear()
                temp_photos_set.clear()
                delete_files_set.clear()

            elif user_input == '/exit_save_all':

                with open('log_photos.json', 'w', encoding='utf-8') as file_obj:
                    print()
                    print('Происходит сохранение данных о фото в лог log_photos.json, пожалуйста, подождите...')
                    json.dump(log_photos_list, file_obj, ensure_ascii=False, indent=4)

                with open('log_albums.json', 'w', encoding='utf-8') as file_obj:
                    print()
                    print('Происходит сохранение данных об альбомах в лог log_albums.json, пожалуйста, подождите...')
                    json.dump(log_albums_list, file_obj, ensure_ascii=False, indent=4)

                print()
                print('Данные успешно сохранены.')
                print()
                print('Python Software, 2021. Все права защищены.')
                break

        except ValueError:
            print()
            print('Возникло исключение ValueError: несоответствие типов при вводе данных.\n'
                  'Программа продолжает работу в штатном режиме.\n')

        except TypeError:
            print()
            print('Возникло исключение TypeError: передано пустое значение служебной переменной или аргумента.\n'
                  'Программа завершает свою работу...\n')
            exit()

        except UnboundLocalError:
            print()
            print('Возникло исключение UnboundLocalError.\n'
                  'Прежде,чем использовать метод download_files_yandex_disk или кнопку exit_save_all, необходимо получить данные с помощью метода get_photos()\n'
                  'Программа продолжает работу в штатном режиме.\n')