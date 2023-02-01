SPOOL trigger_on_delete.lst


PROMPT Creating triggers on deleting data

PROMPT Creating triiger on delete frame

CREATE OR REPLACE TRIGGER t_del_frames
BEFORE DELETE ON frames FOR EACH ROW
BEGIN
  DELETE FROM slots_frames
  WHERE sfr_frm_id = :old.frm_id;
END;
/


PROMPT Creating trigger on delete slot

CREATE OR REPLACE TRIGGER t_del_slots
BEFORE DELETE ON slots FOR EACH ROW
BEGIN
  DELETE FROM slots_frames
  WHERE sfr_slt_id = :old.slt_id;
END;
/


PROMPT Creating trigger on delete slot_value

CREATE OR REPLACE TRIGGER t_del_slot_value
BEFORE DELETE ON slot_value FOR EACH ROW
BEGIN
  DELETE FROM slots_frames
  WHERE sfr_slv_id = :old.slv_id;
END;
/


SPOOL off
COMMIT;
