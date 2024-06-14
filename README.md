# auto_mailings

сервис управления рассылками, администрирования и получения статистики

___
Пример: компания N захотела создать на нашем сервисе рассылку. Создала для нее сообщение, которое будет отправлено
клиентам, наполнила базу клиентов своими данными с помощью графического интерфейса сайта, затем перешла к созданию
рассылки: указала необходимые параметры, сообщение и выбрала клиентов, которым эта рассылка должна быть отправлена.
___

- По умолчанию при запуске приложения автоматические рассылки выключены.
- Включить их можно в файле config.settings - переменная AUTO_MAILING.
- Так же в не зависимости от того запущенно приложение или нет вы можете воспользоваться командой 'python manage.py
  start_mailings' в терминале для едино-разового запуска рассылок

 /               | CRUD(create) | CRUD(read) | CRUD(update) | CRUD(delete) 
-----------------|--------------|------------|--------------|--------------
 Сущьности       | /            | /          | /            | /            
 Mailing         | +            | +          | +            | +            
 RecipientClient | +            | +          | +            | +            
 MailingMessage  | +            | +          | +            | +            
 HistoryMailing  | auto         | -          | -            | +            