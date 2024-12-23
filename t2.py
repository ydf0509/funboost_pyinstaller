

# D:/ProgramData/Miniconda3/envs/py39b/Lib/site-packages/funboost/utils/dependency_packages_in_pythonpath/


import funboost,os
import site
from pathlib import Path
print(os.path.dirname(funboost.__file__))

print(Path(site.getsitepackages()[0]).joinpath('funboost/utils/dependency_packages_in_pythonpath').absolute().as_posix())