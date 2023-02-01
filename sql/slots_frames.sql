SPOOL sfr.lst


PROMPT Creating table slots_frames

DROP TABLE slots_frames CASCADE CONSTRAINTS;
CREATE TABLE slots_frames (
		sfr_id         INTEGER NOT NULL,
		sfr_slt_id     INTEGER NOT NULL,
		sfr_slv_id     INTEGER NOT NULL,
		sfr_frm_id     INTEGER NOT NULL
)
TABLESPACE USERS;


PROMPT Creating index

DROP INDEX i_sfr_id;
CREATE UNIQUE INDEX i_sfr_id ON slots_frames(sfr_id)
TABLESPACE USERS;


PROMPT Creating pk

ALTER TABLE slots_frames 
DROP CONSTRAINT i_sfr_pk;
ALTER TABLE slots_frames 
ADD (CONSTRAINT i_sfr_pk PRIMARY KEY (sfr_id));


PROMPT Creating sequence

DROP SEQUENCE s_slots_frames ;
CREATE SEQUENCE s_slots_frames ;


PROMPT Creating trigger on insert

CREATE OR REPLACE TRIGGER t_ins_slots_frames 
BEFORE INSERT ON slots_frames  FOR EACH ROW
BEGIN
  SELECT s_slots_frames.NEXTVAL
  INTO :new.sfr_id
  FROM dual;
END;
/


PROMPT Creating trigger on update

CREATE OR REPLACE TRIGGER t_upd_slots_frames 
BEFORE UPDATE ON slots_frames  FOR EACH ROW
BEGIN
  if (:new.sfr_id != :old.sfr_id) THEN
    :new.sfr_id := :old.sfr_id;
  END IF;
END;
/


PROMPT Creating fk

ALTER TABLE slots_frames
DROP CONSTRAINT c_sfr_slt_id CASCADE;
ALTER TABLE slots_frames
ADD (CONSTRAINT c_sfr_slt_id FOREIGN KEY(sfr_slt_id) 
REFERENCES slots(slt_id));

ALTER TABLE slots_frames
DROP CONSTRAINT c_sfr_slv_id CASCADE;
ALTER TABLE slots_frames
ADD (CONSTRAINT c_sfr_slv_id FOREIGN KEY(sfr_slv_id) 
REFERENCES slot_value(slv_id));

ALTER TABLE slots_frames
DROP CONSTRAINT c_sfr_frm_id CASCADE;
ALTER TABLE slots_frames
ADD (CONSTRAINT c_sfr_frm_id FOREIGN KEY(sfr_frm_id) 
REFERENCES frames(frm_id));


PROMPT Creating synonym

DROP PUBLIC SYNONYM slots_frames;
CREATE PUBLIC SYNONYM slots_frames FOR slots_frames;


SPOOL off
COMMIT;
