swig -c++ -python NLPIR.interface
sudo cp libNLPIR.so /usr/lib
python setup.py build_ext --inplace
