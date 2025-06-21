CREATE TYPE tipo_operacao AS ENUM ('deposito', 'saque', 'transferencia', 'consulta_saldo', 'rendimento');

CREATE TABLE operacoes (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    tipo tipo_operacao NOT NULL,
    valor NUMERIC(15, 2) NOT NULL CHECK (valor > 0),
    conta_origem_id UUID NOT NULL REFERENCES contas(id),
    conta_destino_id UUID REFERENCES contas(id),
    datahora TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);