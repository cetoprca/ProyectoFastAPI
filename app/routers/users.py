from fastapi import APIRouter,Depends
from routers.schemas import User,UpdateUser,ShowUser
from db.database import get_db
from sqlalchemy.orm import Session
from db import models

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.get("/")
def getUsers(db: Session=Depends(get_db)):
    data = db.query(models.User).all()
    
    usuarios = []
    
    for user in data:
        usuarios.append(
            ShowUser(
                id=user.id,
                username=user.username,
                nombre=user.nombre,
                correo=user.correo
            )
        )
    
    return usuarios

@router.post("/add")
def addUser(user:User, db:Session=Depends(get_db)):
    usuario = user.model_dump()
    nuevo_usuario = models.User(
        username = usuario["username"],
        password = usuario["password"],
        nombre = usuario["nombre"],
        apellido = usuario["apellido"],
        direccion = usuario["direccion"],
        telefono = usuario["telefono"],
        correo = usuario["correo"],
    )
    
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return{"message": "Usuario creado"}

@router.get("/{user_id}")
def obtener_usuario(user_id:int, db:Session=Depends(get_db)):
    usuario = db.query(models.User).filter(models.User.id == user_id).first()
    if not usuario:
        return{"message": "Usuario no encontrado"}
    return ShowUser(
                id=usuario.id,
                username=usuario.username,
                nombre=usuario.nombre,
                correo=usuario.correo
            )


@router.delete("/user/{user_id}")
def eliminar_usuario(user_id:int, db:Session=Depends(get_db)):
    usuario = db.query(models.User).filter(models.User.id == user_id).first()
    if not usuario:
        return{"message": "Usuario no encontrado"}
    db.delete(usuario) 
    db.commit()   
    return{"message": "Usuario eliminado"}

@router.patch("/{user_id}")
def actualizar_usuario(user_id:int, updateUser:UpdateUser, db:Session=Depends(get_db)):
    usuario = db.query(models.User).filter(models.User.id == user_id)
    if not usuario.first():
        return{"message": "Usuario no encontrado"}
    usuario.update(updateUser.model_dump(exclude_unset=True))
    db.commit()
    return{"message": "Usuario actualizado"}
