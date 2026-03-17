WITH
selectedMember AS (
    SELECT id AS member_id FROM member WHERE mail = 'johnny@stud.ntnu.no'
),
activity AS (
    SELECT id AS activity_id FROM activity_type WHERE name = 'Spin60'
),
lesson AS (
    SELECT group_lesson.id AS lesson_id, group_lesson.capacity
    FROM group_lesson
    JOIN room ON group_lesson.room_id = room.id
    JOIN center ON room.center_id = center.id
    JOIN lesson_types ON group_lesson.id = lesson_types.lesson_id
    WHERE group_lesson.time = '2025-03-17 18:30' 
      AND center.name = 'Øya treningssenter' 
      AND lesson_types.activity_type_id = (SELECT activity_id FROM activity)
)
INSERT INTO group_lesson_participates (member_id, group_lesson_id, date)
SELECT member_id, lesson_id, datetime('now')
FROM selectedMember, lesson;