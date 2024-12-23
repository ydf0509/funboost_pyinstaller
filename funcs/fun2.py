from funboost import BoosterParams, BrokerEnum, funboost_current_task
from funboost.constant import FunctionKind


@BoosterParams(queue_name='installer_q2', consuming_function_kind=FunctionKind.COMMON_FUNCTION,
               broker_kind=BrokerEnum.REDIS)
def f2(x):
    fct = funboost_current_task()
    fct.logger.info(f'f2: {x}')
