# BiWorks
Проект реализован при помощи фреймворка Django. Фреймворк Django реализует архитектурный паттерн MVT (Model-View-Template). 
По умолчанию фреймворк Django работает с базой данных SQLite3.
Для вёрстки веб-страниц использовались HTML и JavaScript.
Для использования веб-приложения пользователю необходимо зарегистрироваться, обязательно с указанием почтового адреса для дальнейшей двухфакторной аутентификации. 
После успешной регистрации пользователь авторизируется, после чего ему становятся доступны разделы сайта:

•	Раздел “Feed” – данный раздел представляет собой «ленту» из объявлений;

•	Раздел “Home” – в данном разделе пользователь может заполнить форму для того, чтобы разместить объявление, а также посмотреть все свои 
размещенные и объявления, и все принятые заказы;

•	Раздел “Profile” – содержит личные данные о пользователе. 

Для каждого размещенного объявления указано описание задачи и установлена стоимость, а также есть возможность оставить фотографию. 
Контактная информация (например, телефонный номер для связи или же адрес электронной почты) становится доступной только после того, как какой-либо пользователь 
берет на себя задачу.
Помимо этого, есть возможность поиска. Поиск осуществляется по имени пользователя, ключевым словам в записи или же по номеру тега у объявления. 

Также определены API, с помощью которого можно взаимодействовать с базой данных. 
В работе использовался класс APIView. Используется декоратор api_view, который принимает список методов HTTP, на которые должно реагировать представление.
По умолчанию принимаются только методы GET, поэтому декоратору необходимо явно указать, какие методы должно допускать представление. 
В разрабатываемом проекте API были реализованы для приложений Profiles, T_messages и Threads.

Данное веб-приложение размещено на хостинге и доступно по ссылке https://lavax.pythonanywhere.com/login/.
