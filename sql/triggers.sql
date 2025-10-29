-- Atualizar estoque de peças ao adicionar item de OS
DELIMITER //
CREATE TRIGGER atualizar_estoque_peca
AFTER INSERT ON itens_os
FOR EACH ROW
BEGIN
    UPDATE pecas
    SET quantidade_estoque = quantidade_estoque - NEW.quantidade
    WHERE id = NEW.peca_id;
END //
DELIMITER ;

-- Atualizar data de modificação de OS
DELIMITER //
CREATE TRIGGER atualizar_data_mod_os
AFTER UPDATE ON ordens_servico
FOR EACH ROW
BEGIN
    UPDATE ordens_servico
    SET data_modificacao = NOW()
    WHERE id = NEW.id;
END //
DELIMITER ;

-- Registrar log de exclusão de cliente
DELIMITER //
CREATE TRIGGER log_exclusao_cliente
AFTER DELETE ON clientes
FOR EACH ROW
BEGIN
    INSERT INTO logs_clientes (cliente_id, nome, deletado_em)
    VALUES (OLD.id, OLD.nome, NOW());
END //
DELIMITER ;
