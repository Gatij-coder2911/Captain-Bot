-- ----------------------------------------------------------------------------
-- MySQL Workbench Migration
-- Migrated Schemata: captain
-- Source Schemata: captain
-- Created: Mon Apr  1 21:00:56 2024
-- Workbench Version: 8.0.34
-- ----------------------------------------------------------------------------

SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------------------------------------------------------
-- Schema captain
-- ----------------------------------------------------------------------------
DROP SCHEMA IF EXISTS `captain` ;
CREATE SCHEMA IF NOT EXISTS `captain` ;

-- ----------------------------------------------------------------------------
-- Table captain.data
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `captain`.`data` (
  `log_id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(255) NULL DEFAULT NULL,
  `userquery` TEXT NULL DEFAULT NULL,
  `query_datetime` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`log_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- ----------------------------------------------------------------------------
-- Table captain.users
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `captain`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;
SET FOREIGN_KEY_CHECKS = 1;
