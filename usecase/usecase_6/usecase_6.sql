INSERT OR IGNORE INTO penalties (member_id, date) VALUES
((SELECT id FROM member WHERE member.mail = 'johnny@stud.ntnu.no'), datetime('now', '-10 days')),
((SELECT id FROM member WHERE member.mail = 'johnny@stud.ntnu.no'), datetime('now', '-5 days')),
((SELECT id FROM member WHERE member.mail = 'johnny@stud.ntnu.no'), datetime('now', '-1 day'));

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
