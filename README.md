Test - проект который мы рефакторим.

Остальной проект - отрефакторенная версия.

Rules - Правила для написания кода.

Архитектура приложений: 

Папка приложения/
│
├── model/               	# Модель (данные + логика)
│   ├── entityes/		# Сущности (User, Product)
│   ├── services/        	# Бизнес-логика (UserService)
│   └── UserRepository/    	# Работа с БД (UserRepository)
│
├── view/ 
|   ├── CustomControls/         # Кастомные контролы
|   ├── BaseFrame/          	# Главное окно
│   ├── BaseControls/	   	# Стандартные контролы
│   └── CustomWigets/        	# Кастомные виджеты
│	
│
├── db/                 	# База данных
│   ├── models.py       	# ORM-модели (SQLAlchemy/Peewee)
│   └── database.py     	# Инициализация БД
│
└── app.py		        # Точка входа (запуск приложения)
