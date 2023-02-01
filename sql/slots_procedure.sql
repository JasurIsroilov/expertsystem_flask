SPOOL slots_procedure.lst


PROMPT Creating procedure for slots

CREATE OR REPLACE PACKAGE prod_slots IS

PROCEDURE slots_add(
p_slot_name IN slots.slt_name%TYPE,
p_slot_describe IN slots.slt_describe%TYPE) ;

PROCEDURE slots_update(
p_slot_id IN slots.slt_id%TYPE,
p_slot_name IN slots.slt_name%TYPE,
p_slot_describe IN slots.slt_describe%TYPE) ;

PROCEDURE slots_delete(
p_slot_id IN slots.slt_id%TYPE) ;

END prod_slots;
/


CREATE OR REPLACE PACKAGE BODY prod_slots
AS

PROCEDURE slots_add(
p_slot_name IN slots.slt_name%TYPE,
p_slot_describe IN slots.slt_describe%TYPE) 
IS
BEGIN
INSERT INTO slots(slt_name, slt_describe)
       VALUES (p_slot_name, p_slot_describe);	
	COMMIT;
END slots_add;


PROCEDURE slots_update(
p_slot_id IN slots.slt_id%TYPE,
p_slot_name IN slots.slt_name%TYPE,
p_slot_describe IN slots.slt_describe%TYPE) 
IS
BEGIN
UPDATE slots 
	SET slt_name=p_slot_name,
    	    slt_describe=p_slot_describe
WHERE slt_id=p_slot_id;  	
	COMMIT;
END slots_update;


PROCEDURE slots_delete(
p_slot_id IN slots.slt_id%TYPE) 
IS
BEGIN
DELETE FROM slots
WHERE slt_id=p_slot_id;  	
	COMMIT;
END slots_delete;

END prod_slots;
/


SPOOL off
COMMIT;
