CREATE SCHEMA dados_vacina;

USE dados_vacina;

create table Categorias (
	codigo INT PRIMARY KEY,
    nome VARCHAR(255)
);

create table Racas (
	codigo INT PRIMARY KEY,
    nome VARCHAR(255)
);

create table Paises (
	codigo INT PRIMARY KEY,
    nome VARCHAR(255)
);

create table Grupo_atendimento (
	codigo INT PRIMARY KEY,
    nome VARCHAR(255)
);

create table Municipios (
	codigo INT PRIMARY KEY,
    nome VARCHAR(255),
    uf VARCHAR(3)
);

create table Estabelecimentos (
	codigo INT PRIMARY KEY,
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    cod_mun INT,
    mun_nome VARCHAR(255),
    uf VARCHAR(3)
);

create table Vacinas (
	codigo INT,
    nome VARCHAR(255),
    lote VARCHAR(255),
    fabricante_nome VARCHAR(255),
    fabricante_referencia VARCHAR(255),
    data_aplicacao DATE,
    dose VARCHAR(50),
    sistema_origem VARCHAR(255),
    data_importacao VARCHAR(255),
    categoria_id INT
);

create table Pacientes (
	document_id VARCHAR(255),
    paciente_id VARCHAR(255),
    idade INT,
    paciente_datanascimento DATE,
    sexo ENUM('M', 'F'),
    cep VARCHAR(7),
    nacionalidade VARCHAR(3),
    pais_id INT,
    municipio_id INT,
    raca_id INT,
    estabelecimento_id INT,
    grupo_id INT,
    vacina_id VARCHAR(255)
);

ALTER TABLE Vacinas
ADD CONSTRAINT fk_categoriavacina FOREIGN KEY (categoria_id)
REFERENCES Categorias (codigo);

ALTER TABLE Pacientes
ADD CONSTRAINT fk_paispaciente FOREIGN KEY (pais_id)
REFERENCES Paises (codigo);

ALTER TABLE Pacientes
ADD CONSTRAINT fk_municipiopaciente FOREIGN KEY (municipio_id)
REFERENCES Municipios (codigo);

ALTER TABLE Pacientes
ADD CONSTRAINT fk_racacorpaciente FOREIGN KEY (raca_id)
REFERENCES Racas (codigo);

ALTER TABLE Pacientes
ADD CONSTRAINT fk_estabelecimentovacina FOREIGN KEY (estabelecimento_id)
REFERENCES Estabelecimentos (codigo);

ALTER TABLE Pacientes
ADD CONSTRAINT fk_grupopaciente FOREIGN KEY (grupo_id)
REFERENCES Grupo_atendimento (codigo);
