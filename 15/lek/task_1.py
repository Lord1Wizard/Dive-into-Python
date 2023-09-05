import logging
from other import log_all


logging.basicConfig(level=logging.WARNING)

logger = logging.getLogger(__name__)

logger.info('Немного информации')
logger.error('Поймали ошибку')
logger.error(__name__)
logging.error(__name__)

logger = logging.getLogger('Основной файл проекта')
logger.warning('Внимание! Используем вызов функции из другого модуля')
log_all()
