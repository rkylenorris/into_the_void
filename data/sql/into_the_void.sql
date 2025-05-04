CREATE SCHEMA "world";

CREATE SCHEMA "psyche";

CREATE SCHEMA "player";

CREATE SCHEMA "narrative";

CREATE SCHEMA "key_narrative";

CREATE TABLE "world"."map" (
  "id" serial PRIMARY KEY,
  "name" text,
  "description" text
);

CREATE TABLE "world"."room" (
  "id" serial PRIMARY KEY,
  "map_id" int,
  "name" text,
  "theme_id" int,
  "room_type_id" int,
  "ambiance_id" int
);

CREATE TABLE "world"."connection" (
  "id" serial PRIMARY KEY,
  "from_room_id" int,
  "to_room_id" int,
  "bidirectional" boolean
);

CREATE TABLE "world"."theme" (
  "id" serial PRIMARY KEY,
  "name" text,
  "description" text
);

CREATE TABLE "world"."adjective" (
  "id" serial PRIMARY KEY,
  "word" text
);

CREATE TABLE "world"."ambiance" (
  "id" serial PRIMARY KEY,
  "description" text
);

CREATE TABLE "world"."room_type" (
  "id" serial PRIMARY KEY,
  "name" text
);

CREATE TABLE "psyche"."aspect" (
  "id" serial PRIMARY KEY,
  "name" text,
  "description" text
);

CREATE TABLE "psyche"."conflict" (
  "id" serial PRIMARY KEY,
  "aspect_id" int,
  "opposes_id" int,
  "name" text,
  "description" text,
  "strength" float
);

CREATE TABLE "psyche"."resolution" (
  "id" serial PRIMARY KEY,
  "conflict_id" int,
  "description" text
);

CREATE TABLE "psyche"."threshold" (
  "id" serial PRIMARY KEY,
  "aspect_id" int,
  "level" int,
  "name" text,
  "description" text
);

CREATE TABLE "psyche"."milestone" (
  "id" serial PRIMARY KEY,
  "name" text,
  "description" text
);

CREATE TABLE "player"."player" (
  "id" serial PRIMARY KEY,
  "name" text,
  "created_at" timestamp
);

CREATE TABLE "player"."character" (
  "id" serial PRIMARY KEY,
  "player_id" int,
  "current_room_id" int
);

CREATE TABLE "player"."inventory" (
  "id" serial PRIMARY KEY,
  "character_id" int,
  "item_id" int
);

CREATE TABLE "player"."toolkit" (
  "id" serial PRIMARY KEY,
  "character_id" int,
  "name" text,
  "effect" text
);

CREATE TABLE "player"."state" (
  "id" serial PRIMARY KEY,
  "character_id" int,
  "key" text,
  "value" text
);

CREATE TABLE "player"."aspect_presence_log" (
  "id" serial PRIMARY KEY,
  "character_id" int,
  "aspect_id" int,
  "presence" int,
  "timestamp" timestamp
);

CREATE TABLE "player"."ritual_log" (
  "id" serial PRIMARY KEY,
  "character_id" int,
  "ritual_id" int,
  "performed_at" timestamp
);

CREATE TABLE "player"."meditation_log" (
  "id" serial PRIMARY KEY,
  "character_id" int,
  "entry" text,
  "timestamp" timestamp
);

CREATE TABLE "player"."grounding_exercises_log" (
  "id" serial PRIMARY KEY,
  "character_id" int,
  "technique" text,
  "notes" text,
  "timestamp" timestamp
);

CREATE TABLE "player"."void_journal_entry" (
  "id" serial PRIMARY KEY,
  "character_id" int,
  "content" text,
  "created_at" timestamp
);

CREATE TABLE "player"."tarot_card" (
  "id" serial PRIMARY KEY,
  "name" text,
  "meaning" text
);

CREATE TABLE "player"."tarot_reading" (
  "id" serial PRIMARY KEY,
  "character_id" int,
  "card_id" int,
  "interpretation" text,
  "created_at" timestamp
);

CREATE TABLE "narrative"."npc" (
  "id" serial PRIMARY KEY,
  "name" text,
  "description" text,
  "location_id" int
);

CREATE TABLE "narrative"."item" (
  "id" serial PRIMARY KEY,
  "name" text,
  "description" text,
  "motif_id" int
);

CREATE TABLE "narrative"."motif" (
  "id" serial PRIMARY KEY,
  "symbol" text,
  "meaning" text
);

