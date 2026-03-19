WITH
student_id AS (
    SELECT id member_id FROM member WHERE mail = 'johnny@stud.ntnu.no'
),
activity_id AS (
    SELECT id activity_id FROM activity_type WHERE name = 'Spin60'
),
lesson AS (
    SELECT group_lesson.id lesson_id, group_lesson.capacity
    FROM group_lesson
    JOIN room ON group_lesson.room_id = room.id
    JOIN center ON room.center_id = center.id
    JOIN lesson_types ON group_lesson.id = lesson_types.lesson_id
    WHERE group_lesson.time = '2026-03-17 18:30' 
      AND lesson_types.activity_type_id = (SELECT activity_id FROM activity_id)
),
current_booked_count AS (
    SELECT COUNT(*) count FROM group_lesson_booking 
    WHERE group_lesson_id = (SELECT lesson_id FROM lesson)
),
capacity_count AS (
    SELECT COUNT(*) count FROM group_lesson_booking 
    WHERE member_id = (SELECT member_id FROM student_id) 
      AND group_lesson_id = (SELECT lesson_id FROM lesson)
)

INSERT INTO group_lesson_booking (member_id, group_lesson_id, time_booked)
SELECT student_id.member_id, lesson.lesson_id, datetime('now')
FROM student_id, lesson, current_booked_count, capacity_count
WHERE capacity_count.count < lesson.capacity AND current_booked_count .count = 0;