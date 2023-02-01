SPOOL solution_procedure.lst

PROMPT Creating package pack_solution

CREATE OR REPLACE PACKAGE pack_solution AS

TYPE return_cur IS REF CURSOR;

PROCEDURE proc_solution (
ask_number IN INTEGER, 
p_frm IN OUT return_cur);

PROCEDURE proc_solution_del;

END pack_solution;
/


CREATE OR REPLACE PACKAGE BODY pack_solution
AS

PROCEDURE proc_solution(ask_number IN INTEGER, p_frm IN OUT return_cur) 
IS
BEGIN
OPEN p_frm FOR

SELECT frm_name from frames, slots_frames
		where sfr_slv_id = (SELECT ask_val from asks
						where ask_num=ask_number) 
		AND frm_id=sfr_frm_id;

COMMIT;
END proc_solution;


PROCEDURE proc_solution_del  
IS
BEGIN
DELETE FROM asks;
COMMIT;
END proc_solution_del;

END pack_solution;
/


SPOOL off;
commit;




