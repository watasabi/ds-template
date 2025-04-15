import sys
import cookiecutter.prompt
'''
This pre_gen is to avoid to input tests variables if you don't want to create it
'''

descriptions = {
    "default_branch":"Name of the default-branch:"
}

if "{{ cookiecutter.use_git }}" == "yes":
    cookiecutter.prompt.read_user_variable("default_branch","main", descriptions)
    

else:
    """{{ cookiecutter.update(
        {
            "default_branch": "",
        }
    )}}"""

sys.exit(0)