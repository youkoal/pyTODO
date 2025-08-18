# pyTODO
TODO-list python desktop

https://doc.qt.io/qtforpython-6/gettingstarted.html

Create environment (Your Python executable might be called python3):

python -m venv .env


Activate the environment (Windows):

.env\Scripts\activate.bat


For the latest version:

pip install pyside6


================================
add a .gitignore to the root with :
# Exclude all __pycache__ directories
__pycache__/
**/__pycache__/

# Exclude config.json anywhere in the project
config.json
**/config.json

# Exclude Data folder
Data/
**/Data/
================================



Troubleshooting :
issue with JSON : delete "Data" folder and empty the "config.json" file => should be re-created


color palette : https://coolors.co/palette/6f1d1b-bb9457-432818-99582a-ffe6a7

#6F1D1B
#BB9457
#432818
#99582A
#FFE6A7
