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
if it is your first time with nltk, while venv is activated open python3 in interactive mode and run following commands:
```
import nltk
nltk.download()

```
This will pop-up a new window, download all resources and packages that you need.
