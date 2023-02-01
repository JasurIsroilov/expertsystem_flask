from flask import Blueprint, redirect, render_template, url_for, flash, request
from flask_login import login_required

from ..models import SlotValueModel, SlotsFramesModel
from .forms import SlotValueForm, SlotsFramesForm


examplyar = Blueprint('examplyars', __name__)


@examplyar.route('/examplyars/', methods=['GET', 'POST'])
@examplyar.route('/examplyars/list', methods=['GET', 'POST'])
@login_required
def list_examplyars():
    rows = SlotsFramesModel.get_all()
    return render_template("examplyars/list.html", rows=rows)


@examplyar.route('/examplyars/value/edit', methods=['POST', 'GET'])
@login_required
def edit_examplyars():
    bar = request.args.to_dict()
    rows = SlotsFramesModel.get_table_by_id(bar.get('frm_id'))
    form = SlotsFramesForm()
    form.slt_name.choices = SlotsFramesModel.get_slots()
    form.slv_value.choices = SlotValueModel.get_slv_name()
    frm_name = SlotsFramesModel.get_frm_name_by_id(bar['frm_id'])
    if form.validate_on_submit():
        SlotsFramesModel.insert_examp_data(bar['frm_id'], form)
        flash('Успешно', category='success')
        return redirect(url_for('examplyars.edit_examplyars', frm_id=bar['frm_id'], frm_name=frm_name))
    return render_template('examplyars/examp_val_edit.html', form=form, rows=rows, frm_name=frm_name)


@examplyar.route('/examplyars/value/delete', methods=['GET', 'POST'])
@login_required
def del_exam_val():
    bar = request.args.to_dict()
    SlotsFramesModel.del_row(bar['sfr_id'])
    flash('Успешно', category='success')
    return redirect(url_for('examplyars.edit_examplyars', frm_id=bar['frm_id']))


@examplyar.route('/examplyars/slots/add', methods=['GET', 'POST'])
@login_required
def add_slot_value():
    form = SlotValueForm()
    rows = SlotValueModel.get_rows()
    if form.validate_on_submit():
        SlotValueModel.add_row(form.value.data)
        flash('Добавление успешно', category='success')
        return redirect(url_for('examplyars.add_slot_value'))
    return render_template('examplyars/slt_add.html', rows=rows, form=form)


@examplyar.route('/examplyars/slots/delete', methods=['GET', 'POST'])
@login_required
def delete_slot_value():
    bar = request.args.to_dict()
    SlotValueModel.delete_row(bar['slv_id'])
    flash('Удаление успешно', category='success')
    return redirect(url_for('examplyars.add_slot_value'))


@examplyar.route('/examplyars/slots/edit', methods=['GET', 'POST'])
@login_required
def edit_slot_value():
    bar = request.args.to_dict()
    form = SlotValueForm()
    row = SlotValueModel.get_row_by_id(bar['slv_id'])
    if form.validate_on_submit():
        SlotValueModel.edit_slot_value(slv_id=bar['slv_id'], value=form.value.data)
        flash('Изменение успешно', category='success')
        return redirect(url_for('examplyars.add_slot_value'))
    form.value.data = row.mappings().all()[0]['slv_val']
    return render_template('examplyars/slt_edit.html', form=form)
