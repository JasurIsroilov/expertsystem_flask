SPOOL frames_procedure.lst

PROMPT Creating procedure for frames

CREATE OR REPLACE PACKAGE prod_frames IS

PROCEDURE frames_add(
p_frame_name IN frames.frm_name%TYPE,
p_frame_examplyar IN frames.frm_examplyar%TYPE,
p_frame_parent_id IN frames.frm_parent_id%TYPE);

PROCEDURE frames_update(
p_frame_id IN frames.frm_id%TYPE,
p_frame_name IN frames.frm_name%TYPE,
p_frame_examplyar IN frames.frm_examplyar%TYPE,
p_frame_parent_id IN frames.frm_parent_id%TYPE);

PROCEDURE frames_delete(
p_frame_id IN frames.frm_id%TYPE) ;

END prod_frames;
/


CREATE OR REPLACE PACKAGE BODY prod_frames
AS

PROCEDURE frames_add(
p_frame_name IN frames.frm_name%TYPE,
p_frame_examplyar IN frames.frm_examplyar%TYPE,
p_frame_parent_id IN frames.frm_parent_id%TYPE) 
IS
BEGIN
INSERT INTO frames(frm_name, frm_examplyar, frm_parent_id)
       VALUES (p_frame_name, p_frame_examplyar, p_frame_parent_id);	
	COMMIT;
END frames_add;


PROCEDURE frames_update(
p_frame_id IN frames.frm_id%TYPE,
p_frame_name IN frames.frm_name%TYPE,
p_frame_examplyar IN frames.frm_examplyar%TYPE,
p_frame_parent_id IN frames.frm_parent_id%TYPE) 
IS
BEGIN
UPDATE frames 
	SET frm_name=p_frame_name,
    	    frm_examplyar=p_frame_examplyar,
	    frm_parent_id=p_frame_parent_id
WHERE frm_id=p_frame_id;  	
	COMMIT;
END frames_update;


PROCEDURE frames_delete(
p_frame_id IN frames.frm_id%TYPE) 
IS
BEGIN
DELETE FROM frames WHERE frm_id=p_frame_id;
DELETE FROM frames WHERE frm_parent_id=p_frame_id;   	
	COMMIT;
END frames_delete;

END prod_frames;
/

SPOOL off;
commit;