CREATE TABLE "narrative"."ritual" (
  "id" serial PRIMARY KEY,
  "name" text,
  "requirement" text,
  "effect" text
);

CREATE TABLE "narrative"."place" (
  "id" serial PRIMARY KEY,
  "name" text,
  "theme_id" int,
  "description" text
);

CREATE TABLE "key_narrative"."npc" (
  "id" serial PRIMARY KEY,
  "npc_id" int,
  "symbolic_role" text
);

ALTER TABLE "world"."room" ADD FOREIGN KEY ("map_id") REFERENCES "world"."map" ("id");

ALTER TABLE "world"."room" ADD FOREIGN KEY ("theme_id") REFERENCES "world"."theme" ("id");

ALTER TABLE "world"."room" ADD FOREIGN KEY ("room_type_id") REFERENCES "world"."room_type" ("id");

ALTER TABLE "world"."room" ADD FOREIGN KEY ("ambiance_id") REFERENCES "world"."ambiance" ("id");

ALTER TABLE "world"."connection" ADD FOREIGN KEY ("from_room_id") REFERENCES "world"."room" ("id");

ALTER TABLE "world"."connection" ADD FOREIGN KEY ("to_room_id") REFERENCES "world"."room" ("id");

ALTER TABLE "psyche"."conflict" ADD FOREIGN KEY ("aspect_id") REFERENCES "psyche"."aspect" ("id");

ALTER TABLE "psyche"."conflict" ADD FOREIGN KEY ("opposes_id") REFERENCES "psyche"."aspect" ("id");

ALTER TABLE "psyche"."resolution" ADD FOREIGN KEY ("conflict_id") REFERENCES "psyche"."conflict" ("id");

ALTER TABLE "psyche"."threshold" ADD FOREIGN KEY ("aspect_id") REFERENCES "psyche"."aspect" ("id");

ALTER TABLE "player"."character" ADD FOREIGN KEY ("player_id") REFERENCES "player"."player" ("id");

ALTER TABLE "player"."character" ADD FOREIGN KEY ("current_room_id") REFERENCES "world"."room" ("id");

ALTER TABLE "player"."inventory" ADD FOREIGN KEY ("character_id") REFERENCES "player"."character" ("id");

ALTER TABLE "player"."inventory" ADD FOREIGN KEY ("item_id") REFERENCES "narrative"."item" ("id");

ALTER TABLE "player"."toolkit" ADD FOREIGN KEY ("character_id") REFERENCES "player"."character" ("id");

ALTER TABLE "player"."state" ADD FOREIGN KEY ("character_id") REFERENCES "player"."character" ("id");

ALTER TABLE "player"."aspect_presence_log" ADD FOREIGN KEY ("character_id") REFERENCES "player"."character" ("id");

ALTER TABLE "player"."aspect_presence_log" ADD FOREIGN KEY ("aspect_id") REFERENCES "psyche"."aspect" ("id");

ALTER TABLE "player"."ritual_log" ADD FOREIGN KEY ("character_id") REFERENCES "player"."character" ("id");

ALTER TABLE "player"."ritual_log" ADD FOREIGN KEY ("ritual_id") REFERENCES "narrative"."ritual" ("id");

ALTER TABLE "player"."meditation_log" ADD FOREIGN KEY ("character_id") REFERENCES "player"."character" ("id");

ALTER TABLE "player"."grounding_exercises_log" ADD FOREIGN KEY ("character_id") REFERENCES "player"."character" ("id");

ALTER TABLE "player"."void_journal_entry" ADD FOREIGN KEY ("character_id") REFERENCES "player"."character" ("id");

ALTER TABLE "player"."tarot_reading" ADD FOREIGN KEY ("character_id") REFERENCES "player"."character" ("id");

ALTER TABLE "player"."tarot_reading" ADD FOREIGN KEY ("card_id") REFERENCES "player"."tarot_card" ("id");

ALTER TABLE "narrative"."npc" ADD FOREIGN KEY ("location_id") REFERENCES "world"."room" ("id");

ALTER TABLE "key_narrative"."npc" ADD FOREIGN KEY ("npc_id") REFERENCES "narrative"."npc" ("id");

ALTER TABLE "narrative"."item" ADD FOREIGN KEY ("motif_id") REFERENCES "narrative"."motif" ("id");

ALTER TABLE "narrative"."place" ADD FOREIGN KEY ("theme_id") REFERENCES "world"."theme" ("id");
