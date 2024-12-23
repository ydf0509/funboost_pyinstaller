import sys
# print(1,sys.path)
# import nb_log_config
# print(2,sys.path)
# import funboost_config
# print(3,sys.path)
# from funboost.utils.dependency_packages_in_pythonpath import add_to_pythonpath
# # print(4,sys.path)
# from funboost.utils.dependency_packages_in_pythonpath import aioredis,func_timeout

print(5,sys.path)

from funcs.fun1 import f1

from  funcs.fun2 import f2


if __name__ == '__main__':

    f1.consume()
    f2.consume()