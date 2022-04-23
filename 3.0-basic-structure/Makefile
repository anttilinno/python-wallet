run:
	pdm run python -m wallet

unittest:
	pdm run python -m pytest tests/unit/*

coverage:
	pdm run coverage run --source=wallet -m pytest tests/unit/*.py
	pdm run coverage report

cov_html:
	pdm run coverage run --source=wallet -m pytest tests/unit/*.py
	pdm run coverage html

clean:
	rm -f wallet/__pycache__
