-- Legg inn treningssenter, saler, noen sykler, noen brukere, noen trenere og treninger som nevnt over.
-- Her er trenere lagt inn som et form for medlem innenfor gruppetimen

--Treningsentere 
INSERT OR IGNORE INTO center VALUES
(1, "Vangslundsgate 2, 7030, Trondheim", "Øya treningssenter", 1, 1),
(2, "Moholt allmenning 12, 7050, Trondheim", "Moholt treningssenter", 0, 1),
(3, "Chr. Frederiks gate 20, 7030, Trondheim", "Gløshaugen idrettsbygg", 1, 1),
(4, "Loholt allé 81, 7049, Trondheim", "Dragvoll idrettssenter", 1, 1);

-- Saler
INSERT OR IGNORE INTO room VALUES
(1, 1, "spinningssal", 40),
(2, 1, "gruppetreningssal", 30),
(3, 1, "gruppetreningssal", 45),
(4, 1, "gruppetreningssal", 15),
(5, 4, "spinningssal", 20);

-- Sykler
INSERT OR IGNORE INTO bike VALUES
(1, 1, "Titan Life Indoor Bike S72", 0),
(2, 1, "Titan Life Indoor Bike S72", 0),
(3, 1, "Titan Life Indoor Bike S72", 0),
(4, 1, "Titan Life Indoor Bike S72", 0),
(5, 1, "Titan Life Indoor Bike S72", 0),
(6, 1, "Titan Life Indoor Bike S72", 0),
(7, 1, "Titan Life Indoor Bike S72", 0),
(8, 1, "Titan Life Indoor Bike S72", 0),
(9, 1, "Titan Life Indoor Bike S72", 0),
(10, 1, "Titan Life Indoor Bike S72", 0),
(11, 1, "Titan Life Indoor Bike S72", 0),
(12, 1, "Titan Life Indoor Bike S72", 0),
(13, 1, "Titan Life Indoor Bike S72", 0),
(14, 1, "Titan Life Indoor Bike S72", 0),
(15, 1, "Titan Life Indoor Bike S72", 0),
(16, 1, "Titan Life Indoor Bike S72", 0),
(17, 1, "Titan Life Indoor Bike S72", 0),
(18, 1, "Titan Life Indoor Bike S72", 0),
(19, 1, "Titan Life Indoor Bike S72", 0),
(20, 1, "Titan Life Indoor Bike S72", 0),
(21, 1, "Titan Life Indoor Bike S72", 0),
(22, 1, "Titan Life Indoor Bike S72", 0),
(23, 1, "Titan Life Indoor Bike S72", 0),
(24, 1, "Titan Life Indoor Bike S72", 0),
(25, 1, "Titan Life Indoor Bike S72", 0),
(26, 1, "Titan Life Indoor Bike S72", 0),
(27, 1, "Titan Life Indoor Bike S72", 0),
(28, 1, "Titan Life Indoor Bike S72", 0),
(29, 1, "Titan Life Indoor Bike S72", 0),
(30, 1, "Titan Life Indoor Bike S72", 0),
(31, 1, "Titan Life Indoor Bike S72", 0),
(32, 1, "Titan Life Indoor Bike S72", 0),
(33, 1, "Titan Life Indoor Bike S72", 0),
(34, 1, "Titan Life Indoor Bike S72", 0),
(35, 1, "Titan Life Indoor Bike S72", 0),
(36, 1, "Titan Life Indoor Bike S72", 0),
(37, 1, "Titan Life Indoor Bike S72", 0),
(38, 1, "Titan Life Indoor Bike S72", 0),

(39, 5, "ICG IC7", 1),
(40, 5, "ICG IC7", 1),
(41, 5, "ICG IC7", 1),
(42, 5, "ICG IC7", 1),
(43, 5, "ICG IC7", 1),
(44, 5, "ICG IC7", 1),
(45, 5, "ICG IC7", 1),
(46, 5, "ICG IC7", 1),
(47, 5, "ICG IC7", 1),
(48, 5, "ICG IC7", 1),
(49, 5, "ICG IC7", 1),
(50, 5, "ICG IC7", 1),
(51, 5, "ICG IC7", 1),
(52, 5, "ICG IC7", 1),
(53, 5, "ICG IC7", 1),
(54, 5, "ICG IC7", 1),
(55, 5, "ICG IC7", 1),
(56, 5, "ICG IC7", 1),
(57, 5, "ICG IC7", 1),
(58, 5, "ICG IC7", 1);

-- Brukere
INSERT OR IGNORE INTO member VALUES
(2, "Gina Giske", "gina.giske@ntnu.no", "22334455"),
(3, "Catrin Johansen", "catrin-johansen@ntnu.no", "33445566"),
(4, "Tobi Haugrønning", "tbh@ntnu.no", "44556677"),
(5, "Erlend Jåsund", "ej@ntnu.no", "55667788"),
(6, "Eirik Jåsund", "eikj@ntnu.no", "66778899"),
(7, "Are Saltnes Tømmerås", "are.sal.tøm@ntnu.no", "10101010"),
(8, "Lars Tangen", "lartanfg@ntnu.no", "45454545"),
(9, "Merete Jåsund", "meretejaas@ntnu.no", "23232323"),
(10, "Sofie Hjelle", "sofhjelle@ntnu.no", "12121212"),
(11, "Johnny John", "johnny@stud.ntnu.no", "00000000");

