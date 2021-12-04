CREATE TABLE IF NOT EXISTS dota_2.game_session_character_insert_with_loop
(
    game_session_id INT NOT NULL REFERENCES game_sessions (id),
    character_id    INT NOT NULL REFERENCES characters (id),
    PRIMARY KEY (game_session_id, character_id)
);

CREATE OR REPLACE FUNCTION random_between(low INT ,high INT)
   RETURNS INT AS
$$
BEGIN
   RETURN floor(random()* (high-low + 1) + low);
END;
$$ language 'plpgsql' STRICT;

DO
$do$
BEGIN
   FOR i IN 1..15 LOOP
      INSERT INTO game_session_character_insert_with_loop
         (game_session_id, character_id)
      SELECT random_between(1, 5), random_between(1, 6)
      ON CONFLICT DO NOTHING;
   END LOOP;
END
$do$;

