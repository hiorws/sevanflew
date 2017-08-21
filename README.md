# sevanflew


#### setting up development environment
```bash
git clone git@github.com:hiorws/sevanflew.git
cd sevanflew
virtualenv --python python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
```

if you add a new library please add it to requirements.txt with that command
```bash
pip3 freeze > requirements.txt
```
