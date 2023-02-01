SPOOL slv.lst


PROMPT Creating table slot_value

DROP TABLE slot_value CASCADE CONSTRAINTS;
CREATE TABLE slot_value (
		slv_id         INTEGER NOT NULL,
		slv_val        VARCHAR2(300) NOT NULL
)
TABLESPACE USERS;


PROMPT Creating index

DROP INDEX i_slv_id;
CREATE UNIQUE INDEX i_slv_id ON slot_value(slv_id)
TABLESPACE USERS;


PROMPT Creating pk

ALTER TABLE slot_value 
DROP CONSTRAINT i_slv_pk;
ALTER TABLE slot_value 
ADD (CONSTRAINT i_slv_pk PRIMARY KEY (slv_id));


PROMPT Creating sequence

DROP SEQUENCE s_slot_value ;
CREATE SEQUENCE s_slot_value ;


PROMPT Creating trigger on insert

CREATE OR REPLACE TRIGGER t_ins_slot_value 
BEFORE INSERT ON slot_value FOR EACH ROW
BEGIN
  SELECT s_slot_value.NEXTVAL
  INTO :new.slv_id
  FROM dual;
END;
/


PROMPT Creating trigger on update

CREATE OR REPLACE TRIGGER t_upd_slot_value 
BEFORE UPDATE ON slot_value FOR EACH ROW
BEGIN
  if (:new.slv_id != :old.slv_id) THEN
    :new.slv_id := :old.slv_id;
  END IF;
END;
/


PROMPT Inserting some data

INSERT INTO slot_value(slv_val)
VALUES('v lente dlya avtomata');

INSERT INTO slot_value(slv_val)
VALUES('avtomaticheski');

INSERT INTO slot_value(slv_val)
VALUES('obrabotka volnoy pripoya');

INSERT INTO slot_value(slv_val)
VALUES('testerom');

INSERT INTO slot_value(slv_val)
VALUES('ostsillografom');

PROMPT creating synonym

DROP PUBLIC SYNONYM slot_value;
CREATE PUBLIC SYNONYM slot_value FOR slot_value;


SPOOL off
COMMIT;
