# Virtual Environments

#### To install virtual environment
```bash
pip install virtualenv
```
#### Create a directory to make our virtual environments
```bash
mkdir Environments
```
```bash
cd Environments
```

#### Create a virtual Environment
```bash
virtualenv project1_env
```

#### Activate this virtual env
source project1_env/bin/activate

#### List of all packages installed with versions in current environment

```bash
pip list 
```
#### Export these package names and versions to a file
Takes only local entities that we had in the python environment
```bash
pip freeze --local > requirements.txt
```
```bash
which python
```
#### To deactivate the virtual environment
```bash
deactivate
```
#### To delete the venv
```bash
rm -rf project1_env/
```

#### We can specify the version of python that we need
```bash
virtualenv -p /usr/bin/python3.5 py35_env
```
```bash
source py35_env/bin/activate
```
