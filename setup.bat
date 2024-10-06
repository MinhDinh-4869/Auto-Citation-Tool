@echo off
pip install -r requirements.txt

git clone https://github.com/MinhDinh-4869/python-autocite.git

cd python-autocite
python setup.py install
cd ..