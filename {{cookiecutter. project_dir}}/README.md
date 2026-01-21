<a name="readme-top"></a>

<div align="center">

  <h1 align="center">{{ cookiecutter.project_name }}</h1>

  <p align="center">
    {{ cookiecutter.project_desc }}
    <br />
    <br />
    <a href="#getting-started"><strong>Explorar a documentação »</strong></a>
    <br />
    <br />
    <img src="https://img.shields.io/badge/Python-X.XX-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/Status-Development-yellow?style=for-the-badge" alt="Status">
    <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
  </p>
</div>

<details>
  <summary>📝 Tabela de Conteúdos</summary>
  <ol>
    <li><a href="#sobre-o-projeto">Sobre o Projeto</a></li>
    <li><a href="#organizacao-e-estrutura">Organização e Estrutura</a></li>
  </ol>
</details>

---

## 🧐 Sobre o Projeto

Uma breve descrição do contexto de negócio, objetivos e metodologia deste projeto.

### Principais Stakeholders
* **Nome** (Area/Cargo) - [email@exemplo.com]
* **Nome** (Area/Cargo) - [email@exemplo.com]

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## 📂 Organização e Estrutura

Este projeto segue uma estrutura padronizada para garantir reprodutibilidade.

> **Nota sobre Convenção de Nomes:**
> Arquivos numerados (ex: `01_load_data.py`) indicam **ordem de execução** em pipelines ou análises.
> Código reutilizável (funções/classes) deve residir em `src/` ou `utils/` e ser importado.

```text
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

