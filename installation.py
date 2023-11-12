import subprocess

# Список библиотек, которые нужно установить
libraries_to_install = ['pyfiglet', 'matplotlib', 'sympy', 'numpy']

for library in libraries_to_install:
    try:
        subprocess.check_call(['pip', 'install', library])
        print(f'{library} успешно установлена.')
    except subprocess.CalledProcessError:
        print(f'Ошибка при установке {library}.')

print('Установка библиотек завершена.')