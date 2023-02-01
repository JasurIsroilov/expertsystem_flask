SPOOL sfr_procedure.lst

PROMPT Creating procedure for slots_frames

CREATE OR REPLACE PACKAGE prod_slots_frames IS

PROCEDURE slots_frames_update(
p_sfr_frm_id IN slots_frames.sfr_frm_id%TYPE,
p_sfr_slt_id IN slots_frames.sfr_slt_id%TYPE,
p_sfr_slv_id IN slots_frames.sfr_slv_id%TYPE) ;

PROCEDURE slots_frames_delete(
p_sfr_frm_id IN slots_frames.sfr_frm_id%TYPE) ;

END prod_slots_frames;
/

CREATE OR REPLACE PACKAGE BODY prod_slots_frames
AS


PROCEDURE slots_frames_update(
p_sfr_frm_id IN slots_frames.sfr_frm_id%TYPE,
p_sfr_slt_id IN slots_frames.sfr_slt_id%TYPE,
p_sfr_slv_id IN slots_frames.sfr_slv_id%TYPE) 
IS
BEGIN

INSERT INTO slots_frames(sfr_frm_id,sfr_slt_id,sfr_slv_id)
VALUES (p_sfr_frm_id,p_sfr_slt_id,p_sfr_slv_id); 
	COMMIT;
END slots_frames_update;


PROCEDURE slots_frames_delete(
p_sfr_frm_id IN slots_frames.sfr_frm_id%TYPE) 
IS
BEGIN
DELETE FROM slots_frames WHERE sfr_frm_id=p_sfr_frm_id;   	
	COMMIT;
END slots_frames_delete;



END prod_slots_frames;
/

SPOOL off;
commit;