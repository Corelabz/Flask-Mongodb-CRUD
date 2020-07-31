from flask import render_template, request, redirect, url_for

from . import backend
from . forms import CountyForm

from ..models import County


@backend.route('/admin')
def dashboard():
	count = County.objects().count()
	budget = County.objects().sum('amount')
	return render_template('backend/index.html', count=count, title="Dashboard", budget=budget)

@backend.route('/admin/record/create', methods=['GET', 'POST'])
def create():
	form = CountyForm()
	if form.validate_on_submit(): 
		data = County(
			name=form.name.data,
			year=form.year.data,
			amount=form.amount.data
		)
		data.save()
		return redirect(url_for('backend.dashboard'))
	return render_template('backend/add.html', title="Add Record", form=form)

@backend.route('/admin/records/read')
def read():
	records = County.objects()
	return render_template('backend/list.html', records=records)

@backend.route('/record/update/<record_id>', methods=['GET', 'POST'])
def update(record_id):
	record = County.objects.get_or_404(id=record_id)
	form = CountyForm()
	if form.validate_on_submit():
		record.update(
			name=form.name.data,
			year=form.year.data,
			amount=form.amount.data
		)
		return redirect(url_for('.read'))

	return render_template('backend/edit.html', title="Update", record=record, form=form)

@backend.route('/record/delete/<record_id>')
def delete(record_id):
	record = County.objects.get_or_404(id=record_id)
	record.delete()
	return redirect(url_for('backend.read'))