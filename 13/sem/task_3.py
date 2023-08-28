# Создайте класс с базовым исключением и дочерние классыисключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class UserExeption(Exception):
    pass

class UserLevelExeption(UserExeption):
    pass

class UserPermissionExeption(UserExeption):
    pass

raise UserLevelExeption