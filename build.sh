python3 -m pip install --upgrade build
python3 -m build 
echo "Uploading to TestPyPi"
twine upload --repository testpypi dist/*
echo "Uploading to PyPi"
twine upload dist/* 