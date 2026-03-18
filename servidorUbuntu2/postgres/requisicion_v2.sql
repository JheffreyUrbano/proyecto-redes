-- =============================================
-- SUPERAMIGOS S.A.S - Sistema de Requisiciones
-- DDL v2
-- =============================================

CREATE TABLE area(
    codarea     varchar(2)   NOT NULL,
    descripcion varchar(150) NOT NULL,
    estado      boolean      NOT NULL,
    CONSTRAINT PK2 PRIMARY KEY (codarea)
);

CREATE TABLE perfil(
    codperfil   varchar(2)   NOT NULL,
    descripcion varchar(150) NOT NULL,
    estado      boolean      NOT NULL,
    CONSTRAINT PK3 PRIMARY KEY (codperfil)
);

CREATE TABLE funciones(
    codfuncion  varchar(2)   NOT NULL,
    descripcion varchar(150) NOT NULL,
    estado      boolean      NOT NULL,
    CONSTRAINT PK4 PRIMARY KEY (codfuncion)
);

CREATE TABLE estado_requi(
    codestado   varchar(2)   NOT NULL,
    descripcion varchar(150) NOT NULL,
    estado      boolean      NOT NULL,
    CONSTRAINT PK6 PRIMARY KEY (codestado)
);

CREATE TABLE usuario(
    codusuario  varchar(20)  NOT NULL,
    nombre      varchar(150) NOT NULL,
    cargo       varchar(150) NOT NULL,
    login       varchar(20)  NOT NULL,
    pass        varchar(10)  NOT NULL,
    email       varchar(255) NOT NULL,
    estado      boolean      NOT NULL,
    codperfil   varchar(2)   NOT NULL,
    CONSTRAINT PK1 PRIMARY KEY (codusuario)
);

CREATE TABLE asignacion(
    codusuario  varchar(20) NOT NULL,
    codfuncion  varchar(2)  NOT NULL,
    codarea     varchar(2)  NOT NULL,
    CONSTRAINT PK9 PRIMARY KEY (codusuario, codfuncion, codarea)
);

CREATE TABLE proveedor(
    codproveedor varchar(20)  NOT NULL,
    descripcion  varchar(150) NOT NULL,
    direccion    varchar(150) NOT NULL,
    telefono     varchar(20)  NOT NULL,
    estado       boolean      NOT NULL,
    CONSTRAINT PK7 PRIMARY KEY (codproveedor)
);

CREATE TABLE producto(
    codproducto varchar(20)  NOT NULL,
    descripcion varchar(150) NOT NULL,
    precio      float4       NOT NULL,
    cantidad    float4       NOT NULL,
    cmi         float4       NOT NULL,
    estado      boolean      NOT NULL,
    CONSTRAINT PK8 PRIMARY KEY (codproducto)
);

CREATE TABLE requisicion(
    requino      varchar(20)  NOT NULL,
    fecha        varchar(10)  NOT NULL,
    obs          varchar(254) NOT NULL,
    valor_total  float4       NOT NULL,
    codusuario   varchar(20)  NOT NULL,
    codestado    varchar(2)   NOT NULL,
    codproveedor varchar(20)  NOT NULL,
    CONSTRAINT PK5 PRIMARY KEY (requino)
);

CREATE TABLE detalle_requisicion(
    item        float4      NOT NULL,
    codproducto varchar(20) NOT NULL,
    requino     varchar(20) NOT NULL,
    cantidad    float4      NOT NULL,
    valor       float4      NOT NULL,
    CONSTRAINT PK10 PRIMARY KEY (item, codproducto, requino)
);

-- =============================================
-- TABLA DE AUDITORÍA
-- =============================================
CREATE TABLE log_requisicion(
    id                 SERIAL       PRIMARY KEY,
    requino            varchar(20)  NOT NULL,
    codusuario         varchar(20)  NOT NULL,
    accion             varchar(20)  NOT NULL,
    fecha              TIMESTAMP    NOT NULL DEFAULT NOW(),
    ip_address         varchar(45),
    user_agent         TEXT,
    codestado_anterior varchar(2),
    codestado_nuevo    varchar(2),
    observaciones      varchar(500),
    datos_modificados  JSONB
);

CREATE INDEX idx_log_requino ON log_requisicion(requino);
CREATE INDEX idx_log_usuario ON log_requisicion(codusuario);
CREATE INDEX idx_log_fecha   ON log_requisicion(fecha DESC);
CREATE INDEX idx_log_accion  ON log_requisicion(accion);

-- =============================================
-- FOREIGN KEYS
-- =============================================
ALTER TABLE usuario       ADD CONSTRAINT Refperfil5      FOREIGN KEY (codperfil)    REFERENCES perfil(codperfil);

ALTER TABLE asignacion    ADD CONSTRAINT Refusuario2      FOREIGN KEY (codusuario)   REFERENCES usuario(codusuario);
ALTER TABLE asignacion    ADD CONSTRAINT Reffunciones3    FOREIGN KEY (codfuncion)   REFERENCES funciones(codfuncion);
ALTER TABLE asignacion    ADD CONSTRAINT Refarea6         FOREIGN KEY (codarea)      REFERENCES area(codarea);

ALTER TABLE requisicion   ADD CONSTRAINT Refusuario7      FOREIGN KEY (codusuario)   REFERENCES usuario(codusuario);
ALTER TABLE requisicion   ADD CONSTRAINT Refestado_requi8 FOREIGN KEY (codestado)    REFERENCES estado_requi(codestado);
ALTER TABLE requisicion   ADD CONSTRAINT Refproveedor9    FOREIGN KEY (codproveedor) REFERENCES proveedor(codproveedor);

ALTER TABLE detalle_requisicion ADD CONSTRAINT Refproducto10   FOREIGN KEY (codproducto) REFERENCES producto(codproducto);
ALTER TABLE detalle_requisicion ADD CONSTRAINT Refrequisicion11 FOREIGN KEY (requino)    REFERENCES requisicion(requino);

ALTER TABLE log_requisicion     ADD CONSTRAINT FK_log_requi    FOREIGN KEY (requino)    REFERENCES requisicion(requino);
ALTER TABLE log_requisicion     ADD CONSTRAINT FK_log_usr      FOREIGN KEY (codusuario) REFERENCES usuario(codusuario);
ALTER TABLE log_requisicion     ADD CONSTRAINT FK_log_est_ant  FOREIGN KEY (codestado_anterior) REFERENCES estado_requi(codestado);
ALTER TABLE log_requisicion     ADD CONSTRAINT FK_log_est_nvo  FOREIGN KEY (codestado_nuevo)    REFERENCES estado_requi(codestado);

-- =============================================
-- DATOS INICIALES DE CATÁLOGOS
-- =============================================
INSERT INTO estado_requi VALUES
    ('01', 'Pendiente de Revisión',     true),
    ('02', 'Pendiente de Autorización', true),
    ('03', 'Convertida en OC',          true),
    ('04', 'Rechazada',                 true);

INSERT INTO perfil VALUES
    ('01', 'Administrador', true),
    ('02', 'Solicitante',   true),
    ('03', 'Revisor',       true),
    ('04', 'Autorizador',   true);

INSERT INTO area VALUES
    ('01', 'Administración', true),
    ('02', 'Sistemas',       true),
    ('03', 'Compras',        true),
    ('04', 'Producción',     true),
    ('05', 'Diseño',         true),
    ('06', 'Comercial',      true);
