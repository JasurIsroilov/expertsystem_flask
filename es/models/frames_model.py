from ..config import db


class FramesModel(db.Model):

    __tablename__ = 'frames'

    frm_id = db.Column(db.Integer, primary_key=True)
    frm_parent_id = db.Column(db.Integer, nullable=True)
    frm_name = db.Column(db.String(50), nullable=False)
    frm_examplyar = db.Column(db.Integer, nullable=False)

    def __init__(self, frm_name: str, frm_examplyar: str, parent_name: str):
        self.frm_name = frm_name
        self.frm_examplyar = frm_examplyar
        self.frm_parent_id = self.get_parent_id_by_name(parent_name)

    def add_frame(self):
        db.session.execute(f"BEGIN prod_frames.frames_add('{self.frm_name}', {1 if self.frm_examplyar else 0}, "
                           f"{self.frm_parent_id}); COMMIT; END;")
        db.session.commit()

    @staticmethod
    def get_select_field():
        field = []
        rows = FramesModel.query.filter(FramesModel.frm_examplyar == '0').all()
        for row in rows:
            field.append(row.frm_name)
        return field

    @staticmethod
    def get_parent_id_by_name(parent_name):
        row = FramesModel.query.filter(FramesModel.frm_name == parent_name).first()
        print(f'Достал родитель --- {row.frm_id}')
        return row.frm_id

    @staticmethod
    def edit_frame(old, form):
        old.frm_name = form.name.data
        old.frm_examplyar = 1 if form.is_instance.data else 0
        old.frm_parent_id = old.get_parent_id_by_name(form.parent.data)
        db.session.execute(f"BEGIN prod_frames.frames_update({old.frm_id}, '{old.frm_name}', {old.frm_examplyar}, "
                           f"{old.frm_parent_id}); COMMIT; END;")
        db.session.commit()

    @staticmethod
    def delete_frame(frm_id):
        db.session.execute(f"BEGIN prod_frames.frames_delete({frm_id}); COMMIT; END;")
        db.session.commit()
