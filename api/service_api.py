from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api, Resource, fields
from sqlalchemy import ForeignKey
from flask_cors import CORS


app = Flask(__name__)
#Conexão Postgree
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:5353@localhost:5432/projeto_ctt'
app.config['SQLALCHMEY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

app.debug = True

api = Api(app = app,
            version = 1.0,
            title = "MVP-0 CTT",
            description = "Gerenciamento de backend API")

name_space_banco_post = api.namespace('banco', description='Gerenciamento banco')
name_space_banco= api.namespace('banco', description='Gerenciamento banco')

name_space_cliente_post = api.namespace('cliente', description='Gerenciamento cliente')
name_space_cliente_put = api.namespace('cliente', description='Gerenciamento cliente')

name_space_proprietario_post = api.namespace('proprietario', description='Gerenciamento proprietario')
name_space_proprietario_put = api.namespace('proprietario', description='Gerenciamento proprietario')

name_space_despesas_post = api.namespace('despesas', description='Gerenciamento vendedor ')
name_space_despesas_put = api.namespace('despesas', description='Gerenciamento vendedor ')

name_space_imovel_post = api.namespace('imovel', description='Gerenciamento imovel')
name_space_imovel_put = api.namespace('imovel', description='Gerenciamento imovel')

name_space_compra_post = api.namespace('compra', description='Gerenciamento compra')
name_space_compra_put = api.namespace('compra', description='Gerenciamento compra')



#Model que indica o padrão JSON aceito no Swagger
model_banco_post = api.model('Modelo Banco Post',
                                {'nome': fields.String(required = True,
                                                        help="Nome do Banco")})

model_banco_put = api.model('Modelo Banco Put',
                                {'nome': fields.String(help="Nome do Banco")})

model_cliente_post = api.model('Modelo Cliente Post',
                                {'id_banco': fields.Integer(required=False,
                                                         help="ID do banco referente a tabela Banco"),
                                'nome': fields.String(required = True,
                                                        help="Nome do Cliente"),
                                'data_de_nascimento': fields.Date(required=True,
                                                         help="Data de nascimento do Cliente"),
                                'rg': fields.String(required=True,
                                                         help="RG do Cliente"),
                                'cpf': fields.String(required=True,
                                                         help="CPF do Cliente"),
                                'estado_civil': fields.String(required=True,
                                                         help="Estado civil  do Cliente"),
                                'profissao': fields.String(required=True,
                                                         help="Profissao do Cliente"),
                                'tipo_residencia': fields.String(required=True,
                                                         help="Tipo de residencia do Cliente"),
                                'cep': fields.String(required=True,
                                                         help="CEP do Cliente"),
                                'rua': fields.String(required=True,
                                                         help="Rua do Cliente"),
                                'numero': fields.String(required=True,
                                                         help="Numero do Cliente"),
                                'cidade': fields.String(required=True,
                                                         help="Cidade do Cliente"),
                                'estado': fields.String(required=True,
                                                         help="Estado do Cliente"),
                                'uf': fields.String(required=True,
                                                         help="UF do Cliente")})

model_cliente_put = api.model('Modelo Cliente Put',                        
                                {'id_banco': fields.Integer(help="ID do banco referente a tabela Banco"),
                                'nome': fields.String(help="Nome do Cliente"),
                                'data_de_nascimento': fields.Date(help="Data de nascimento do Cliente"),
                                'rg': fields.String(help="RG do cliente"),
                                'cpf': fields.String(help="CPF do cliente"),
                                'estado_civil': fields.String(help="Estado civil  do Cliente"),
                                'profissao': fields.String(help="Profissao do Cliente"),
                                'tipo_residencia': fields.String(help="Tipo de residencia do Cliente"),
                                'cep': fields.String(help="CEP do Cliente"),
                                'rua': fields.String(help="Rua do Cliente"),
                                'numero': fields.String(help="Numero do Cliente"),
                                'cidade': fields.String(help="Cidade do Cliente"),
                                'estado': fields.String(help="Estado do Cliente"),
                                'uf': fields.String(help="UF do Cliente")})

model_proprietario_post = api.model('Modelo Proprietario Post',
                                {'nome': fields.String(required = True,
                                                        help="Nome da Proprietario"),
                                'data_de_nascimento': fields.Date(required=True,
                                                         help="Data de nascimento do Proprietario"),
                                'rg': fields.String(required=True,
                                                         help="RG do Proprietario"),
                                'cpf': fields.Integer(required=True,
                                                         help="CPF do Proprietario"),
                                'estado_civil': fields.String(required=True,
                                                         help="Estado Civil do Proprietario"),
                                'profissao': fields.String(required=True,
                                                         help="Profissao Proprietario")})

model_proprietario_put = api.model('Modelo Proprietario Put',
                                {'nome': fields.String(help="Nome da Proprietario"),
                                'data_de_nascimento': fields.Date(help="Data de nascimento do Proprietario"),
                                'rg': fields.String(help="RG do Proprietario"),
                                'cpf': fields.Integer(help="CPF do Proprietario"),
                                'estado_civil': fields.String(help="Estado Civil do Proprietario"),
                                'profissao': fields.String(help="Profissao Proprietario")})

model_despesas_post = api.model('Modelo Despesas Post',
                                {'conta_luz': fields.Float(required = True,
                                                        help="Nome da Despesas"),
                                'conta_agua': fields.Float(required=True,
                                                         help="Conta de agua"),
                                'conta_condominio': fields.Float(required=True,
                                                         help="Conta de condominio"),
                                'propaganda_pre_venda': fields.Float(required=True,
                                                         help="Gastos com propraganda na pre venda")})

model_despesas_put = api.model('Modelo Despesas Put',
                                {'conta_luz': fields.Float(help="Nome da Despesas"),
                                'conta_agua': fields.Float(help="Conta de agua"),
                                'conta_condominio': fields.Float(help="Conta de condominio"),
                                'propaganda_pre_venda': fields.Float(help="Gastos com propraganda na pre venda")})

model_imovel_post = api.model('Modelo Imovel Post',
                                {'id_proprietario': fields.Integer(required=True,
                                                         help="ID do proprietario referente a tabela proprietario"),
                                'id_despesas': fields.Integer(required=True,
                                                         help="ID da despesa referente a tabela despesa"),
                                'valor': fields.Float(required = True,
                                                        help="Valor imovel"),
                                'tipo_residencia': fields.String(required=True,
                                                         help="Tipo de imovel"),
                                'cep': fields.Integer(required=True,
                                                         help="CEP do imovel"),
                                'rua': fields.String(required=True,
                                                         help="Rua do imovel"),
                                'numero': fields.String(required=True,
                                                         help="Numero do imovel"),
                                'cidade': fields.String(required=True,
                                                         help="Cidade do imovel"),
                                'estado': fields.String(required=True,
                                                         help="Estado do imovel"),
                                'uf': fields.String(required=True,
                                                         help="UF do imovel"),
                                'data_de_cadastro': fields.String(required=True,
                                                         help="Data de Cadastro do imovel")})

model_imovel_put = api.model('Modelo Imovel Put',
                                {'id_proprietario': fields.Integer(help="ID do proprietario referente a tabela proprietario"),
                                'id_despesas': fields.Integer(help="ID da despesa referente a tabela despesa"),
                                'valor': fields.Float(help="Valor imovel"),
                                'tipo_residencia': fields.String(help="Tipo de imovel"),
                                'cep': fields.Integer(help="CEP do imovel"),
                                'rua': fields.String(help="Rua do imovel"),
                                'numero': fields.String(help="Numero do imovel"),
                                'cidade': fields.String(help="Cidade do imovel"),
                                'estado': fields.String(help="Estado do imovel"),
                                'uf': fields.String(help="UF do imovel"),
                                'data_de_cadastro': fields.Date(help="Data de Cadastro do imovel")})

model_compra_post = api.model('Modelo Compra Post',
                                {'id_cliente': fields.Integer(required=True,
                                                         help="ID do cliente referente a tabela cliente"),
                                'id_imovel': fields.Integer(required=True,
                                                         help="ID do imovel referente a tabela imovel"),
                                'numero_parcelas': fields.Float(required=True,
                                                         help="Numero de parcelas da compra"),
                                'forma_pagamento': fields.String(required=True,
                                                         help="Forma de pagamento da compra"),
                                'data_aquisicao': fields.Date(required=True,
                                                         help="Data de aquisição da compra")})

model_compra_put = api.model('Modelo Compra Put',
                                {'id_cliente': fields.Integer(help="ID do cliente referente a tabela cliente"),
                                'id_imovel': fields.Integer(help="ID do imovel referente a tabela imovel"),
                                'numero_parcelas': fields.Float(help="Numero de parcelas da compra"),
                                'forma_pagamento': fields.Float(help="Forma de pagamento da compra"),
                                'data_aquisicao': fields.Date(help="Data de aquisição da compra")})


#inicialização de tabelas nas classes
class banco(db.Model):
    id_banco = db.Column(db.Integer, primary_key = True, autoincrement = True, unique=True)
    nome = db.Column(db.String)

    def __init__(self, nome):
        self.nome = nome

class cliente(db.Model):
    id_cliente = db.Column(db.Integer, primary_key = True, autoincrement = True, unique=True)
    id_banco = db.Column(db.Integer, ForeignKey('banco.id_banco'))
    nome = db.Column(db.String)
    data_de_nascimento = db.Column(db.Date)
    rg = db.Column(db.String)
    cpf = db.Column(db.String)
    estado_civil = db.Column(db.String)
    profissao = db.Column(db.String)
    tipo_residencia = db.Column(db.String)
    cep = db.Column(db.String)
    rua = db.Column(db.String)
    numero = db.Column(db.String)
    cidade = db.Column(db.String)
    estado = db.Column(db.String)
    uf = db.Column(db.String)
    

    def __init__(self,id_banco, nome, data_de_nascimento, rg, cpf, estado_civil, profissao, tipo_residencia, cep, rua, numero, cidade, estado, uf):
        self.id_banco = id_banco
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.rg = rg
        self.cpf = cpf
        self.estado_civil = estado_civil
        self.profissao = profissao
        self.tipo_residencia = tipo_residencia
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        self.uf = uf
        
class proprietario(db.Model):
    id_proprietario = db.Column(db.Integer, primary_key = True, autoincrement = True, unique=True)
    nome = db.Column(db.String)
    data_de_nascimento = db.Column(db.Date)
    rg = db.Column(db.String)
    cpf = db.Column(db.String)
    estado_civil = db.Column(db.String)
    profissao = db.Column(db.String)
    
    def __init__(self, nome, data_de_nascimento, rg, cpf, estado_civil, profissao):
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.rg = rg
        self.cpf = cpf
        self.estado_civil = estado_civil
        self.profissao = profissao

class despesas(db.Model):
    id_despesas = db.Column(db.Integer, primary_key = True, autoincrement = True, unique=True)
    conta_luz = db.Column(db.Float)
    conta_agua = db.Column(db.Float)
    conta_condominio = db.Column(db.Float)
    propaganda_pre_venda = db.Column(db.Float)
    
    def __init__(self, conta_luz, conta_agua, conta_condominio, propaganda_pre_venda):
        self.conta_luz = conta_luz
        self.conta_agua = conta_agua
        self.conta_condominio = conta_condominio
        self.propaganda_pre_venda = propaganda_pre_venda
    
class imovel(db.Model):
    id_imovel = db.Column(db.Integer, primary_key = True, autoincrement = True, unique=True)
    id_proprietario = db.Column(db.Integer, ForeignKey('proprietario.id_proprietario'))
    id_despesas = db.Column(db.Integer, ForeignKey('despesas.id_despesas'))
    valor = db.Column(db.Float)
    tipo_residencia = db.Column(db.String)
    cep = db.Column(db.String)
    rua = db.Column(db.String)
    numero = db.Column(db.String)
    cidade = db.Column(db.String)
    estado = db.Column(db.String)
    uf = db.Column(db.String)
    data_de_cadastro = db.Column(db.Date)

    
    def __init__(self, id_proprietario, id_despesas, valor, tipo_residencia, cep, rua, numero, cidade, estado, uf, data_de_cadastro):
        self.id_proprietario = id_proprietario
        self.id_despesas = id_despesas
        self.valor = valor
        self.tipo_residencia = tipo_residencia
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        self.uf = uf
        self.data_de_cadastro = data_de_cadastro

class compra(db.Model):
    id_compra = db.Column(db.Integer, primary_key = True, autoincrement = True, unique=True)
    id_cliente = db.Column(db.Integer, ForeignKey('cliente.id_cliente'))
    id_imovel = db.Column(db.Integer, ForeignKey('imovel.id_imovel'))
    forma_pagamento = db.Column(db.String)
    numero_parcelas = db.Column(db.Integer)
    data_aquisicao = db.Column(db.Date)
    
    def __init__(self, id_cliente, id_imovel, forma_pagamento, numero_parcelas, data_aquisicao):
        self.id_cliente = id_cliente
        self.id_imovel = id_imovel
        self.forma_pagamento = forma_pagamento
        self.numero_parcelas = numero_parcelas
        self.data_aquisicao = data_aquisicao


#Namespace exige um id para get e delete
@name_space_banco.route("/banco")
class MainClassBanco(Resource):
        def get(self):    
                try:
                        
                                all_bancos = banco.query.all()
                                output = []
                                for bank in all_bancos:
                                    cur_banco = {}                            
                                    cur_banco['id_banco'] = bank.id_banco
                                    cur_banco['nome'] = bank.nome
                                    output.append(cur_banco)
                                return jsonify(output)
                except KeyError as e:
                    name_space_banco.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
                except Exception as e:
                    name_space_banco.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

        @api.expect(model_banco_post)
        def post(self):
                try:
                        banco_db = request.get_json()
                        new_banco = banco(
                            nome=banco_db['nome'])
                            

                        db.session.add(new_banco)
                        db.session.commit()
                        return jsonify(banco_db)
                except KeyError as e:
                    name_space_banco.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
                except Exception as e:
                    name_space_banco.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")
        


@name_space_banco.route("/banco/<int:id>")
class MainClassBanco(Resource):
        def get(self, id):    
                try:
                        
                                all_bancos = banco.query.filter(banco.id_banco==id)
                                output = []
                                for bank in all_bancos:
                                    cur_banco = {}                            
                                    cur_banco['id_banco'] = bank.id_banco
                                    cur_banco['nome'] = bank.nome
                                    output.append(cur_banco)
                                return jsonify(output)
                except KeyError as e:
                    name_space_banco.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
                except Exception as e:
                    name_space_banco.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

        
        def delete(self, id):
                try:
                        banco_data = banco.query.filter(banco.id_banco==id).delete()
                        db.session.commit()
                        return jsonify(banco_data)

                except KeyError as e:
                    name_space_banco.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
                except Exception as e:
                    name_space_banco.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")
        
        @api.expect(model_banco_put)
        def put(self, id):
                try:    

                        banco_put =  banco.query.get(id)
                        banco_put.id_banco = request.json.get('id_banco', banco_put.id_banco)
                        banco_put.nome = request.json.get('nome', banco_put.nome)
                        
                        db.session.commit()

                        return jsonify({'nome': banco_put.nome})
                except KeyError as e:
                    name_space_banco.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
                except Exception as e:
                    name_space_banco.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")


       




@name_space_cliente_put.route("/cliente/<int:id>")
class MainClassClientes(Resource):
        def get(self, id):
                try:
                        all_cliente = cliente.query.filter(cliente.id_cliente==id)
                        output = []
                        for clientes in all_cliente:
                            cur_cliente = {}
                            cur_cliente['id_cliente'] = clientes.id_cliente
                            cur_cliente['id_banco'] = clientes.id_banco
                            cur_cliente['nome'] = clientes.nome
                            cur_cliente['data_de_nascimento'] = clientes.data_de_nascimento
                            cur_cliente['rg'] = clientes.rg
                            cur_cliente['cpf'] = clientes.cpf
                            cur_cliente['estado_civil'] = clientes.estado_civil
                            cur_cliente['profissao'] = clientes.profissao
                            cur_cliente['tipo_residencia'] = clientes.tipo_residencia
                            cur_cliente['cep'] = clientes.cep
                            cur_cliente['rua'] = clientes.rua
                            cur_cliente['numero'] = clientes.numero
                            cur_cliente['cidade'] = clientes.cidade
                            cur_cliente['estado'] = clientes.estado
                            cur_cliente['uf'] = clientes.uf
                            output.append(cur_cliente)
                        return jsonify(output)
                except KeyError as e:
                    name_space_cliente_put.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
                except Exception as e:
                    name_space_cliente_put.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

        def delete(self, id):
                try:
                        cliente_data = cliente.query.filter(cliente.id_cliente==id).delete()
                        db.session.commit()
                        return jsonify(cliente_data)

                except KeyError as e:
                    name_space_cliente_put.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
                except Exception as e:
                    name_space_cliente_put.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

        @api.expect(model_cliente_put)
        def put(self, id):
                try:
                        cliente_put =  cliente.query.get(id)
                        cliente_put.id_banco = request.json.get('id_banco', cliente_put.id_banco)
                        cliente_put.nome = request.json.get('nome', cliente_put.nome)
                        cliente_put.data_de_nascimento = request.json.get('data_de_nascimento', cliente_put.data_de_nascimento)
                        cliente_put.rg = request.json.get('rg', cliente_put.rg)
                        cliente_put.cpf = request.json.get('cpf', cliente_put.cpf)
                        cliente_put.estado_civil = request.json.get('estado_civil', cliente_put.estado_civil)
                        cliente_put.profissao = request.json.get('profissao', cliente_put.profissao)
                        cliente_put.tipo_residencia = request.json.get('tipo_residencia', cliente_put.tipo_residencia)
                        cliente_put.cep = request.json.get('cep', cliente_put.cep)
                        cliente_put.rua = request.json.get('rua', cliente_put.rua)
                        cliente_put.cidade = request.json.get('cidade', cliente_put.cidade)
                        cliente_put.estado = request.json.get('estado', cliente_put.estado)
                        cliente_put.uf = request.json.get('uf', cliente_put.uf)

                        db.session.commit()

                        return jsonify({'nome': cliente_put.nome})
                except KeyError as e:
                    name_space_cliente_put.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
                except Exception as e:
                    name_space_cliente_put.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

#namespace não necessita post não necessita de id para funcionamento
@name_space_cliente_post.route("/clientes")
class MainClassClientes(Resource):
        def get(self):
            try:
                    all_cliente = cliente.query.all()
                    output = []
                    for clientes in all_cliente:
                        cur_cliente = {}
                        cur_cliente['id_cliente'] = clientes.id_cliente
                        cur_cliente['id_banco'] = clientes.id_banco
                        cur_cliente['nome'] = clientes.nome
                        cur_cliente['data_de_nascimento'] = clientes.data_de_nascimento
                        cur_cliente['rg'] = clientes.rg
                        cur_cliente['cpf'] = clientes.cpf
                        cur_cliente['estado_civil'] = clientes.estado_civil
                        cur_cliente['profissao'] = clientes.profissao
                        cur_cliente['tipo_residencia'] = clientes.tipo_residencia
                        cur_cliente['cep'] = clientes.cep
                        cur_cliente['rua'] = clientes.rua
                        cur_cliente['numero'] = clientes.numero
                        cur_cliente['cidade'] = clientes.cidade
                        cur_cliente['estado'] = clientes.estado
                        cur_cliente['uf'] = clientes.uf
                        output.append(cur_cliente)
                    return jsonify(output)
            except KeyError as e:
                name_space_cliente_put.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
            except Exception as e:
                name_space_cliente_put.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")
        @api.expect(model_cliente_post)
        def post(self):
                try:
                        cliente_db = request.get_json()
                        new_cliente = cliente(
                            id_banco=cliente_db['id_banco'],
                            nome=cliente_db['nome'],
                            data_de_nascimento=cliente_db['data_de_nascimento'], 
                            rg=cliente_db['rg'], 
                            cpf=cliente_db['cpf'], 
                            estado_civil=cliente_db['estado_civil'], 
                            profissao=cliente_db['profissao'], 
                            tipo_residencia=cliente_db['tipo_residencia'], 
                            cep=cliente_db['cep'],
                            rua=cliente_db['rua'], 
                            numero=cliente_db['numero'], 
                            cidade=cliente_db['cidade'],
                            estado=cliente_db['estado'], 
                            uf=cliente_db['uf'])

                        db.session.add(new_cliente)
                        db.session.commit()
                        return jsonify(cliente_db)
                except KeyError as e:
                    name_space_cliente_put.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
                except Exception as e:
                    name_space_cliente_put.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")
            
      

@name_space_proprietario_put.route("/proprietario/<int:id>")
class MainClassProprietario(Resource):
        def get(self, id):
                try:
                        all_proprietario = proprietario.query.filter(proprietario.id_proprietario==id)
                        output = []
                        for proprietarios in all_proprietario:
                            cur_proprietarios= {}
                            cur_proprietarios['id_proprietario'] = proprietarios.id_proprietario
                            cur_proprietarios['nome'] = proprietarios.nome
                            cur_proprietarios['data_de_nascimento'] = proprietarios.data_de_nascimento
                            cur_proprietarios['rg'] = proprietarios.rg
                            cur_proprietarios['cpf'] = proprietarios.cpf
                            cur_proprietarios['estado_civil'] = proprietarios.estado_civil
                            cur_proprietarios['profissao'] = proprietarios.profissao
                            output.append(cur_proprietarios)
                        return jsonify(output)
                except KeyError as e:
                    name_space_proprietario_put.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
                except Exception as e:
                    name_space_proprietario_put.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

        def delete(self, id):
                try:
                        proprietario_data = proprietario.query.filter(proprietario.id_proprietario==id).delete()
                        db.session.commit()
                        return jsonify(proprietario_data)

                except KeyError as e:
                    name_space_proprietario_put.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
                except Exception as e:
                    name_space_proprietario_put.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

        @api.expect(model_proprietario_put)
        def put(self, id):
                try:
                        proprietario_put =  proprietario.query.get(id)
                        proprietario_put.nome = request.json.get('nome', proprietario_put.nome)
                        proprietario_put.data_de_nascimento = request.json.get('data_de_nascimento', proprietario_put.data_de_nascimento)
                        proprietario_put.rg = request.json.get('rg', proprietario_put.rg)
                        proprietario_put.cpf = request.json.get('cpf', proprietario_put.cpf)
                        proprietario_put.estado_civil = request.json.get('estado_civil', proprietario_put.estado_civil)
                        proprietario_put.profissao = request.json.get('profissao', proprietario_put.profissao)

                        db.session.commit()

                        return jsonify({'nome': proprietario_put.nome})
                except KeyError as e:
                    name_space_proprietario_put.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
                except Exception as e:
                    name_space_proprietario_put.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

@name_space_proprietario_post.route("/proprietario")
class MainClassProprietario(Resource):
        def get(self):
                try:
                        all_proprietario = proprietario.query.all()
                        output = []
                        for proprietarios in all_proprietario:
                            cur_proprietarios= {}
                            cur_proprietarios['id_proprietario'] = proprietarios.id_proprietario
                            cur_proprietarios['nome'] = proprietarios.nome
                            cur_proprietarios['data_de_nascimento'] = proprietarios.data_de_nascimento
                            cur_proprietarios['rg'] = proprietarios.rg
                            cur_proprietarios['cpf'] = proprietarios.cpf
                            cur_proprietarios['estado_civil'] = proprietarios.estado_civil
                            cur_proprietarios['profissao'] = proprietarios.profissao
                            output.append(cur_proprietarios)
                        return jsonify(output)
                except KeyError as e:
                    name_space_proprietario_put.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
                except Exception as e:
                    name_space_proprietario_put.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

        @api.expect(model_proprietario_post)
        def post(self):
                try:
                        proprietario_db = request.get_json()
                        new_proprietario = proprietario(
                            nome=proprietario_db['nome'],
                            data_de_nascimento=proprietario_db['data_de_nascimento'], 
                            rg=proprietario_db['rg'], 
                            cpf=proprietario_db['cpf'], 
                            estado_civil=proprietario_db['estado_civil'], 
                            profissao=proprietario_db['profissao'])

                        db.session.add(new_proprietario)
                        db.session.commit()
                        return jsonify(proprietario_db)
                except KeyError as e:
                    name_space_proprietario_post.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
                except Exception as e:
                    name_space_proprietario_post.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

@name_space_despesas_put.route("/despesas")
class MainClassDespesas(Resource):
        def get(self):
                try:
                        all_despesas = despesas.query.all()
                        output = []
                        for despesa in all_despesas:
                            cur_despesa= {}
                            cur_despesa['id_despesas'] = despesa.id_despesas
                            cur_despesa['conta_luz'] = despesa.conta_luz
                            cur_despesa['conta_agua'] = despesa.conta_agua
                            cur_despesa['conta_condominio'] = despesa.conta_condominio
                            cur_despesa['propaganda_pre_venda'] = despesa.propaganda_pre_venda
                            output.append(cur_despesa)
                        return jsonify(output)
                except KeyError as e:
                    name_space_despesas_put.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
                except Exception as e:
                    name_space_despesas_put.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")
        
        @api.expect(model_despesas_post)
        def post(self):
                        despesas_db = request.get_json()
                        new_despesas = despesas(
                            conta_luz=despesas_db['conta_luz'],
                            conta_agua=despesas_db['conta_agua'], 
                            conta_condominio=despesas_db['conta_condominio'], 
                            propaganda_pre_venda=despesas_db['propaganda_pre_venda'])

                        db.session.add(new_despesas)
                        db.session.commit()
                        return jsonify(despesas_db)

@name_space_despesas_put.route("/despesas/<int:id>")
class MainClassDespesas(Resource):
        def get(self, id):
                try:
                        all_despesas = despesas.query.filter(despesas.id_despesas==id)
                        output = []
                        for despesa in all_despesas:
                            cur_despesa= {}
                            cur_despesa['id_proprietario'] = despesa.id_despesas
                            cur_despesa['conta_luz'] = despesa.conta_luz
                            cur_despesa['conta_agua'] = despesa.conta_agua
                            cur_despesa['conta_condominio'] = despesa.conta_condominio
                            cur_despesa['propaganda_pre_venda'] = despesa.propaganda_pre_venda
                            output.append(cur_despesa)
                        return jsonify(output)
                except KeyError as e:
                    name_space_despesas_put.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
                except Exception as e:
                    name_space_despesas_put.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

        def delete(self, id):
                try:
                        despesas_data = despesas.query.filter(despesas.id_despesas==id).delete()
                        db.session.commit()
                        return jsonify(despesas_data)

                except KeyError as e:
                    name_space_despesas_put.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
                except Exception as e:
                    name_space_despesas_put.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

        @api.expect(model_despesas_put)
        def put(self, id):
                try:
                        despesas_put =  despesas.query.get(id)
                        despesas_put.conta_luz = request.json.get('conta_luz', despesas_put.conta_luz)
                        despesas_put.conta_agua = request.json.get('conta_agua', despesas_put.conta_agua)
                        despesas_put.conta_condominio = request.json.get('conta_condominio', despesas_put.conta_condominio)
                        despesas_put.propaganda_pre_venda = request.json.get('propaganda_pre_venda', despesas_put.propaganda_pre_venda)
                        db.session.commit()

                        return jsonify({'conta_luz': despesas_put.conta_luz,
                                        'conta_agua': despesas_put.conta_agua,
                                        'conta_condominio': despesas_put.conta_condominio,
                                        'propaganda_pre_venda': despesas_put.propaganda_pre_venda,})
                except KeyError as e:
                    name_space_despesas_put.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
                except Exception as e:
                    name_space_despesas_put.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

@name_space_imovel_post.route("/imovel")
class MainClassImovel(Resource):

        def get(self):
                        all_imovel = imovel.query.all()
                        output = []
                        for imovels in all_imovel:
                            cur_imovel= {}
                            cur_imovel['id_proprietario'] = imovels.id_proprietario
                            cur_imovel['id_despesas'] = imovels.id_despesas
                            cur_imovel['valor'] = imovels.valor
                            cur_imovel['tipo_residencia'] = imovels.tipo_residencia
                            cur_imovel['cep'] = imovels.cep
                            cur_imovel['rua'] = imovels.rua
                            cur_imovel['numero'] = imovels.numero
                            cur_imovel['cidade'] = imovels.cidade
                            cur_imovel['estado'] = imovels.estado
                            cur_imovel['uf'] = imovels.uf
                            cur_imovel['data_de_cadastro'] = imovels.data_de_cadastro
                            output.append(cur_imovel)
                        return jsonify(output)

        @api.expect(model_imovel_post)
        def post(self):
                        imovel_db = request.get_json()
                        new_imovel = imovel(
                            id_proprietario=imovel_db['id_proprietario'],
                            id_despesas=imovel_db['id_despesas'], 
                            valor=imovel_db['valor'], 
                            tipo_residencia=imovel_db['tipo_residencia'],
                            cep=imovel_db['cep'],
                            rua=imovel_db['rua'], 
                            numero=imovel_db['numero'], 
                            cidade=imovel_db['cidade'],
                            estado=imovel_db['estado'], 
                            uf=imovel_db['uf'], 
                            data_de_cadastro=imovel_db['data_de_cadastro'])

                        db.session.add(new_imovel)
                        db.session.commit()
                        return jsonify(imovel_db)


@name_space_imovel_put.route("/imovel/<int:id>")
class MainClassImovel(Resource):
        def get(self, id):
                        all_imovel = imovel.query.filter(imovel.id_imovel==id)
                        output = []
                        for imovels in all_imovel:
                            cur_imovel= {}
                            cur_imovel['id_proprietario'] = imovels.id_imovel
                            cur_imovel['id_despesas'] = imovels.id_despesas
                            cur_imovel['valor'] = imovels.valor
                            cur_imovel['tipo_residencia'] = imovels.tipo_residencia
                            cur_imovel['cep'] = imovels.cep
                            cur_imovel['rua'] = imovels.rua
                            cur_imovel['numero'] = imovels.numero
                            cur_imovel['cidade'] = imovels.cidade
                            cur_imovel['estado'] = imovels.estado
                            cur_imovel['uf'] = imovels.uf
                            cur_imovel['data_de_cadastro'] = imovels.data_de_cadastro
                            output.append(cur_imovel)
                        return jsonify(output)


        def delete(self, id):
                try:
                        imovel_data = imovel.query.filter(imovel.id_imovel==id).delete()
                        db.session.commit()
                        return jsonify(imovel_data)

                except KeyError as e:
                    name_space_imovel_put.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
                except Exception as e:
                    name_space_imovel_put.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

        @api.expect(model_imovel_put)
        def put(self, id):
                try:
                        imovel_put =  imovel.query.get(id)
                        imovel_put.id_proprietario = request.json.get('id_proprietario', imovel_put.id_proprietario)
                        imovel_put.id_despesas = request.json.get('id_despesas', imovel_put.id_despesas)
                        imovel_put.valor = request.json.get('valor', imovel_put.valor)
                        imovel_put.tipo_residencia = request.json.get('tipo_residencia', imovel_put.tipo_residencia)
                        imovel_put.cep = request.json.get('cep', imovel_put.cep)
                        imovel_put.rua = request.json.get('rua', imovel_put.rua)
                        imovel_put.numero = request.json.get('numero', imovel_put.numero)
                        imovel_put.cidade = request.json.get('cidade', imovel_put.cidade)
                        imovel_put.estado = request.json.get('estado', imovel_put.estado)
                        imovel_put.uf = request.json.get('uf', imovel_put.uf)
                        imovel_put.data_de_cadastro = request.json.get('data_de_cadastro', imovel_put.data_de_cadastro)
                        db.session.commit()

                        return jsonify({'id_proprietario': imovel_put.id_proprietario,
                                        'id_despesas': imovel_put.id_despesas,
                                        'valor': imovel_put.valor,
                                        'tipo_residencia': imovel_put.tipo_residencia,
                                        'cep': imovel_put.cep,
                                        'rua': imovel_put.rua,
                                        'numero': imovel_put.numero,
                                        'cidade': imovel_put.cidade,
                                        'estado': imovel_put.estado,
                                        'uf': imovel_put.uf,
                                        'data_de_cadastro': imovel_put.data_de_cadastro})
                except KeyError as e:
                    name_space_imovel_put.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
                except Exception as e:
                    name_space_imovel_post.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "400")

