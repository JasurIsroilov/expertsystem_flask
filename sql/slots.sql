SPOOL slots.lst


PROMPT Creating table slots

DROP TABLE slots CASCADE CONSTRAINTS;
CREATE TABLE slots (
		slt_id         INTEGER,
		slt_name       VARCHAR2(50) NOT NULL,
		slt_describe   VARCHAR2(300)
)
TABLESPACE USERS;


PROMPT Creating index

DROP INDEX i_slt_id;
CREATE UNIQUE INDEX i_slt_id ON slots(slt_id)
TABLESPACE USERS;


PROMPT Creating pk

ALTER TABLE slots
DROP CONSTRAINT i_slt_pk;
ALTER TABLE slots
ADD (CONSTRAINT i_slt_pk PRIMARY KEY (slt_id));


PROMPT Creating sequence

DROP SEQUENCE s_slots;
CREATE SEQUENCE s_slots;


PROMPT Creating trigger on insert

CREATE OR REPLACE TRIGGER t_ins_slots
BEFORE INSERT ON slots FOR EACH ROW
BEGIN
  SELECT s_slots.NEXTVAL
  INTO :new.slt_id
  FROM dual;
END;
/


PROMPT Creating trigger on UPDATE

CREATE OR REPLACE TRIGGER t_upd_slots
BEFORE UPDATE ON slots FOR EACH ROW
BEGIN
  if (:new.slt_id != :old.slt_id) THEN
    :new.slt_id := :old.slt_id;
  END IF;
END;
/


PROMPT inserting some data

INSERT INTO slots( slt_name, slt_describe)
VALUES('Vid sborki', 'Osobennosti sborki izdeliya');

INSERT INTO slots( slt_name, slt_describe)
VALUES('Xarakter upakovki komponentov', 'Osobennosti upakovki komponentov');

INSERT INTO slots( slt_name, slt_describe)
VALUES('Tip raspredeleniya komponentov', 'Osobennosi raspredeleniya komponentov');

INSERT INTO slots( slt_name, slt_describe)
VALUES('Kontrol', 'Osobennosti kontrolya');

INSERT INTO slots( slt_name, slt_describe)
VALUES('Vid formovki', 'Osobennosti formovki');

INSERT INTO slots( slt_name, slt_describe)
VALUES('Ispolzuemie komplektuyushie', 'Vidi ispolzuemix komplektuyushix');

INSERT INTO slots( slt_name, slt_describe)
VALUES('Xarakter proizvodstva', 'Tip proizvodstva');


PROMPT Creating SYNONYM

DROP PUBLIC SYNONYM slots;
CREATE PUBLIC SYNONYM slots FOR slots;


SPOOL OFF
COMMIT;
