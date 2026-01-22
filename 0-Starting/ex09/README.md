# Package

Create your first package in python the way you want, it will appear in the list of
installed packages when you type the command "pip list" and display its characteristics
when you type "pip show -v ft_package"

python -m build

python3 -m twine upload --repository testpypi dist/* --verbose

pip install -i <Link>

pip list

pip show -v ft_package
