import os
from flask import Blueprint, request, redirect, render_template, url_for
from flask_login import login_required
from fpdf import FPDF

from .forms import SintezForm
from ..models import SintezModel


sintez = Blueprint('sintez', __name__)


@sintez.route('/sintez/sintez', methods=['GET', 'POST'])
@login_required
def start():
    SintezModel.clear_asks()
    rows = {'frame': '',
            'choices': []}
    return render_template('sintez/sintez.html', rows=rows)


@sintez.route('/sintez/process', methods=['GET', 'POST'])
@login_required
def process():
    bar = request.args.to_dict()
    stage = int(bar['stage'])
    form = SintezForm()
    form.slv_val.choices = [row['slv_val'] for row in SintezModel.get_slv_val()]
    if int(bar['stage']) > len(SintezModel.get_slots()):
        rows = SintezModel.check_answer()
        return render_template('sintez/sintez.html', rows=rows)
    slot = SintezModel.get_slots()[stage - 1]['slt_name']
    form.slt_name.data = slot
    if form.validate_on_submit():
        SintezModel.add_answer(slot, form.slv_val.data)
        return redirect(url_for('sintez.process', stage=stage+1, slt_name=slot))
    return render_template('sintez/process.html', form=form, stage=bar.get('stage'), slt_name=slot)


@sintez.route('/sintez/fpdf', methods=['GET', 'POST'])
@login_required
def fpdf():
    path = os.getcwd()
    rows = SintezModel.check_answer()
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_font('Arial', 'B', 14)
    pdf.add_page()
    pdf.image(fr'{path}\es\static\report.png', x=0, y=0, w=210, h=297)
    pdf.set_x(20)
    pdf.cell(200, 30, txt='Report By: Isroilov J.O.')
    pdf.ln(8)
    pdf.set_x(20)
    pdf.cell(200, 30, txt=rows['frame'])
    pdf.ln(8)
    for choice in rows['choices']:
        pdf.set_font("Arial", style='B', size=14)
        pdf.set_x(20)
        pdf.cell(200, 30, txt=choice[0])
        pdf.ln(8)
        pdf.set_font("Arial", size=14)
        pdf.set_x(20)
        pdf.cell(200, 30, txt=choice[1])
        pdf.ln(8)
    pdf.output(fr'{path}\es\static\report.pdf')
    return redirect(url_for('sintez.start'))

