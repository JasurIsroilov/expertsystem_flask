SPOOL users.lst


PROMPT Creating table user_table

DROP TABLE user_table CASCADE CONSTRAINTS;
CREATE TABLE user_table (
		id         INTEGER NOT NULL,
		login      VARCHAR2(50) NOT NULL,
		password   VARCHAR2(50) NOT NULL,
		role       VARCHAR2(50) NOT NULL
)
TABLESPACE USERS;


PROMPT Creating index

DROP INDEX i_user_id;
CREATE UNIQUE INDEX i_user_id ON user_table(id)
TABLESPACE USERS;


PROMPT Creating pk

ALTER TABLE user_table
DROP CONSTRAINT users_pk;
ALTER TABLE user_table
ADD (CONSTRAINT users_pk PRIMARY KEY (id));


PROMPT Creating sequence

DROP SEQUENCE s_users;
CREATE SEQUENCE s_users;


PROMPT Creating trigger on insert

CREATE OR REPLACE TRIGGER t_ins_user
BEFORE INSERT ON user_table FOR EACH ROW
BEGIN
  SELECT s_users.NEXTVAL
  INTO :new.id
  FROM dual;
END;
/


PROMPT Creating trigger on update

CREATE OR REPLACE TRIGGER t_upd_user
BEFORE UPDATE ON user_table FOR EACH ROW
BEGIN
  if (:new.id != :old.id) THEN
    :new.id := :old.id;
  END IF;
END;
/


PROMPT Inserting some data

INSERT INTO user_table(login, password, role)
VALUES ('tech', 'tech', 'tech');
INSERT INTO user_table(login, password, role)
VALUES ('admin', 'admin', 'admin');
INSERT INTO user_table(login, password, role)
VALUES ('expert', 'expert', 'expert');

SPOOL off
COMMIT;
