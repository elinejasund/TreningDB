-- Johnny og Gina work out together 3 times
-- Commented out as it is already inserted in the database
INSERT INTO visit VALUES
(11, 1, '2026-02-01 10:00:00'),
(2,  1, '2026-02-01 10:00:40'),

(11, 1, '2026-02-10 11:15:00'),
(2,  1, '2026-02-10 11:15:50'),

(11, 1, '2026-03-05 09:30:10'),
(2,  1, '2026-03-05 09:30:50');

-- Select to check training in pairs the last 3 months
SELECT 
    m1.mail AS student1,
    m2.mail AS student2,
    COUNT(*) AS shared_visits
FROM visit v1
JOIN visit v2
    ON v1.center_id = v2.center_id
    AND v1.member_id < v2.member_id
    AND ABS(strftime('%s', v1.date) - strftime('%s', v2.date)) <= 60
JOIN member m1 ON v1.member_id = m1.id
JOIN member m2 ON v2.member_id = m2.id
WHERE v1.date >= '2026-01-01'
  AND v1.date <= '2026-03-31'
GROUP BY m1.mail, m2.mail
HAVING COUNT(*) >= 3;