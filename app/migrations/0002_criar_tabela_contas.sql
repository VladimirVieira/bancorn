CREATE TYPE tipo_conta AS ENUM ('corrente', 'poupanca', 'bonus');

CREATE TABLE contas (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    numero VARCHAR(12) NOT NULL UNIQUE,
    saldo NUMERIC(15, 2) DEFAULT 0.00 NOT NULL,
    tipo tipo_conta DEFAULT 'corrente' NOT NULL,
    pontos INTEGER DEFAULT 0 NOT NULL CHECK (pontos >= 0),
    agencia_id UUID NOT NULL REFERENCES agencia_bancaria(id),
);
