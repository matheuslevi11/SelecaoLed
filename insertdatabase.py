import mysql.connector
import pandas
from mysql.connector import Error

dataset = pd.read_csv("vacina.csv", sep=';')

# Tratamento de problemas com a base de dados
dataset = dataset.drop('id_sistema_origem',axis =1)
dataset.dropna(inplace=True)


try:
  con = mysql.connector.connect(host='localhost', database='dados_vacina', port='3306',user='root',password='root', auth_plugin='mysql_native_password')
  cursor = con.cursor()

  for index, row in dataset.iterrows():
    # Categorias
    query = f"INSERT INTO Categorias (codigo, nome) VALUES ({row['vacina_categoria_codigo']},{row['vacina_categoria_nome']})"
    cursor.execute(query)
    con.commit()

    # Raças
    query = f"INSERT INTO Racas (codigo, nome) VALUES ({row['paciente_racacor_codigo']},{row['paciente_racacor_valor']})"
    cursor.execute(query)
    con.commit()

    # Países
    query = f"INSERT INTO Paises (codigo, nome) VALUES ({row['paciente_endereco_copais']},{row['paciente_endereco_nmpais']})"
    cursor.execute(query)
    con.commit()

    # Grupo Atendimento
    query = f"INSERT INTO Grupo_atendimento (codigo, nome) VALUES ({row['vacina_grupoatendimento_codigo']},{row['vacina_grupoatendimento_nome']})"
    cursor.execute(query)
    con.commit()
    
    #Municipios
    query = f"INSERT INTO Municipios (codigo, nome, uf) VALUES ({row['paciente_endereco_coibgemunicipio']},{row['paciente_endereco_nmmunicipio']}, {row['paciente_endereco_uf']})"
    cursor.execute(query)
    con.commit()

    # Estabelecimentos
    query = f"INSERT INTO Estabelecimentos (codigo, razao_social, nome_fantasia, cod_mun, mun_nome, uf) VALUES ({row['estabelecimento_valor']},{row['estabelecimento_razaosocial']},{row['estalecimento_nofantasia']},{row['estabelecimento_municipio_codigo']},{row['estabelecimento_municipio_nome']},{row['estabelecimento_uf']})"
    cursor.execute(query)
    con.commit()

    # Vacinas
    query = f"INSERT INTO Vacinas (codigo, nome, lote, fabricante_nome, fabricante_referencia, data_aplicacao, dose, sistema_origem, data_importacao, categoria_id) VALUES ({row['vacina_codigo']},{row['vacina_nome']},{row['vacina_lote']},{row['vacina_fabricante_nome']},{row['vacina_fabricante_referencia']},{row['vacina_fabricante_dataaplicacao']},{row['vacina_descricao_dose']}, {row['sistema_origem']}, {row['data_importacao_rnds']}, {row['vacina_categoria_codigo']})"
    cursor.execute(query)
    con.commit()

    # Pacientes
    query = f"INSERT INTO Pacientes (document_id, paciente_id, idade, paciente_datanascimento, sexo, cep, nacionalidade, pais_id, municipio_id, raca_id, estabelecimento_id, grupo_id, vacina_id) VALUES ({row['document_id']},{row['paciente_id']},{row['paciente_idade']},{row['paciente_datanascimento']},{row['paciente_enumsexobiologico']},{row['paciente_endereco_cep']},{row['paciente_nacionalidade_enumnacionalidade']}, {row['paciente_endereco_copais']}, {row['paciente_endereco_coibgemunicipio']}, {row['paciente_racacor_codigo']}, {row['estabelecimento_valor']}, {row['vacina_grupoatendimento_codigo']}, {row['vacina_codigo']})"
    cursor.execute(query)
    con.commit()

  cursor.close()
except Error as error:
  print(f'Falha! {error}')
