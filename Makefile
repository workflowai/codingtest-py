
.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: run
run:
	PYTHONPATH=. uvicorn main:app --host 0.0.0.0 --port 8000 --reload

.PHONY: test
test:
	PYTHONPATH=. pytest
