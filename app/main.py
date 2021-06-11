from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
	if current_user.is_authenticated:
		return render_template('index.html', title='Flask App', logged=True)
	else:
		return render_template('index.html', title='Flask App')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title='Profile', logged=True, name=current_user.name)