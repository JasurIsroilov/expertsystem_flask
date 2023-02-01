from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_login import login_required

from .forms import SlotsForm
from ..models import SlotsModel


slot = Blueprint('slots', __name__)


@slot.route('/slots/', methods=['GET', 'POST'])
@slot.route('/slots/list', methods=['GET', 'POST'])
@login_required
def slots_list():
    rows = SlotsModel.query.all()
    return render_template('slots/list.html', rows=rows)


@slot.route('/slots/add', methods=['GET', 'POST'])
@login_required
def add_slot():
    form = SlotsForm()
    if form.validate_on_submit():
        new_slot = SlotsModel(slt_name=form.name.data, slt_describe=form.description.data)
        new_slot.add_slot()
        flash('Слот добавлен', category='success')
        return redirect(url_for('slots.slots_list'))
    return render_template('slots/add.html', form=form)


@slot.route('/slots/delete', methods=['GET', 'POST'])
@login_required
def delete_slot():
    bar = request.args.to_dict()
    SlotsModel.delete_slot(bar.get('slt_id'))
    flash('Удаление успешно', category='success')
    return redirect(url_for('slots.slots_list'))


@slot.route('/slots/edit', methods=['GET', 'POST'])
@login_required
def edit_slot():
    bar = request.args.to_dict()
    form = SlotsForm()
    row = SlotsModel.query.get_or_404(bar.get('slt_id'))
    if form.validate_on_submit():
        flash('Изменение успешно', category='success')
        SlotsModel.edit_slot(bar.get('slt_id'), form)
        return redirect(url_for('slots.slots_list'))
    form.name.data = row.slt_name
    form.description.data = row.slt_describe
    return render_template('slots/edit.html', form=form)
