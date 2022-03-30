from fastapi import HTTPException
from pydantic import UUID4

from src.core import database 


def delete(id: UUID4):
    db = database.connect()
    user = db.execute(
        'SELECT id FROM public.user WHERE id=:id',
        {'id': id}
    ).first()
    
    if not user:
        raise HTTPException(
            status_code=400,
            detail='Erro: Usuário não existe'
        )

    try:
        db.execute(
            'DELETE FROM public.user where id=:id',
            {'id':id}
        )
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
        raise HTTPException(
            status_code=400,
            detail='Erro: Não foi possivel deletar o usuario.'
        )
    
    return 'Usuário removido com sucesso!'
