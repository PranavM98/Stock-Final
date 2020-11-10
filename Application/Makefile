install:

		pip install -r requirements.txt


lint:
	pylint --disable=R,C application.py &&\
	pylint --disable=R,C prediction.py
	

all: install lint 