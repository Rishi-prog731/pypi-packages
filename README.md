PyPi Package Starter
This GitHub repository has a shell for a PyPi package which includes a master file, a dist file, your .egg-info file, your secondary file, along with a changelog, license, manifest, and setup template. I have put my information in the setup file just incase you have questions and want to contact me.

Commands
pip install setuptools
pip3 install setuptools twine
cd C:\Users\USER\Desktop\beginnerpackage
Windows - dir
Linux/ Mac - ls
python3 setup.py sdist
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
Enter your username: 
Enter your password:
Acknowledgements
https://pypi.org/
Installation
Once you upload your package, you will get a pip install "package-name" which you can run and you will recieve the functionality brought within the package.

  pip install "package-name"
  cd "beginnerpackage"
License
MIT

Authors
@Rishi Hariharaprasad
