# Data Science Project Template

## Authors
- [Watasabi](https://github.com/watasabi)
- [Blaugi](https://github.com/blaugi)

## Getting Started
TODO
```bash
uvx cookiecutter gh:RepoName 
```

## Project Organization
```
.
├── config/                 # Configurações globais e de ambiente
│   └── pipe_env/           # Configs específicas do Pipeline (YAML, JSON)
│
├── data/                   # Dados do projeto (Geralmente ignorados pelo Git)
│   ├── external/           # Dados de fontes terceiras
│   ├── interim/            # Dados transformados intermediários
│   ├── processed/          # Dados finais prontos para modelagem
│   └── raw/                # Dados originais imutáveis
│
├── notebooks/              # Jupyter Notebooks para exploração e rascunho
│   ├── eda/                # 00_eda, 01_analise_inicial...
│   └── modeling/           # Testes de modelos antes da produção
│
├── pipe/                   # Orquestração e Pipeline de Produção
│   ├── orchestrator.py     # Orquestrador (ex: Azure ML, Airflow)
│   ├── src/                # Steps do pipeline (Scripts numerados)
│   │   ├── 01_load.py
│   │   ├── 02_preprocess.py
│   │   ├── 03_inference.py
│   │   └── 04_postprocess.py
│   └── utils/              # Utilitários específicos do pipeline
│
├── reports/                # Relatórios gerados, html, pdf
│   └── figures/            # Gráficos e imagens geradas pelos códigos
│
├── src/                    # Código Fonte Reutilizável (Library do projeto)
│   └── __init__.py         # Funções de engenharia de features
│
├── .gitignore              # Arquivos a serem ignorados pelo git
├── LICENSE                 # Licença do projeto
└── README.md               # Documentação principal


```
