# Install modules python
install:
	python3 -m venv env
	env/bin/python3 -m pip install -r requirements.txt

# Run application
list:
	env/bin/pip list

# Remove python modules
remove:
	rm -rf env/ activate

# Set environment
set:
	export FLASK_APP=wsgi.py

# Run application
run:
	env/bin/gunicorn --bind 127.0.0.1:8005 wsgi:app --log-level="debug" --reload --workers 1 --threads 1 --capture-output --log-syslog

# Backup modules python installed
freeze:
	rm requirements.txt
	touch requirements.txt
	env/bin/python -m pip freeze >> requirements.txt

shell:
	env/bin/flask shell

# Install packages APT
install_apt:
	sudo apt-get update
	sudo apt install nginx supervisor -y
	systemctl enable supervisor
	systemctl enable nginx

# config logal project in port 80
config_local:
	sudo ln -s config/supervisor.conf /etc/supervisorctl/conf.d/cache_app.conf
	sudo ln -s config/nginx.conf /etc/nginx/sites_enabled/cache_app
	sudo supervisorctl update
	sudo service nginx restart
	ps aux | grep cache_app
