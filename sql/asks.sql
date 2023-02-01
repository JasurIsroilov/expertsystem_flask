SPOOL asks.lst

PROMPT Creating table asks asks

DROP TABLE asks;
CREATE TABLE asks (
		ask_id         INTEGER NOT NULL,
		ask_num	       INTEGER,
		ask_val        VARCHAR2(200)		
)
TABLESPACE USERS;


PROMPT Creating index

DROP INDEX i_ask_id;
CREATE UNIQUE INDEX i_ask_id ON asks(ask_id)
TABLESPACE USERS;

PROMPT Creating pk

ALTER TABLE asks
DROP CONSTRAINT i_ask_pk;
ALTER TABLE asks
ADD (CONSTRAINT i_ask_pk PRIMARY KEY (ask_id));

PROMPT Creating sequence

DROP SEQUENCE s_asks;
CREATE SEQUENCE s_asks;

PROMPT Creating trigger on inserts

CREATE OR REPLACE TRIGGER t_ins_asks
BEFORE INSERT ON asks FOR EACH ROW
BEGIN
  SELECT s_asks.NEXTVAL
  INTO :new.ask_id
  FROM dual;
END;
/

PROMPT Creating trigger on update
CREATE OR REPLACE TRIGGER t_upd_asks
BEFORE UPDATE ON asks FOR EACH ROW
BEGIN
  if (:new.ask_id != :old.ask_id) THEN
    :new.ask_id := :old.ask_id;
  END IF;
END;
/


PROMPT Creating synonym

DROP PUBLIC SYNONYM asks;
CREATE PUBLIC SYNONYM asks FOR asks;

spool off
commit;