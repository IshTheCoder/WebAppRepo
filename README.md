# WebAppRepo
WebApp for 229 Repo

Here to save the script and data process


http://54.218.118.253:5000/

# Before run
pip install -r requirements.txt

# Before upload
pip freeze > requirements.txt

# FileSystem
-data,data2: save data
-assets: images and css file
-appUpdate: .py files to update app
-src: source file to generate figure
-testing: test files for pytest
-Sphinx: sphinx file for documents
application.py: main file to run dash
requirements.txt: environment document

# test
```
cd testing

coverage run --source ../src -m pytest   

coverage report -m 

coverage html   
```

then the html report will be in /testing/htmlcov/index.html

** Please do these to maintain the consistence of environment **
