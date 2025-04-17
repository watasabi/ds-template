"""
# We use a docstring here so that we have a valid Python file that allows us to access the Jinja2 templating engine

{{ cookiecutter.update({ "full_name": prompt_user("full_name", get_user_name())})}}
{{ cookiecutter.update({ "email": prompt_user("email", get_user_email())})}}
{{ cookiecutter.update({ "use_git": prompt_user_choices("use_git", ["Yes", "No"])})}}

{% if cookiecutter.use_git == "Yes" %}
{{ cookiecutter.update({"default_branch": branch_name("default_branch", "main")}) }}
{% else %}
{{ cookiecutter.update({"default_branch": ''}) }}
{% endif %}

"""
