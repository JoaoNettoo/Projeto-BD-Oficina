-- Inserir nova ordem de serviço
DELIMITER //
CREATE PROCEDURE inserir_ordem_servico(
    IN veiculoId INT,
    IN statusInicial VARCHAR(20),
    IN valorInicial DECIMAL(10,2)
)
BEGIN
    INSERT INTO ordens_servico (veiculo_id, data_abertura, status, valor_total)
    VALUES (veiculoId, NOW(), statusInicial, valorInicial);
END //
DELIMITER ;

-- Atualizar valor total de uma OS
DELIMITER //
CREATE PROCEDURE atualizar_valor_os(
    IN osId INT,
    IN novoValor DECIMAL(10,2)
)
BEGIN
    UPDATE ordens_servico
    SET valor_total = novoValor,
        data_modificacao = NOW()
    WHERE id = osId;
END //
DELIMITER ;

-- Listar serviços por veículo
DELIMITER //
CREATE PROCEDURE listar_servicos_por_veiculo(
    IN veiculoId INT
)
BEGIN
    SELECT os.id AS ordem_id, s.nome AS servico, s.valor
    FROM ordens_servico os
    JOIN itens_os ios ON os.id = ios.ordem_id
    JOIN servicos s ON ios.servico_id = s.id
    WHERE os.veiculo_id = veiculoId;
END //
DELIMITER ;

-- Remover cliente e seus registros relacionados
DELIMITER //
CREATE PROCEDURE remover_cliente(
    IN clienteId INT
)
BEGIN
    DELETE FROM ordens_servico WHERE veiculo_id IN (
        SELECT id FROM veiculos WHERE cliente_id = clienteId
    );
    DELETE FROM veiculos WHERE cliente_id = clienteId;
    DELETE FROM clientes WHERE id = clienteId;
END //
DELIMITER ;
