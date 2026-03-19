WITH attendance AS (
    SELECT member_id, COUNT(*) AS total_attendances
    FROM group_lesson_participates
    WHERE date LIKE '2026-03%'
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