"""Файл, содержащий служебные переменные с постоянными значениями."""

main_menu = """
Главное меню:

Служебные команды:
/docs - вывести дополнительное меню документации программы,
/exit_save_all - выйти из программы, предварительно сохранив данные в лог программы,
/exit_not_save - выйти из программы без сохранения данных.

Команды для работы с VK API (от лица пользователя):
/get_photos – получить информацию о фотографиях пользователя (пользователей) Вконтакте,
/get_albums - получить информацию о фотоальбомах пользователя (пользователей) Вконтакте.

Команды для работы с Яндекс.Диском:
/get_files_yandex_disk - получить список файлов на Яндекс.Диске,
/create_directory_yandex_disk – создать папку на Яндекс.Диске с определённым именем,
/download_photos_yandex_disk – загрузить фото на Яндекс.Диск по определённому пути.

Команды для работы с Google.Drive:
/get_files_google_drive - получить список файлов на Google.Drive,
/create_directory_google_drive - создать папку на Google.Drive с определённым именем,
/download_photos_google_drive - загрузить фото на Google.Drive по определённому пути.
"""

documentation = """
Документация:

Файлы (документация):
/const_doc - документация файла const.py,
/settings_doc - документация файла settings.py.

Функции (документация)
/program_interface_doc - документация функции program_interface.

Класс VkUser (документация):
/VkUser_doc - документация класса VkUser,
/_error_validator_doc – документация метода _error_validator (является приватным),
/users_get_doc - документация метода users_get,
/get_albums_doc - документация метода get_albums,
/get_photos_doc – документация метода get_photos.

Класс YandexDisk (документация):
/YandexDisk_doc – документация класса YandexDisk,
/_error_validator_doc – документация метода _error_validator (является приватным),
/get_files_list_doc – документация метода get_files_list,
/create_directory_yandex_disk_doc – документация метода create_directory_yandex_disk,
/_download_files_doc – документация метода _download_files (является приватным),
/download_files_yandex_disk_doc - документация метода download_files_yandex_disk,
/delete_files_yandex_disk_doc - документация метода delete_files_yandex_disk.

Класс GoogleDrive (документация):
/GoogleDrive_doc – документация класса GoogleDrive,
/get_files_google_drive_doc - документация метода get_files_google_drive,
/create_directory_google_drive_doc - документация метода create_directory_google_drive,
/download_files_google_drive_doc - документация метода download_files_google_drive,
/delete_files_google_drive_doc - документация метода delete_files_google_drive.

/back - вернуться в главное меню.
"""