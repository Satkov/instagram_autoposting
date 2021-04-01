**Функция автопостинга в инстаграмм для приложения на IOS**

Суть работы:
Сервис получает на вход данные поста, который нужно опубликовать, и время его публикации. Далее планирует задачу по его публикациис помощью Django Q. Когда наступает время публикации сначала создаёт контейнер поста на сервере facebook, и сразу после этого публикует его.

**Алгоритм работы программы:**
Публикация.
Сервер получает post запрос с данными поста на /api/v1/posts/ ---> Валидирует данные и записывает их в модель Post ---> 
Cрабатывает сигнал post_save. Из сигнала идёт вызов фунции из q_manager.py, в которую передаётся ID поста --->
В q_manager создаётся задание и планируется на время, указаное в объекте. Записывает id задания в объект поста --->
Когда наступает время публикации, Django Q вызывает функцию Container, которая отправляет данные на сервер фб --->
Далее вызывается ContainerPublisher, который публикует загруженный ранее контейнер.

Редактирование.
После получения PATCH или PUT запросов и сохранения изменений в объект, вызывается сигнал post_save --->
С помощью id задания, которое мы сохранили в объект при его создании, мы находим объект schedule --->
Перезаписываем значение date_pub в schedule, на случай, если при изменении объекта было изменено время его публикации.

Удаление.
После получения  DELETE запроса вызывается сигнал pre_delete ---> по id находим объект schedule и удаляем его.

**Аутентификация:**
Чтобы совершать любой запрос к API, нужно иметь токен аутентификации пользователя. Чтобы его получить нужно отправить люгин и пароль вашего аккаунта в Body на /api/v1/api-token-auth/. Аккаунт создаётся через консоль администратора.
Полученый токен передаётся в заголовке.  Key - Authorization, Value - Token {your token}.

**Адрес для взаимодействия с API: /api/v1/posts/**

GET: В ответ на get запрос вернёт список всех постов. Чтобы получить один конкеретный пост нужно добавить его id на конце адреса: /api/v1/posts/4/

POST: Создаёт контейнер поста. В body можно передавать: "user_id" "caption" - null=True "url" "location_id"- null=True "user_tags"- null=True "thump_offset" - null=True "token" "date_pub" "content_type"

В "content_type" можно передать только Photo или Video Возвращает данные только что созданного объекта поста.

PATCH: Для редактирования поста нужно знать его id: /api/v1/posts/{id}/ Разрешено частичное обновление.

PUT: Меняет объект. Всё также как в PATCH, только запрос должен содержать как минимум все обязательные поля.

DELETE: /api/v1/posts/{id}/ - удаляет пост с указанным id.
