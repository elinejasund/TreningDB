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