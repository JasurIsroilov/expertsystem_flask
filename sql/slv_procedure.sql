SPOOL slv_procedure.lst

PROMPT Creating procedure for slot_value

CREATE OR REPLACE PACKAGE prod_slot_value IS

PROCEDURE slot_value_add(
p_slv_val IN slot_value.slv_val%TYPE) ;

PROCEDURE slot_value_update(
p_slv_id IN slot_value.slv_id%TYPE,
p_slv_val IN slot_value.slv_val%TYPE) ;

PROCEDURE slot_value_delete(
p_slv_id IN slot_value.slv_id%TYPE) ;

END prod_slot_value;
/

CREATE OR REPLACE PACKAGE BODY prod_slot_value
AS

PROCEDURE slot_value_add(
p_slv_val IN slot_value.slv_val%TYPE) 
IS
BEGIN
INSERT INTO slot_value(slv_val)
       VALUES (p_slv_val);	
	COMMIT;
END slot_value_add;


PROCEDURE slot_value_update(
p_slv_id IN slot_value.slv_id%TYPE,
p_slv_val IN slot_value.slv_val%TYPE) 
IS
BEGIN
UPDATE slot_value 
	SET slv_val=p_slv_val
WHERE slv_id=p_slv_id;  	
	COMMIT;
END slot_value_update;


PROCEDURE slot_value_delete(
p_slv_id IN slot_value.slv_id%TYPE) 
IS
BEGIN
DELETE FROM slot_value WHERE slv_id=p_slv_id;   	
	COMMIT;
END slot_value_delete;

END prod_slot_value;
/

SPOOL off;
commit;