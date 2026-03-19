INSERT OR IGNORE INTO penalties (member_id, date) VALUES
((SELECT id FROM member WHERE member.mail = 'johnny@stud.ntnu.no'), datetime('2026-02-27 16:30')),
((SELECT id FROM member WHERE member.mail = 'johnny@stud.ntnu.no'), datetime('2026-03-07 16:30')),
((SELECT id FROM member WHERE member.mail = 'johnny@stud.ntnu.no'), datetime('2026-03-15 16:30'));

WITH
target_member AS (
    SELECT id
    FROM member
    WHERE mail = 'johnny@stud.ntnu.no'
),

recent_penalties AS (
    SELECT COUNT(*) AS count
    FROM penalties
    WHERE penalties.member_id = (SELECT id FROM target_member)
        AND date >= datetime('now', '-30 days')
)

SELECT
    (SELECT id FROM target_member) AS member_id,
    recent_penalties.count AS penalties_last_30_days,
    CASE
        WHEN recent_penalties.count >= 3 THEN 'Blacklisted'
        ELSE 'Not Blacklisted'
    END AS booking_status
FROM recent_penalties;
