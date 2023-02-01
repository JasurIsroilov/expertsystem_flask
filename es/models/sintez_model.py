from ..config import db


class SintezModel(db.Model):

    __tablename__ = 'asks'

    ask_id = db.Column(db.Integer, primary_key=True)
    ask_num = db.Column(db.Integer, nullable=True)
    ask_val = db.Column(db.String(200), nullable=True)

    @staticmethod
    def get_slv_val():
        return db.session.execute(f"SELECT * FROM slot_value").mappings().all()

    @staticmethod
    def get_slots():
        return db.session.execute(f"SELECT * FROM slots ORDER BY slt_name").mappings().all()

    @staticmethod
    def clear_asks():
        db.session.execute("BEGIN pack_solution.proc_solution_del; COMMIT; END;")

    @staticmethod
    def add_answer(slt_name, slv_val):
        db.session.execute("INSERT INTO asks"
                           "(ask_num, ask_val)"
                           f"VALUES"
                           f"((SELECT slt_id FROM slots WHERE slt_name='{slt_name}'), "
                           f"'{slv_val}')")
        db.session.commit()

    @staticmethod
    def check_answer():
        answers = db.session.execute("SELECT slt_name, ask_val FROM asks, slots "
                                     "WHERE slt_id=ask_num").mappings().all()
        asks = [(answer['slt_name'], answer['ask_val']) for answer in answers]
        choices = {}
        frames = db.session.execute("SELECT frm_name FROM frames").mappings().all()
        for frame in frames:
            query = db.session.execute("SELECT slt_name, sfr_slt_id, slv_val, frm_name FROM slots_frames, "
                                       "frames, slot_value, slots "
                                       "WHERE frm_examplyar=1 "
                                       "AND frm_id=sfr_frm_id "
                                       "AND slv_id=sfr_slv_id "
                                       "AND slt_id=sfr_slt_id "
                                       f"AND frm_name='{frame['frm_name']}' "
                                       "ORDER BY sfr_frm_id").mappings().all()
            if query:
                tmp = []
                for row in query:
                    tmp.append((row['slt_name'], row['slv_val']))
                choices[frame['frm_name']] = tmp
        for key, value in choices.items():
            i = 0
            for ask in asks:
                if ask not in value:
                    break
                else:
                    i += 1
            if i == len(value):
                return {'frame': key,
                        'choices': value}
        return {'frame': '',
                'choices': []}
