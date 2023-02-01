from ..config import db


class SlotsFramesModel(db.Model):

    __tablename__ = 'slots_frames'

    sfr_id = db.Column(db.Integer, primary_key=True)
    sfr_slt_id = db.Column(db.Integer, nullable=False)
    sfr_slv_id = db.Column(db.Integer, nullable=False)
    sfr_frm_id = db.Column(db.Integer, nullable=False)

    @staticmethod
    def add_row(slt_id, slv_id, frm_id):
        db.session.execute(f"BEGIN prod_slots_frames.slots_frames_update({frm_id}, {slt_id}, {slv_id}); COMMIT; END;")

    @staticmethod
    def get_exs():
        query = db.session.execute(f"SELECT * FROM frames WHERE frm_examplyar=1")
        return query.mappings().all()

    @staticmethod
    def get_slots():
        query = db.session.execute(f"SELECT * FROM slots")
        return [row['slt_name'] for row in query.mappings().all()]

    @staticmethod
    def get_table_by_id(sfr_frm_id):
        try:
            query = db.session.execute(f"SELECT sfr_id, sfr_slt_id, sfr_slv_id, sfr_frm_id, slt_name, slv_val, frm_name "
                                       f"FROM slots_frames, frames, slot_value , slots "
                                       f"WHERE sfr_frm_id={sfr_frm_id} "
                                       f"AND slt_id=sfr_slt_id "
                                       f"AND slv_id=sfr_slv_id "
                                       f"AND frm_id=sfr_frm_id")
        except:
            return []
        else:
            return query.mappings().all()

    @staticmethod
    def insert_examp_data(frm_id, form):
        query = db.session.execute(f"SELECT slt_id FROM slots WHERE slt_name='{form.slt_name.data}'")
        sfr_slt_id = query.mappings().all()[0]['slt_id']
        query = db.session.execute(f"SELECT slv_id FROM slot_value WHERE slv_val='{form.slv_value.data}'")
        sfr_slv_id = query.mappings().all()[0]['slv_id']
        db.session.execute(f"BEGIN prod_slots_frames.slots_frames_update({frm_id}, {sfr_slt_id}, {sfr_slv_id}); "
                           f"COMMIT; END;")

    @staticmethod
    def get_frm_name_by_id(frm_id):
        query = db.session.execute(f"SELECT frm_name FROM frames WHERE frm_id={frm_id}")
        return query.mappings().all()[0]['frm_name']

    @staticmethod
    def del_row(sfr_id):
        db.session.execute(f"DELETE FROM slots_frames WHERE sfr_id={sfr_id}")
        db.session.commit()

    @classmethod
    def get_all(cls):
        jackson = []
        exs = cls.get_exs()
        for ex in exs:
            query = db.session.execute(f"SELECT * FROM slots, slot_value, frames, slots_frames "
                                       f"WHERE frm_examplyar=1 AND sfr_frm_id=frm_id AND sfr_slv_id=slv_id "
                                       f"AND sfr_slt_id=slt_id AND frm_id={ex['frm_id']}").mappings().all()
            tmp = {
                'frm_id': ex['frm_id'],
                'frm_name': ex['frm_name'],
            }
            if query:
                tmp['slots'] = query
            jackson.append(tmp)
        return jackson


class SlotValueModel(db.Model):

    __tablename__ = 'slot_value'

    slv_id = db.Column(db.Integer, primary_key=True)
    slv_value = db.Column(db.String(300), nullable=False)

    def __init__(self, slv_value):
        slv_value = slv_value

    @staticmethod
    def get_rows():
        return db.session.execute("SELECT * FROM slot_value")

    @staticmethod
    def add_row(value):
        db.session.execute(f"BEGIN prod_slot_value.slot_value_add('{value}'); COMMIT; END;")

    @staticmethod
    def delete_row(slv_id):
        db.session.execute(f"BEGIN prod_slot_value.slot_value_delete({slv_id}); COMMIT; END;")

    @staticmethod
    def get_row_by_id(slv_id):
        return db.session.execute(f"SELECT * FROM slot_value WHERE slv_id={slv_id}")

    @staticmethod
    def edit_slot_value(slv_id, value):
        db.session.execute(f"BEGIN prod_slot_value.slot_value_update({slv_id}, '{value}'); COMMIT; END;")

    @staticmethod
    def get_slv_name():
        query = db.session.execute(f"SELECT slv_val FROM slot_value")
        l = [row['slv_val'] for row in query.mappings().all()]
        return l
