.PHONY: data alfred create project data science

data-alfred:
	@echo "Criando seu projeto de dados"
	mkdir -p data
	cd data && mkdir preprocessed raw mischaracterized
	cd ..
	mkdir -p docs
	cd docs && touch mkdocs.md && touch config.yml
	cd ..
	mkdir -p models notebooks frontend
	cd frontend && touch __init__.py streamlit_app.py
	cd .. && mkdir -p references 
	mkdir reports
	mkdir src
	cd src && touch __init__.py && mkdir visualization data features models tests
	cd ./ && touch .env .gitignore README.md requirements.txt setup.py test_environment.py Dockerfile
	# touch Makefile
	@echo "Alfred finalizado"