-- Gruppetimer
INSERT OR IGNORE INTO group_lesson (id, room_id, capacity, time, instructor) VALUES
-- 16 March
(1, 1, 38, '2026-03-16 07:00', 1),
(2, 5, 20, '2026-03-16 16:30', 1),
(3, 1, 38, '2026-03-16 16:30', 2),
(4, 1, 38, '2026-03-16 17:40', 2),
(5, 1, 38, '2026-03-16 19:00', 2),

-- 17 March
(6, 1, 38, '2026-03-17 07:00', 1),
(7, 1, 38, '2026-03-17 18:30', 2),
(8, 1, 38, '2026-03-17 19:45', 3),

-- 18 March
(9, 1, 38, '2026-03-18 16:15', 3),
(10, 5, 20, '2026-03-18 16:30', 3),
(11, 1, 38, '2026-03-18 17:30', 1),
(12, 1, 38, '2026-03-18 18:30', 1),
(13, 1, 38, '2026-03-18 19:30', 2);

-- Center facilities
INSERT OR IGNORE INTO facility (center_id, type) VALUES
(1, 'Gruppetrening'),
(1, 'Egentrening'),
(1, 'Utholdenhet'),
(1, 'Styrke'),
(1, 'Yoga'),
(1, 'Klatring'),
(1, 'Spinning'),
(1, 'Hall'),
(1, 'Garderober'),
(1, 'Badstue'),
(1, 'Dusj'),
(1, 'Ubemannet treningssenter'),
(1, 'Tilgjengelighet'),
(2, 'Egentrening'),
(2, 'Ubemannet treningssenter'),
(2, 'Styrketrening'),
(2, 'Utholdenhet'),
(2, 'Tilgjengelighet'),
(3, 'Egentrening'),
(3, 'Gruppetrening'),
(3, 'Styrketrening'),
(3, 'Utholdenhet'),
(3, 'Hall'),
(3, 'Yoga'),
(3, 'Dusj'),
(3, 'Garderober'),
(3, 'Badstue'),
(3, 'Bemannet treningssenter'),
(3, 'Tilgjengelighet'),
(4, 'Egentrening'),
(4, 'Spinning'),
(4, 'Squash'),
(4, 'Hall'),
(4, 'Yoga'),
(4, 'Dusj'),
(4, 'Garderober'),
(4, 'Badstue'),
(4, 'Bemannet treningssenter'),
(4, 'Tilgjengelighet');

-- Group lesson types
INSERT OR IGNORE INTO lesson_types (lesson_id, activity_type_id) VALUES
(1, 4),
(2, 2),
(3, 3),
(4, 1),
(5, 1),
(6, 3),
(7, 1),
(8, 2),
(9, 1),
(10, 4),
(11, 2),
(12, 3),
(13, 3);

--Usecase 2
INSERT OR IGNORE INTO activity_type (id, name, description) VALUES 
(1, "Spin60", "En variert spinningtime som er noe mer utfordrende enn Spin45 med lengre varighet og tidvis høyere tempo. Du styrer likevel intensiteten selv, og timen passer alle som liker å tråkke i takt! Timen inneholder 2-4 arbeidsperioder med variert løype."),
(2, "Spin45", "En variert spinningtime med 2-3 arbeidsperioder som passer for alle. Perfekt for deg som er ny på spinning! Du styrer intensiteten selv, og vi bruker takta til å tråkke oss gjennom timen."),
(3, "Spin8x3", "En forutsigbar intervalltime med 8 intervaller på 3 minutter hver, der du sitter og står annethvert drag. 90-120 sek pause mellom hvert intervall. God oppvarming og nedsykling inkludert."),
(4, "Spin4x4", "En forutsigbar intervalltime: 4 stående intervaller på 4 minutter hver, med ca 2 minutter aktiv pause mellom hvert drag. God oppvarming og nedsykling inkludert.");

-- Use case 5
INSERT OR IGNORE INTO group_lesson_participates (member_id, group_lesson_id, date) VALUES
('11', '1', '2026-03-16 06:55:00'),
('11', '6', '2026-03-17 06:55:00'),
('11', '9', '2026-03-18 16:10:00');

-- Use case 8
INSERT OR IGNORE INTO visit VALUES
(11, 1, '2026-02-01 10:00:00'),
(2,  1, '2026-02-01 10:00:40'),

(11, 1, '2026-02-10 11:15:00'),
(2,  1, '2026-02-10 11:15:50'),

(11, 1, '2026-03-05 09:30:10'),
(2,  1, '2026-03-05 09:30:50');