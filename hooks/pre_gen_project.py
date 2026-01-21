"""
{{ cookiecutter.update({ "full_name": cookiecutter.full_name if cookiecutter.full_name != "Your Name" else get_git_user_name() }) }}
{{ cookiecutter.update({ "email": cookiecutter.email if cookiecutter.email != "Your Email" else get_git_user_email() }) }}
"""

import sys

project_slug = "{{ cookiecutter.project_slug }}"
if hasattr(project_slug, "isidentifier"):
    if not project_slug.isidentifier():
        print(
            f"ERROR: O slug do projeto '{project_slug}' não é um nome válido de pacote Python."
        )
        sys.exit(1)
