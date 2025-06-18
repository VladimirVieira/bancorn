CREATE TYPE tipo_conta AS ENUM ('corrente', 'poupanca', 'bonus');

CREATE TABLE contas (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    numero VARCHAR(20) NOT NULL UNIQUE,
    saldo NUMERIC(15, 2) DEFAULT 0.00 NOT NULL,
    tipo tipo_conta DEFAULT 'corrente' NOT NULL,
    agencia_id UUID NOT NULL REFERENCES agencia_bancaria(id),
);
