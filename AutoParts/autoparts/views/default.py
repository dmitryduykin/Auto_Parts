#-*- coding: utf-8 -*-
from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError
from pyramid.httpexceptions import HTTPFound 
from pyramid.security import Allow, forget, remember
from ..models.mymodel import *

#-----------------------------------------------регистрация----------------------------------------------
@view_config(route_name='registration', renderer='../templates/registration.jinja2')
def registration_view(request):
	DBSession = Session(bind=engine)
	try:
		new_user=Client(email=request.params['mail'],login=request.params['login'],password=request.params['password'])
		DBSession.add(new_user)
		DBSession.commit()
		return HTTPFound(location='../lobby')
	except:return{}


#-------------------------------------------------авторизация--------------------------------------------
@view_config(route_name='loginin', renderer='../templates/loginin.jinja2', request_method='POST')
def loginin_view(request):
	DBSession = Session(bind=engine)
	result = DBSession.query(Client).filter(Client.password==request.params['password'],Client.login==request.params['login']).first()
	if result!=None :		
		headers = remember(request, )
		return HTTPFound(location='../lobby',headers = headers)
	else:
		return HTTPFound(location='../loginin')
	
@view_config(route_name='loginin', renderer='../templates/loginin.jinja2', request_method='GET')
def loginin2_view(request):
	return{}

#---------------------------------------lobby----------------------------------------------------------	
@view_config(route_name='lobby', renderer='../templates/lobby.jinja2', request_method='GET')
def lobby_view(request):
	DBSession = Session(bind=engine)
	user=DBSession.query(Client).filter(Client.login == 'kekovich').first()
	return{'user':user}

@view_config(route_name='lobby', renderer='../templates/lobby.jinja2', request_method='POST')
def lobby2_view(request):
	return{}

#---------------------------------------warehouse------------------------------------------------------	
@view_config(route_name='warehouse', renderer='../templates/warehouse.jinja2',request_method='GET')
def warehouse_view(request):
	DBSession = Session(bind=engine)
	models=DBSession.query(CarModel).all()
	bodies=DBSession.query(Body).all()
	types=DBSession.query(PartType).all()
	part=DBSession.query(Part).all()	
	return{'model':models,'body':bodies,'type':types,'parts':part,"allpart":[]}

@view_config(route_name='warehouse', renderer='../templates/warehouse.jinja2',request_method='POST')
def warehouse2_view(request):
	DBSession = Session(bind=engine)
	allparts=DBSession.query(Part).all()
	result=[]
	for part in allparts:
		parttype=DBSession.query(PartType).filter(part.type_id==PartType.id).first()
		model=DBSession.query(CarModel).filter(part.model_id==CarModel.id).first()
		man=DBSession.query(Manufacturer).filter(part.manufacturer_id==Manufacturer.id).first()
		body=DBSession.query(Body).filter(part.type_id==Body.id).first()
		p={"part":part,"type":parttype, "man":man,"body":body,"model":model}
		result.append(p)
	DBSession = Session(bind=engine)
	models=DBSession.query(CarModel).all()
	bodies=DBSession.query(Body).all()
	types=DBSession.query(PartType).all()
	part=DBSession.query(Part).all()	
	return{'model':models,'body':bodies,'type':types,'parts':part,"allpart":result}
		


#---------------------------------------непонятная хрень-----------------------------------------------	
db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_AutoParts_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
