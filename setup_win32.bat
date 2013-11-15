swig -c++ -python .\win32\NLPIR.interface
copy .\win32\NLPIR.dll %SYSTEMROOT%\system32\ 
python setup.py build_ext --inplace
python setup.py install
pause