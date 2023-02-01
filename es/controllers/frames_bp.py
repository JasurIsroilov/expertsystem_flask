from flask import render_template, Blueprint, flash, redirect, request, url_for
from flask_login import login_required

from ..models import FramesModel
from .forms import FramesForm


frame = Blueprint('frames', __name__)


class FramesNode:
    def __init__(self, row_obj):
        self.row = row_obj
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        if not isinstance(self.row, str):
            print(self.row.frm_name)
        if self.children:
            for child in self.children:
                child.print_tree()


# def build_tree(rows):
#     root = FramesNode('TreeRoot')
#     # Adding level-0 nodes
#     for row in rows:
#         if row.frm_parent_id is None:
#             root.add_child(FramesNode(row))
#     # Adding other level nodes
#     for child in root.children:
#         for row in rows:
#             if row.frm_parent_id == child.row.frm_id:
#                 child.add_child(FramesNode(row))
#     return root


@frame.route('/frames/', methods=['GET', 'POST'])
@frame.route('/frames/list', methods=['GET', 'POST'])
@login_required
def frames_list():
    rows = FramesModel.query.all()
    return render_template('frames/list.html', rows=rows)


@frame.route('/frames/add', methods=['GET', 'POST'])
@login_required
def add_frame():
    form = FramesForm()
    form.parent.choices = FramesModel.get_select_field()
    if form.validate_on_submit():
        new_frame = FramesModel(frm_name=form.name.data, frm_examplyar=form.is_instance.data,
                                parent_name=form.parent.data)
        new_frame.add_frame()
        flash('Фрейм добавлен', category='success')
        return redirect(url_for('frames.frames_list'))
    return render_template('frames/add.html', form=form)


@frame.route('/frames/edit', methods=['GET', 'POST'])
@login_required
def edit_frame():
    bar = request.args.to_dict()
    old_frame = FramesModel.query.get_or_404(bar.get('frm_id'))
    form = FramesForm()
    form.parent.choices = FramesModel.get_select_field()
    if form.validate_on_submit():
        FramesModel.edit_frame(old_frame, form)
        flash('Редактирование успешно', 'success')
        return redirect(url_for('frames.frames_list'))
    form.name.data = old_frame.frm_name
    form.is_instance.data = True if old_frame.frm_examplyar else False
    return render_template('frames/edit.html', form=form)


@frame.route('/frames/delete', methods=['GET', 'POST'])
@login_required
def delete_frame():
    bar = request.args.to_dict()
    FramesModel.delete_frame(bar.get('frm_id'))
    flash('Удаление успешно', category='success')
    return redirect(url_for('frames.frames_list'))
