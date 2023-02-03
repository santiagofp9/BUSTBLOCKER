CREATE DATABASE IF NOT EXISTS `bustblocker` DEFAULT CHARACTER SET utf8 ;
USE `bustblocker` ;

-- -----------------------------------------------------
-- Table `bustblocker`.`category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bustblocker`.`category` (
  `category_id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`category_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bustblocker`.`actor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bustblocker`.`actor` (
  `actor_id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`actor_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bustblocker`.`film`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bustblocker`.`film` (
  `film_id` INT NOT NULL,
  `title` VARCHAR(45) NULL,
  `description` VARCHAR(500) NULL,
  `release_year_x` INT NULL,
  `rental_duration` INT NULL,
  `rental_rate` FLOAT NULL,
  `length` INT NULL,
  `replacement_cost` FLOAT NULL,
  `rating` VARCHAR(10) NULL,
  `special_features` VARCHAR(55) NULL,
  `category_id` INT NULL,
  PRIMARY KEY (`film_id`),
  INDEX `fks_category_idx` (`category_id` ASC),
  CONSTRAINT `fks_category`
    FOREIGN KEY (`category_id`)
    REFERENCES `bustblocker`.`category` (`category_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bustblocker`.`title_actor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bustblocker`.`title_actor` (
  `film_id` INT NULL,
  `actor_id` INT NULL,
  INDEX `fks_film_idx` (`film_id` ASC),
  INDEX `fks_actor_idx` (`actor_id` ASC),
  CONSTRAINT `fks_film`
    FOREIGN KEY (`film_id`)
    REFERENCES `bustblocker`.`film` (`film_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fks_actor`
    FOREIGN KEY (`actor_id`)
    REFERENCES `bustblocker`.`actor` (`actor_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bustblocker`.`inventory`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bustblocker`.`inventory` (
  `inventory_id` INT NOT NULL,
  `film_id` INT NULL,
  `store_id` INT NULL,
  PRIMARY KEY (`inventory_id`),
  INDEX `fks_film_id_idx` (`film_id` ASC),
  CONSTRAINT `fks_film_id`
    FOREIGN KEY (`film_id`)
    REFERENCES `bustblocker`.`film` (`film_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bustblocker`.`rental`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bustblocker`.`rental` (
  `rental_id` INT NOT NULL,
  `rental_date` VARCHAR(45) NULL,
  `inventory_id` INT NULL,
  `customer_id` INT NULL,
  `return_date` VARCHAR(45) NULL,
  `staff_id` INT NULL,
  PRIMARY KEY (`rental_id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

