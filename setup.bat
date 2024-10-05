pip install -r requirements.txt

git clone https://github.com/thenaterhood/python-autocite.git

xcopy "%cd%\__main__.py" "%cd%\python-autocite\src\python_autocite\"  /y 

cd python-autocite
python setup.py install
cd ..