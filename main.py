import os
import asyncio
from sqlalchemy import create_engine, update

from urllib.parse import urlparse

from flask import Flask, jsonify, request


import json
from sqlalchemy import String, Text,  select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


from sqlalchemy.orm import Session



import json





tmpPostgres = urlparse(os.getenv("DATABASE_URL"))
engine = create_engine("postgresql+psycopg2://postgres:fjpVGKopERksWfGjqDONtacLdDEeVuSc@junction.proxy.rlwy.net:34197/railway", echo=True)

    
class Base(DeclarativeBase): pass
class Product(Base):
    __tablename__ = 'product'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(Text)

def async_main() -> None:
    
    with engine.begin() as conn:
        Base.metadata.create_all
    
        app.run(host="0.0.0.0", port=5000, debug=True)   
        
def one(session):
        orm_query_add(session=session,name='Диван',desc='Неплохой')
        orm_query_add(session=session,name='Диван2',desc='Неплохой2')



   

#====================================================================


class Base(DeclarativeBase): pass
class Product(Base):
    __tablename__ = 'product'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(Text)

def orm_query_update(session,id:int,name:str,desc:str):
    query = update(Product).where(Product.id==id).values(name=name,description =desc)
    session.execute(query)
    session.commit()
def orm_query_add(session,name:str,desc:str):

        query =select(Product).where(Product.name ==name)#атрибут большой таблицы Product(колонка)
        res1 =session.execute(query)
        res=res1.scalar()
        if res:
            return


        session.add(Product(name = name,description = desc))
        session.commit()
   
async def orm_query(session,id): 
    
    query =select(Product).where(Product.id == int(id))#атрибут большой таблицы Product(колонка)
    res1 = session.execute(query)
    res = res1.scalar()
    return res




# ======================================================================
#=======================================================================
app = Flask(__name__)
@app.route('/megasuperpuper/product/<id>',methods =['GET'])
def get_pr(id):
        with Session(engine) as session:
            pr =   orm_query(session,id=id)
        dict_query = {'products':pr.name,'description':pr.description}
        return jsonify(dict_query['products'],dict_query['description'])
    

@app.route('/megasuperpuper/productadd',methods =['POST'])
def add_pr():
    name=request.json['name']
    desc = request.json['desc']
    print('name')
    print('desc')
    otvet={'answer':'ок!'}
    with Session(engine) as session:
        orm_query_add(session=session,name=name,desc=desc)
    return jsonify(otvet['answer'])


@app.route('/megasuperpuper/productupdate',methods = ['PUT'])
def upd_pr():
    id =request.json['id']
    name=request.json['name']
    desc = request.json['desc']
    otvet={'answer':'ок!'}
    with Session(engine) as session:
        orm_query_update(session=session,name=name,desc=desc,id=id)
    return jsonify(otvet['answer'])


if __name__ == '__main__':#функция запускается только в родном файле(те если ее импортировать то запустить функцию не получится)
    async_main()
    

