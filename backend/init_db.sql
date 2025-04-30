-- /backend/init_db.sql

\c my_portfolio_db;

CREATE TABLE projects (
  id SERIAL PRIMARY KEY,
  uuid VARCHAR(36) NOT NULL UNIQUE,
  title VARCHAR(255) NOT NULL,
  fr_preview_desciption VARCHAR(255),
  en_preview_desciption VARCHAR(255),
  fr_description TEXT,
  en_description TEXT,
  url VARCHAR(255)
);

CREATE TABLE tags (
  uuid VARCHAR(36) PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  icon_name VARCHAR(100) NOT NULL,
  background_color VARCHAR(20) NOT NULL
);

CREATE TABLE projects_tags (
  project_id INTEGER NOT NULL
    REFERENCES projects(id)
    ON DELETE CASCADE,
  tag_id   VARCHAR(36) NOT NULL
    REFERENCES tags(uuid)
    ON DELETE CASCADE,
  PRIMARY KEY(project_id, tag_id)
);
