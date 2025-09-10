from datetime import date

from pydantic import BaseModel, Field, RootModel, ConfigDict


class CreateOperationSchema(BaseModel):
    """
    Модель для создания новой банковской операции.
    
    Поля:
    - debit (float | None): Сумма списания со счёта
    - credit (float | None): Сумма зачисления на счёт
    - category (str): Категория операции
    - description (str): Описание операции
    - transaction_date (date): Дата транзакции (передаётся в формате "transactionDate")
    """
    model_config = ConfigDict(populate_by_name=True)  # Позволяет использовать alias при сериализации/десериализации

    debit: float | None
    credit: float | None
    category: str
    description: str
    transaction_date: date = Field(alias="transactionDate")  # Указываем alias для соответствия API


class UpdateOperationSchema(BaseModel):
    """
    Модель для обновления банковской операции (используется в PATCH запросах).

    Все поля являются необязательными, так как можно обновлять только часть данных.

    Поля:
    - debit (float | None): Новая сумма списания
    - credit (float | None): Новая сумма зачисления
    - category (str | None): Новая категория
    - description (str | None): Новое описание
    - transaction_date (date | None): Новая дата транзакции (alias "transactionDate")
    """
    model_config = ConfigDict(populate_by_name=True)

    debit: float | None
    credit: float | None
    category: str | None 
    description: str | None
    transaction_date: date | None = Field(alias="transactionDate")


class OperationSchema(CreateOperationSchema):
    """
    Модель банковской операции, содержащая ID.
    
    Наследуется от CreateOperationSchema и добавляет поле:
    - id (int): Уникальный идентификатор операции
    """
    id: int


class OperationsSchema(RootModel):
    """
    Контейнер для списка операций.
    
    Поле:
    - root (list[OperationSchema]): Список операций
    """
    root: list[OperationSchema]