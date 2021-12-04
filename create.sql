CREATE TABLE game_sessions
(
    id INT PRIMARY KEY
);

CREATE TABLE attributes
(
    id   INT PRIMARY KEY,
    name VARCHAR(32) NOT NULL
);

CREATE TABLE roles
(
    id   INT PRIMARY KEY,
    name VARCHAR(32) NOT NULL
);

CREATE TABLE characters
(
    id             INT PRIMARY KEY,
    name           VARCHAR(32) NOT NULL,
    intelligence   INT         NOT NULL,
    strength       INT         NOT NULL,
    agility        INT         NOT NULL,
    main_attribute INT         NOT NULL REFERENCES attributes (id)
);

CREATE TABLE game_session_character
(
    game_session_id INT NOT NULL REFERENCES game_sessions (id),
    character_id    INT NOT NULL REFERENCES characters (id),
    PRIMARY KEY (game_session_id, character_id)
);

CREATE TABLE character_role
(
    character_id INT NOT NULL REFERENCES characters (id),
    role_id      INT NOT NULL REFERENCES roles (id),
    PRIMARY KEY (character_id, role_id)
);