# my_own_namespace.yandex_cloud_elk

Коллекция Ansible с кастомным модулем для создания файлов на удаленных хостах.

## Установка

Из Git репозитория
bash
ansible-galaxy collection install git+https://github.com/SLzDevOps/my_own_collection.git

Из локального архива
bash
ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz

Модули
my_own_module
Создает текстовый файл на указанном хосте с заданным содержимым.

Параметры
Параметр	Тип	Обязательный	По умолчанию	Описание
path	str	yes	-	Абсолютный путь к файлу для создания
content	str	yes	-	Содержимое файла
Примеры
Создание файла:

yaml
- name: Create a file with my module
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/example.txt
    content: "Hello, Ansible!"
  
В составе роли:
yaml
- name: Create file from role
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: "{{ my_own_module_path }}"
    content: "{{ my_own_module_content }}"

Возвращаемые значения
Ключ	Тип	Описание
path	str	Путь к созданному файлу
content	str	Содержимое файла
changed	bool	Был ли файл создан или изменен

Роли
my_test_role
Демонстрационная роль для использования модуля my_own_module.

Переменные роли
Имя	Значение по умолчанию	Описание
my_own_module_path	/tmp/default_ansible_file.txt	Путь к создаваемому файлу
my_own_module_content	"Default content from role"	Содержимое файла
Пример использования
yaml
- name: Use my_test_role with custom parameters
  hosts: localhost
  vars:
    my_own_module_path: /tmp/custom_file.txt
    my_own_module_content: "Custom content"
  roles:
    - my_test_role

Тестирование
Проверка идемпотентности

Модуль поддерживает идемпотентность:
При первом запуске файл создается (changed=true)
При повторном запуске с тем же содержимым изменений нет (changed=false)

