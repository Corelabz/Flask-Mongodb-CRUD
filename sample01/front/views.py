from flask import render_template

from . import front
from ..models import County


@front.route('/')
def index():
	records = County.objects()
	return render_template('front/index.html', title='Home', records=records)