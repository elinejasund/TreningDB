-- member 
CREATE TABLE member ( 
  id INTEGER NOT NULL PRIMARY KEY, 
  name TEXT NOT NULL, 
  mail TEXT NOT NULL UNIQUE, 
  phone_number TEXT NOT NULL 
);

-- group lesson participates
CREATE TABLE group_lesson_participates ( 
  member_id INTEGER NOT NULL,
  group_lesson_id INTEGER NOT NULL,
  date DATETIME NOT NULL, -- date i lesson gjelder ikke her siden dette registrerer oppmøte
  FOREIGN KEY (member_id) REFERENCES member(id),
  FOREIGN KEY (group_lesson_id) REFERENCES group_lesson(id),
  PRIMARY KEY (member_id, group_lesson_id, date) 
  );
  
-- penalties 
CREATE TABLE penalties ( 
  member_id INTEGER NOT NULL, 
  date DATETIME NOT NULL, 
  FOREIGN KEY (member_id) REFERENCES member(id),
  PRIMARY KEY (member_id, date) 
); 

-- group lessons 
CREATE TABLE group_lesson ( 
  id INTEGER NOT NULL PRIMARY KEY, 
  room_id INTEGER NOT NULL, 
  capacity INTEGER NOT NULL, -- dersom vi antar at room cap != group cap mtp utstyr 
  time DATETIME NOT NULL,
  instructor INTEGER NOT NULL,
  FOREIGN KEY (room_id) REFERENCES room(id),
  FOREIGN KEY (instructor) REFERENCES member(id)
);

-- activity types 
CREATE TABLE activity_type ( 
  id INTEGER NOT NULL PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT NOT NULL
);

-- lesson_types
CREATE TABLE lesson_types (
  lesson_id INTEGER NOT NULL,
  activity_type_id INTEGER NOT NULL,
  PRIMARY KEY (lesson_id, activity_type_id),
  FOREIGN KEY (lesson_id) REFERENCES group_lesson(id),
  FOREIGN KEY (activity_type_id) REFERENCES activity_type(id)
);

-- center
CREATE TABLE center (
    id INTEGER PRIMARY KEY NOT NULL,
    address TEXT NOT NULL,
    name TEXT NOT NULL,
    has_group_lesson BOOLEAN NOT NULL,
    has_self_training BOOLEAN NOT NULL
);

-- room
CREATE TABLE room (
    id INTEGER PRIMARY KEY NOT NULL,
    center_id INTEGER NOT NULL,
    type TEXT NOT NULL,
    capacity INTEGER NOT NULL,
    FOREIGN KEY (center_id) REFERENCES center(id)
);

-- center_hours
CREATE TABLE opening_hours (
    center_id INTEGER NOT NULL,
    weekday TEXT CHECK(weekday IN ('mandag','tirsdag','onsdag','torsdag','fredag','lørdag','søndag')),
    opening_time TIME NOT NULL,
    closing_time TIME NOT NULL,
    PRIMARY KEY (center_id, weekday, opening_time, closing_time),
    FOREIGN KEY (center_id) REFERENCES center(id)
);

CREATE TABLE staffing_hours (
  center_id INTEGER NOT NULL,
  weekday TEXT CHECK(weekday IN ('mandag','tirsdag','onsdag','torsdag','fredag','lørdag','søndag')),
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  PRIMARY KEY (center_id, weekday, start_time, end_time),
  FOREIGN KEY (center_id) REFERENCES center(id)
);

-- facility
CREATE TABLE facility (
    center_id INTEGER NOT NULL,
    type TEXT NOT NULL,
    PRIMARY KEY (type, center_id),
    FOREIGN KEY (center_id) REFERENCES center(id)
);

-- visit
CREATE TABLE visit (
    member_id INTEGER NOT NULL,
    center_id INTEGER NOT NULL,
    date DATETIME NOT NULL,
    PRIMARY KEY (member_id, center_id, date),
    FOREIGN KEY (center_id) REFERENCES center(id),
    FOREIGN KEY (member_id) REFERENCES member(id)
);

-- sports team
CREATE TABLE sports_team (
  id INTEGER NOT NULL PRIMARY KEY,
  name TEXT NOT NULL
);

-- sports team members
CREATE TABLE sports_team_members (
  team_id INTEGER NOT NULL,
  member_id INTEGER NOT NULL,
  FOREIGN KEY (team_id) REFERENCES sports_team(id),
  FOREIGN KEY (member_id) REFERENCES member(id),
  PRIMARY KEY (team_id, member_id)
);

-- bike
CREATE TABLE bike (
  number INTEGER NOT NULL PRIMARY KEY,
  room INTEGER NOT NULL,
  type TEXT NOT NULL,
  has_bluetooth BOOLEAN NOT NULL,
  FOREIGN KEY (room) REFERENCES room(id)
);

-- treadmill
CREATE TABLE treadmill (
  number INTEGER NOT NULL PRIMARY KEY,
  room INTEGER NOT NULL,
  manufacturer TEXT NOT NULL,
  max_speed INTEGER NOT NULL,
  max_rise INTEGER NOT NULL,
  FOREIGN KEY (room) REFERENCES room(id)
);

-- room booking
CREATE TABLE room_booking (
  id INTEGER NOT NULL PRIMARY KEY,
  room INTEGER NOT NULL,
  time DATETIME NOT NULL,
  team_id INTEGER NOT NULL,
  FOREIGN KEY (room) REFERENCES room(id),
  FOREIGN KEY (team_id) REFERENCES sports_team(id)
);

-- team room booking participates
CREATE TABLE team_room_booking_participates (
  member_id INTEGER NOT NULL,
  room_booking_id INTEGER NOT NULL,
  date DATETIME NOT NULL,
  FOREIGN KEY (member_id) REFERENCES member(id),
  FOREIGN KEY (room_booking_id) REFERENCES room_booking(id),
  PRIMARY KEY (member_id, room_booking_id, date)
);

CREATE TABLE group_lesson_booking (
  member_id INTEGER NOT NULL,
  group_lesson_id INTEGER NOT NULL,
  FOREIGN KEY (member_id) REFERENCES member(id),
  FOREIGN KEY (group_lesson_id) REFERENCES group_lesson(id),
  PRIMARY KEY (member_id, group_lesson_id)
);

-- waitlist
CREATE TABLE waitlist (
  member_id INTEGER NOT NULL,
  position INTEGER NOT NULL,
  group_lesson_id INTEGER NOT NULL,
  FOREIGN KEY (member_id) REFERENCES member(id),
  FOREIGN KEY (group_lesson_id) REFERENCES group_lesson(id),
  PRIMARY KEY (member_id, group_lesson_id)
);