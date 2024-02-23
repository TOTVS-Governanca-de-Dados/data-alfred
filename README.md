# Data Alfred: Structuring Data Projects in Seconds

## About the Project

Data Alfred is a tool designed to streamline the setup of new data projects by creating essential folders and files structure in seconds. Aimed at data teams and data analysis projects, Data Alfred establishes a solid and standardized foundation, allowing data scientists and analysts to focus on what truly matters: extracting valuable insights from data.

## Features

- Creates directories for raw, preprocessed, and mischaracterized data.
- Initializes directories for documentation, machine learning models, Jupyter notebooks, frontend for interactive visualizations, and references.
- Prepares a source code directory structure for visualization, data manipulation, feature engineering, models, and testing.
- Generates initial files, including `.env` for environment variables, `.gitignore`, `README.md`, `requirements.txt` for dependencies, `setup.py` for package installation, `test_environment.py` for testing, and a `Dockerfile` for containerization.

## Prerequisites

To use Data Alfred, you will need to have Python installed on your system. The tool has been developed and tested in environments supporting Python 3.6 or newer.

## How to Install

```bash
pip install data-alfred
```

## How to Use

```bash
python data-alfred
```

1. Data Alfred will take care of the rest, creating the necessary directory and file structure for your data project.

## Created Directory Structure

- `data/`: Subdivided into `preprocessed`, `raw`, and `mischaracterized` for different stages of data handling.
- `docs/`: Contains `mkdocs.md` and `config.yml` for project documentation.
- `models/`: Intended to store trained machine learning models.
- `notebooks/`: For Jupyter notebooks of data analysis and exploration.
- `frontend/`: Includes `__init__.py` and `streamlit_app.py` for development of data visualization applications.
- `references/`: To store project references and resources.
- `reports/`: Intended for data analysis reports and visualizations.
- `src/`: Contains subdirectories for `visualization`, `data`, `features`, `models`, and `tests`, along with an `__init__.py` to treat the contents as a Python package.

## Contributing

Contributions to Data Alfred are welcome! If you have a suggestion to improve this tool, feel free to open an issue or pull request on the project repository. Let's work together to make starting data projects a quick and effortless task!

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Alestan - privacidade@totvs.com.br

Project Link: [https://github.com/TOTVS-Privacidade-de-Dados/data-alfred](https://github.com/TOTVS-Privacidade-de-Dados/data-alfred)

---
