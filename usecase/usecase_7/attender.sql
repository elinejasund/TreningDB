WITH attendance_plan(mail, lesson_time) AS (
    VALUES
		('johnny@stud.ntnu.no', '2025-03-16 07:00'),
        ('johnny@stud.ntnu.no', '2025-03-16 16:30'),
        ('gina.giske@ntnu.no', '2025-03-16 16:30'),
        ('gina.giske@ntnu.no', '2025-03-16 17:40'),
        ('catrin-johansen@ntnu.no', '2025-03-17 18:30')
),

member_ids AS (
    SELECT id, mail FROM member
),

lesson_ids AS (
    SELECT id AS lesson_id, time FROM group_lesson
)

INSERT OR IGNORE INTO group_lesson_participates(member_id, group_lesson_id, date)
SELECT m.id, l.lesson_id, t.lesson_time
FROM attendance_plan t
JOIN member_ids m ON m.mail = t.mail
JOIN lesson_ids l ON l.time LIKE t.lesson_time || '%';

WITH attendance AS (
    SELECT member_id, COUNT(*) AS total_attendances
    FROM group_lesson_participates
    WHERE date LIKE '2025-03%'
    GROUP BY member_id
),
max_attendance AS (
    SELECT MAX(total_attendances) AS max_number
    FROM attendance
)
SELECT m.name, m.mail, a.total_attendances
FROM attendance a
JOIN member m ON m.id = a.member_id
WHERE a.total_attendances = (SELECT max_number FROM max_attendance);