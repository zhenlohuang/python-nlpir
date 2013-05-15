swig -c++ -python NLPIR.interface
copy NLPIR.dll %SYSTEMROOT%\system32\ 
python setup.py build_ext --inplace
python setup.py install
pause