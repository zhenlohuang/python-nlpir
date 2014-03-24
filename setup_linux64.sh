swig -c++ -python NLPIR.interface
sudo cp ./lib/linux64/libNLPIR.so /usr/lib64/
python setup.py build_ext --inplace
python setup.py install
