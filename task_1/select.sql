-- 1. Отримати всі завдання певного користувача
SELECT *
FROM tasks
WHERE user_id = 25;

-- 2. Вибрати завдання за певним статусом
SELECT *
FROM tasks
WHERE status_id = (SELECT id FROM status WHERE name = 'in review');

-- 3. Оновити статус конкретного завдання
UPDATE tasks
SET status_id = (SELECT id FROM status WHERE name = 'completed')
WHERE id = 138;

-- 4. Отримати список користувачів, які не мають жодного завдання
SELECT *
FROM users
WHERE id NOT IN (SELECT user_id FROM tasks);

-- 5. Додати нове завдання для конкретного користувача
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('Тестове завдання №1', 'Опис тестового завдання №1', (SELECT id FROM status WHERE name = 'assigned'), 19);

-- 6. Отримати всі завдання, які ще не завершено
SELECT *
FROM tasks
WHERE status_id <> (SELECT id FROM status WHERE name = 'completed');

-- 7. Видалити конкретне завдання
DELETE
FROM tasks
WHERE id = 127;

-- 8. Оновити ім'я користувача та пошту
UPDATE users
SET name = "Ihor Rukavitsyn" AND email = "ihor@goit.com"
WHERE id = 18;

-- 9. Знайти користувачів з певною електронною поштою
SELECT *
FROM users
WHERE email LIKE '%@goit.com';

-- 10. Отримати кількість завдань для кожного статусу
SELECT status.name, COUNT(tasks.id)
FROM status
LEFT JOIN tasks ON status.id = tasks.status_id
GROUP BY status.name;

-- 11. Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти
SELECT tasks.*
FROM tasks
JOIN users ON tasks.user_id = users.id
WHERE users.email LIKE '%@goit.com';

-- 12. Отримати список завдань, що не мають опису
SELECT *
FROM tasks
WHERE description IS NULL
   OR description = '';

-- 13. Вибрати користувачів та їхні завдання, які є у статусі "в процесі"
SELECT users.name, tasks.title
FROM users
INNER JOIN tasks ON users.id = tasks.user_id
WHERE tasks.status_id = (SELECT id FROM status WHERE name = 'in progress');

-- 14. Отримати користувачів та кількість їхніх завдань
SELECT users.name, COUNT(tasks.id) AS task_count
FROM users
LEFT JOIN tasks ON users.id = tasks.user_id
GROUP BY users.name;