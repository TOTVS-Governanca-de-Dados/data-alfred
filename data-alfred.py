import os

def create_project_structure():
    print("Criando seu projeto de dados")

    # Criar diretório data e seus subdiretórios
    data_dirs = ['data/preprocessed', 'data/raw', 'data/mischaracterized']
    for dir in data_dirs:
        os.makedirs(dir, exist_ok=True)
    
    # Criar diretório docs e arquivos dentro dele
    os.makedirs('docs', exist_ok=True)
    with open('docs/mkdocs.md', 'a') as f:
        pass
    with open('docs/config.yml', 'a') as f:
        pass
    
    # Criar outros diretórios e arquivos específicos
    os.makedirs('models', exist_ok=True)
    os.makedirs('notebooks', exist_ok=True)
    os.makedirs('frontend', exist_ok=True)
    with open('frontend/__init__.py', 'a') as f:
        pass
    with open('frontend/streamlit_app.py', 'a') as f:
        pass
    
    os.makedirs('references', exist_ok=True)
    os.makedirs('reports', exist_ok=True)
    
    # Criar diretório src e subdiretórios, além de __init__.py
    src_dirs = ['src/visualization', 'src/data', 'src/features', 'src/models', 'src/tests']
    for dir in src_dirs:
        os.makedirs(dir, exist_ok=True)
    with open('src/__init__.py', 'a') as f:
        pass

    # Criar arquivos na raiz do projeto
    root_files = ['.env', '.gitignore', 'README.md', 'requirements.txt', 'setup.py', 'test_environment.py', 'Dockerfile']
    for file in root_files:
        with open(file, 'a') as f:
            pass
    
    print("Alfred finalizado")

create_project_structure()
