conda create -n xportrait python=3.10 -y
conda activate xportrait

pip install -r requirements.txt

pip install -e ../expdata
pip install gdown
gdown --folder https://drive.google.com/drive/folders/1Bq0n-w1VT5l99CoaVg02hFpqE5eGLo9O --output checkpoint
# sudo apt install python3-tk