from ..config import db


class SlotsModel(db.Model):

    __tablename__ = 'slots'

    slt_id = db.Column(db.Integer, primary_key=True)
    slt_name = db.Column(db.String(50), nullable=False)
    slt_describe = db.Column(db.String(300), nullable=True)

    def __init__(self, slt_name, slt_describe):
        self.slt_name = slt_name
        self.slt_describe = slt_describe

    def add_slot(self):
        db.session.execute(f"BEGIN prod_slots.slots_add('{self.slt_name}', '{self.slt_describe}'); COMMIT; END;")
        db.session.commit()

    @staticmethod
    def delete_slot(slt_id):
        db.session.execute(f"BEGIN prod_slots.slots_delete({slt_id}); COMMIT; END;")
        db.session.commit()

    @staticmethod
    def edit_slot(slt_id, form):
        db.session.execute(f"BEGIN prod_slots.slots_update('{slt_id}', "
                           f"'{form.name.data}', '{form.description.data}'); COMMIT; END;")
        db.session.commit()
