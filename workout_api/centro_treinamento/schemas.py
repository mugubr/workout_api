from typing import Annotated
from pydantic import UUID4, Field
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT King', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do centro de treinamento', example='Rua X, QD Y', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietário do centro de treinamento', example='Pedro', max_length=30)]
    
class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]
    
class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT King', max_length=20)]