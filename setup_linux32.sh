swig -c++ -python NLPIR.interface
sudo cp ./lib/linux32/libNLPIR.so /usr/lib/
python setup.py build_ext --inplace
python setup.py install
