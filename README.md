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
├── config
│   └── pipe_env
│       └── env.yml
├── data
│   ├── external
│   ├── interim
│   ├── processed
│   └── raw
├── LICENSE
├── notebooks
├── pipe
│   ├── azureml_env_build.py
│   ├── azureml_pipe_orchestrator.py
│   ├── src
│   │   ├── 01_load_data.py
│   │   ├── 02_preprocessing.py
│   │   ├── 03_model_inference.py
│   │   ├── 04_post_processing.py
│   │   └── __init__.py
│   └── utils
│       ├── compare_env_version.py
│       └── __init__.py
├── README.md
├── references
└── reports
    └── figures
```
