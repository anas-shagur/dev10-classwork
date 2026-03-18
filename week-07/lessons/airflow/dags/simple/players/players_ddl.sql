DROP DATABASE IF EXISTS players_db;
CREATE DATABASE players_db;
USE players_db;

CREATE TABLE player (
    player_id INT PRIMARY KEY AUTO_INCREMENT,
    player_name VARCHAR(100) NOT NULL,
    club VARCHAR(100) NOT NULL,
    nationality VARCHAR(100) NOT NULL,
    height_cm INT NOT NULL,
    avg_goals_per_game DECIMAL(4,2) NOT NULL
);