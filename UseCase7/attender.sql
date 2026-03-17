DELETE FROM group_lesson_participates
WHERE member_id IN (
    SELECT id 
    FROM member 
    WHERE mail IN (
		'johnny@stud.ntnu.no',
		'gina.giske@ntnu.no',
		'catrin-johansen@ntnu.no'
	)
);

INSERT INTO group_lesson_participates VALUES
((SELECT id FROM member WHERE mail = 'johnny@stud.ntnu.no'), 1, '2026-03-16 07:00'),
((SELECT id FROM member WHERE mail = 'johnny@stud.ntnu.no'), 2, '2026-03-16 16:30'),
((SELECT id FROM member WHERE mail = 'johnny@stud.ntnu.no'), 9, '2026-03-16 16:15');

INSERT INTO group_lesson_participates VALUES
((SELECT id FROM member WHERE mail = 'gina.giske@ntnu.no'), 2, '2026-03-16 16:30'),
((SELECT id FROM member WHERE mail = 'gina.giske@ntnu.no'), 5, '2026-03-16 19:00'),
((SELECT id FROM member WHERE mail = 'gina.giske@ntnu.no'), 9, '2026-03-17 18:30');

INSERT INTO group_lesson_participates VALUES
((SELECT id FROM member WHERE mail = 'catrin-johansen@ntnu.no'), 7, '2026-03-17 18:30'),
((SELECT id FROM member WHERE mail = 'catrin-johansen@ntnu.no'), 9, '2026-03-17 16:15');


WITH
chosen_month AS (
    SELECT '2026-03' AS month
),

attendance AS (
    SELECT member_id, COUNT(*) AS total_attendances
    FROM group_lesson_participates
    WHERE strftime('%Y-%m', date) = (SELECT month FROM chosen_month)
    GROUP BY member_id
),

max_attendance AS (
    SELECT MAX(total_attendances) AS max_attendances
    FROM attendance
)

SELECT member.name, member.mail, attendance.total_attendances
FROM attendance
JOIN member ON attendance.member_id = member.id
WHERE attendance.total_attendances = (SELECT max_attendances FROM max_attendance);