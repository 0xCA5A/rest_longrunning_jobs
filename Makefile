default: run

init:
	python3 -m venv venv

install:
	venv/bin/pip install -r requirements.txt

venv:
	source venv/bin/venv

run:
	venv/bin/python app.py

clean:
	rm -rf venv
