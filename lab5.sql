SET NAMES utf8mb4;
USE it_inventory;

DROP TRIGGER IF EXISTS trg_repair_before_insert;
DROP TRIGGER IF EXISTS trg_repair_before_update;
DROP TRIGGER IF EXISTS trg_equipment_before_delete;
DROP TRIGGER IF EXISTS trg_employee_workplace_before_delete;
DROP TRIGGER IF EXISTS trg_assignment_after_delete;
DROP TRIGGER IF EXISTS trg_assignment_after_update;
DROP PROCEDURE IF EXISTS insert_manufacturer;
DROP PROCEDURE IF EXISTS add_employee_workplace;
DROP PROCEDURE IF EXISTS insert_noname_types;
DROP PROCEDURE IF EXISTS show_avg_ram;
DROP PROCEDURE IF EXISTS split_office;
DROP FUNCTION IF EXISTS get_avg_ram;
DROP TABLE IF EXISTS repair;
DROP TABLE IF EXISTS assignment_log;

CREATE TABLE repair (
  id           INT AUTO_INCREMENT PRIMARY KEY,
  description  VARCHAR(200) NOT NULL,
  equipment_id INT NOT NULL
);

DELIMITER //

CREATE TRIGGER trg_repair_before_insert
BEFORE INSERT ON repair
FOR EACH ROW
BEGIN
  IF NOT EXISTS (SELECT 1 FROM equipment WHERE id = NEW.equipment_id) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Такого обладнання немає';
  END IF;
END//

CREATE TRIGGER trg_repair_before_update
BEFORE UPDATE ON repair
FOR EACH ROW
BEGIN
  IF NOT EXISTS (SELECT 1 FROM equipment WHERE id = NEW.equipment_id) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Такого обладнання немає';
  END IF;
END//

CREATE TRIGGER trg_equipment_before_delete
BEFORE DELETE ON equipment
FOR EACH ROW
BEGIN
  IF EXISTS (SELECT 1 FROM repair WHERE equipment_id = OLD.id) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'На це обладнання посилається repair';
  END IF;
END//

DELIMITER ;

INSERT INTO repair (description, equipment_id) VALUES
  ('Заміна фотобарабана', 9),
  ('Заміна клавіатури',   1),
  ('Заміна акумулятора',  3);

DELIMITER //

CREATE PROCEDURE insert_manufacturer(IN p_name VARCHAR(60), IN p_country VARCHAR(60))
BEGIN
  INSERT INTO manufacturer (name, country) VALUES (p_name, p_country);
END//

CREATE PROCEDURE add_employee_workplace(
  IN p_last_name VARCHAR(50), IN p_first_name VARCHAR(50), IN p_code VARCHAR(10))
BEGIN
  DECLARE v_employee_id INT;
  DECLARE v_workplace_id INT;

  SELECT id INTO v_employee_id FROM employee
  WHERE last_name = p_last_name AND first_name = p_first_name;

  SELECT id INTO v_workplace_id FROM workplace
  WHERE code = p_code;

  INSERT INTO employee_workplace (employee_id, workplace_id)
  VALUES (v_employee_id, v_workplace_id);
END//

CREATE PROCEDURE insert_noname_types()
BEGIN
  DECLARE v_start INT;
  DECLARE i INT DEFAULT 1;

  SELECT MAX(id) INTO v_start FROM equipment_type;

  WHILE i <= 10 DO
    INSERT INTO equipment_type (name) VALUES (CONCAT('Noname', v_start + i));
    SET i = i + 1;
  END WHILE;
END//

CREATE FUNCTION get_avg_ram()
RETURNS DECIMAL(10, 2)
READS SQL DATA
BEGIN
  RETURN (SELECT AVG(ram_gb) FROM computer_configuration);
END//

CREATE PROCEDURE show_avg_ram()
BEGIN
  SELECT get_avg_ram() AS avg_ram_gb;
END//

CREATE PROCEDURE split_office()
BEGIN
  DECLARE done INT DEFAULT FALSE;
  DECLARE v_id INT;
  DECLARE v_table_1 VARCHAR(64);
  DECLARE v_table_2 VARCHAR(64);
  DECLARE office_cursor CURSOR FOR SELECT id FROM office;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

  SET v_table_1 = CONCAT('office_', DATE_FORMAT(NOW(), '%Y%m%d_%H%i%s'), '_1');
  SET v_table_2 = CONCAT('office_', DATE_FORMAT(NOW(), '%Y%m%d_%H%i%s'), '_2');

  SET @sql = CONCAT('CREATE TABLE ', v_table_1, ' LIKE office');
  PREPARE stmt FROM @sql;
  EXECUTE stmt;

  SET @sql = CONCAT('CREATE TABLE ', v_table_2, ' LIKE office');
  PREPARE stmt FROM @sql;
  EXECUTE stmt;

  OPEN office_cursor;
  read_loop: LOOP
    FETCH office_cursor INTO v_id;
    IF done THEN
      LEAVE read_loop;
    END IF;

    IF RAND() < 0.5 THEN
      SET @sql = CONCAT('INSERT INTO ', v_table_1, ' SELECT * FROM office WHERE id = ', v_id);
    ELSE
      SET @sql = CONCAT('INSERT INTO ', v_table_2, ' SELECT * FROM office WHERE id = ', v_id);
    END IF;
    PREPARE stmt FROM @sql;
    EXECUTE stmt;
  END LOOP;
  CLOSE office_cursor;
END//

DELIMITER ;

CREATE TABLE assignment_log (
  id            INT AUTO_INCREMENT PRIMARY KEY,
  action        VARCHAR(10) NOT NULL,
  assignment_id INT NOT NULL,
  logged_at     DATETIME NOT NULL
);

DELIMITER //

CREATE TRIGGER trg_employee_workplace_before_delete
BEFORE DELETE ON employee_workplace
FOR EACH ROW
BEGIN
  IF (SELECT COUNT(*) FROM employee_workplace) <= 6 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Має залишатися щонайменше 6 рядків';
  END IF;
END//

CREATE TRIGGER trg_assignment_after_delete
AFTER DELETE ON equipment_assignment
FOR EACH ROW
BEGIN
  INSERT INTO assignment_log (action, assignment_id, logged_at)
  VALUES ('DELETE', OLD.id, NOW());
END//

CREATE TRIGGER trg_assignment_after_update
AFTER UPDATE ON equipment_assignment
FOR EACH ROW
BEGIN
  INSERT INTO assignment_log (action, assignment_id, logged_at)
  VALUES ('UPDATE', OLD.id, NOW());
END//

DELIMITER ;
