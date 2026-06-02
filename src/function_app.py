import logging
import azure.functions as func

app = func.FunctionApp()

# Importar para function pincipal
from triggers.extract_categoria_produto import bp as extract_categoria_produto_bp
from triggers.extract_cliente import bp as extract_cliente_bp
from triggers.extract_entrega import bp as extract_entrega_bp
from triggers.extract_estoque import bp as extract_estoque_bp
from triggers.extract_estoque_movimentacao import bp as extract_estoque_movimentacao_bp
from triggers.extract_estoque_saldo import bp as extract_estoque_saldo_bp
from triggers.extract_pedido import bp as extract_pedido_bp
from triggers.extract_pedido_item import bp as extract_pedido_item_bp
from triggers.extract_produto import bp as extract_produto_bp
from triggers.extract_regiao import bp as extract_regiao_bp
from triggers.extract_representante import bp as extract_representante_bp
from triggers.extract_titulo_receber import bp as extract_titulo_receber_bp
from triggers.extract_transportadora import bp as extract_transportadora_bp
from triggers.poc_psycopg2 import bp as poc_psycopg2_bp
from triggers.poc_sqlalchemy import bp as poc_sqlalchemy_bp

# Registrar
app.register_functions(extract_categoria_produto_bp)
app.register_functions(extract_cliente_bp)
app.register_functions(extract_entrega_bp)
app.register_functions(extract_estoque_bp)
app.register_functions(extract_estoque_movimentacao_bp)
app.register_functions(extract_estoque_saldo_bp)
app.register_functions(extract_pedido_bp)
app.register_functions(extract_pedido_item_bp)
app.register_functions(extract_produto_bp)
app.register_functions(extract_regiao_bp)
app.register_functions(extract_representante_bp)
app.register_functions(extract_titulo_receber_bp)
app.register_functions(extract_transportadora_bp)
app.register_functions(poc_psycopg2_bp)
app.register_functions(poc_sqlalchemy_bp)