@name_space_compra_put.route("/compra/<int:id>")
class MainClassDespesas(Resource):
        def get(self, id):
                try:
                        all_compra = compra.query.filter(compra.id_compra==id)
                        output = []
                        for compras in all_compra:
                            cur_compra= {}
                            cur_compra['id_cliente'] = compras.id_cliente
                            cur_compra['id_imovel'] = compras.id_imovel
                            cur_compra['forma_pagamento'] = compras.forma_pagamento
                            cur_compra['numero_parcelas'] = compras.numero_parcelas
                            cur_compra['data_aquisicao'] = compras.data_aquisicao
                            output.append(cur_compra)
                        return jsonify(output)
                except KeyError as e:
                    name_space_compra_put.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
                except Exception as e:
                    name_space_compra_put.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")
        
        def delete(self, id):
                try:
                        compra_data = compra.query.filter(compra.id_compra==id).delete()
                        db.session.commit()
                        return jsonify(compra_data)

                except KeyError as e:
                    name_space_compra_put.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
                except Exception as e:
                    name_space_compra_put.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

        @api.expect(model_compra_put)
        def put(self, id):
                try:
                        compra_put =  compra.query.get(id)
                        compra_put.id_cliente = request.json.get('id_cliente', compra_put.id_cliente)
                        compra_put.id_imovel = request.json.get('id_imovel', compra_put.id_imovel)
                        compra_put.forma_pagamento = request.json.get('forma_pagamento', compra_put.forma_pagamento)
                        compra_put.numero_parcelas = request.json.get('numero_parcelas', compra_put.numero_parcelas)
                        compra_put.data_aquisicao = request.json.get('data_aquisicao', compra_put.data_aquisicao)
                        db.session.commit()

                        return jsonify({'id_cliente': compra_put.id_cliente,
                                        'id_imovel': compra_put.id_imovel,
                                        'forma_pagamento': compra_put.forma_pagamento,
                                        'numero_parcelas': compra_put.numero_parcelas,
                                        'data_aquisicao': compra_put.data_aquisicao})
                except KeyError as e:
                    name_space_compra_put.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
                except Exception as e:
                    name_space_compra_put.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

@name_space_compra_post.route("/compra")
class MainClassCompra(Resource):
        def get(self):
                try:
                        all_compra = compra.query.all()
                        output = []
                        for compras in all_compra:
                            cur_compra= {}
                            cur_compra['id_cliente'] = compras.id_cliente
                            cur_compra['id_imovel'] = compras.id_imovel
                            cur_compra['forma_pagamento'] = compras.forma_pagamento
                            cur_compra['numero_parcelas'] = compras.numero_parcelas
                            cur_compra['data_aquisicao'] = compras.data_aquisicao
                            output.append(cur_compra)
                        return jsonify(output)
                except KeyError as e:
                    name_space_compra_put.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
                except Exception as e:
                    name_space_compra_put.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

        @api.expect(model_compra_post)
        def post(self):
                        compra_db = request.get_json()
                        new_compra = compra(
                            id_cliente=compra_db['id_cliente'],
                            id_imovel=compra_db['id_imovel'], 
                            forma_pagamento=compra_db['forma_pagamento'], 
                            numero_parcelas=compra_db['numero_parcelas'],
                            data_aquisicao=compra_db['data_aquisicao'])

                        db.session.add(new_compra)
                        db.session.commit()
                        return jsonify(compra_db)