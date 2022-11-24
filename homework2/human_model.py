from pydantic import BaseModel, ValidationError, validator
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from dataclasses import dataclass as _basemodel_decorator
else:
    _basemodel_decorator = lambda x: x


@_basemodel_decorator
class HumanModel(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

    @validator('age')
    def age_must_positive(cls, age):
        if age < 0:
            raise ValueError('age must be positive')

    @validator('sex')
    def sex_categorical(cls, sex):
        if sex != 0 and sex != 1:
            raise ValueError('sex must be 0 or 1')

    @validator('cp')
    def cp_categorical(cls, cp):
        if cp not in [0, 1, 2, 3]:
            raise ValueError(f'cp must be in {[0, 1, 2, 3]}')

    @validator('fbs')
    def fbs_categorical(cls, fbs):
        values = [0, 1]
        if fbs not in values:
            raise ValueError(f'fbs must be int {values}')

    @validator('restecg')
    def restecg_categorical(cls, restecg):
        values = [0, 1, 2]
        if restecg not in values:
            raise ValueError(f'restecg must be int {values}')

    @validator('exang')
    def exang_categorical(cls, exang):
        values = [0, 1]
        if exang not in values:
            raise ValueError(f'exang must be int {values}')

    @validator('slope')
    def slope_categorical(cls, slope):
        values = [0, 1, 2]
        if slope not in values:
            raise ValueError(f'slope must be int {values}')

    @validator('ca')
    def ca_categorical(cls, ca):
        values = [0, 1, 2, 3]
        if ca not in values:
            raise ValueError(f'ca must be int {values}')

    @validator('thal')
    def thal_categorical(cls, thal):
        values = [0, 1, 2]
        if thal not in values:
            raise ValueError(f'thal must be int {values}')
