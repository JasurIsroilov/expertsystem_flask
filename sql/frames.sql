SPOOL frames.lst


PROMPT Creating table frames

DROP TABLE frames CASCADE CONSTRAINTS;
CREATE TABLE frames (
		frm_id         INTEGER NOT NULL,
		frm_parent_id  INTEGER,
		frm_name       VARCHAR2(50) NOT NULL,
		frm_examplyar  INTEGER NOT NULL
)
TABLESPACE USERS;


PROMPT Creating index

DROP INDEX i_frm_id;
CREATE UNIQUE INDEX i_frm_id ON frames(frm_id)
TABLESPACE USERS;


PROMPT Creating pk

ALTER TABLE frames
DROP CONSTRAINT i_frm_pk;
ALTER TABLE frames
ADD (CONSTRAINT i_frm_pk PRIMARY KEY (frm_id));


PROMPT Creating sequence

DROP SEQUENCE s_frames;
CREATE SEQUENCE s_frames;


PROMPT Creating trigger on insert

CREATE OR REPLACE TRIGGER t_ins_frames
BEFORE INSERT ON frames FOR EACH ROW
BEGIN
  SELECT s_frames.NEXTVAL
  INTO :new.frm_id
  FROM dual;
END;
/


PROMPT Creating trigger on update

CREATE OR REPLACE TRIGGER t_upd_frames
BEFORE UPDATE ON frames FOR EACH ROW
BEGIN
  if (:new.frm_id != :old.frm_id) THEN
    :new.frm_id := :old.frm_id;
  END IF;
END;
/

PROMPT Inserting some data

INSERT INTO frames(frm_id, frm_name, frm_examplyar)
VALUES('1', 'Proizvodstvo', '0');

INSERT INTO frames(frm_id, frm_name, frm_examplyar)
VALUES('2', 'Patametri bloka pitaniya', '0');

INSERT INTO frames(frm_id, frm_parent_id, frm_name, frm_examplyar)
VALUES('3','1', 'Seriynoe', '0');

INSERT INTO frames(frm_id, frm_parent_id, frm_name, frm_examplyar)
VALUES('4','1', 'Massovoe', '0');

INSERT INTO frames(frm_id, frm_parent_id, frm_name, frm_examplyar)
VALUES('5','1', 'Edinichnoe', '0');

INSERT INTO frames(frm_id, frm_parent_id, frm_name, frm_examplyar)
VALUES('6','2', 'Nisha rinka', '0');

INSERT INTO frames(frm_id, frm_parent_id, frm_name, frm_examplyar)
VALUES('7','3', 'Avokomplektatsiya i formovka', '1');

INSERT INTO frames(frm_id, frm_parent_id, frm_name, frm_examplyar)
VALUES('8','3', 'Payka volnoy i avtoispitaniya', '1');

INSERT INTO frames(frm_id, frm_parent_id, frm_name, frm_examplyar)
VALUES('9','4', 'Avotamicheski TP', '1');

INSERT INTO frames(frm_id, frm_parent_id, frm_name, frm_examplyar)
VALUES('10','4', 'TP s ruchnim kontrolem', '1');

INSERT INTO frames(frm_id, frm_parent_id, frm_name, frm_examplyar)
VALUES('11','5', 'Ruchnoy TP', '1');

INSERT INTO frames(frm_id, frm_parent_id, frm_name, frm_examplyar)
VALUES('12','5', 'TP s avtokontrolem', '1');


PROMPT Creating synonym

DROP PUBLIC SYNONYM frames;
CREATE PUBLIC SYNONYM frames FOR frames;

spool off
commit;
