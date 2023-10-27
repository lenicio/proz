DROP TABLE IF EXISTS `transacoes`;
DROP TABLE IF EXISTS `categorias`;
DROP TABLE IF EXISTS `usuarios`;


CREATE TABLE `categorias` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descricao` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
);


CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(200) NOT NULL,
  `email` varchar(200) DEFAULT NULL,
  `senha` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
);


CREATE TABLE `transacoes` (
  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `descricao` varchar(200) NOT NULL,
  `valor` float NOT NULL,
  `data_transacao` date NOT NULL,
  `tipo` varchar(10) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_categoria` int(11) NOT NULL,
  FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`),
  FOREIGN KEY (`id_categoria`) REFERENCES `categorias` (`id`)
);


INSERT INTO usuarios (nome, email, senha) VALUES
('João Silva', 'joao.silva@gmail.com', 'senha123'),
('Maria Santos', 'maria.santos@outlook.com', 'senha456'),
('Pedro Oliveira', 'pedro.oliveira@yahoo.com', 'senha789'),
('Ana Pereira', 'ana.pereira@gmail.com', 'senhaabc'),
('Lucas Fernandes', 'lucas.fernandes@yahoo.com', 'senhaxyz'),
('Mariana Costa', 'mariana.costa@gmail.com', 'senha4567'),
('Carlos Rodrigues', 'carlos.rodrigues@yahoo.com', 'senha8901'),
('Fernanda Alves', 'fernanda.alves@gmail.com', 'senhaxpto'),
('Rafael Santos', 'rafael.santos@outlook.com', 'senhatest'),
('Julia Lima', 'julia.lima@yahoo.com', 'senha1234');


INSERT INTO categorias (descricao) VALUES
('Aluguel'),
('Comida'),
('Transporte'),
('Educação'),
('Saúde'),
('Lazer'),
('Salário'),
('Investimentos'),
('Presentes'),
('Impostos');


INSERT INTO transacoes (descricao, valor, data_transacao, tipo, id_usuario, id_categoria) VALUES
('Compra de alimentos', 100.50, '2023-10-15', 'despesa', 1, 2),
('Salário', 2500.00, '2023-10-05', 'receita', 2, 7),
('Aluguel', 800.00, '2023-10-01', 'despesa', 3, 1),
('Presente de aniversário', 50.00, '2023-09-20', 'despesa', 4, 9),
('Gasolina', 75.20, '2023-09-15', 'despesa', 5, 3),
('Educação', 500.00, '2023-09-10', 'despesa', 6, 4),
('Venda de eletrônicos', 600.00, '2023-08-25', 'receita', 7, 2),
('Viagem', 1200.00, '2023-08-20', 'despesa', 8, 8),
('Presente de casamento', 75.00, '2023-08-15', 'despesa', 9, 9),
('Salário', 2800.00, '2023-08-05', 'receita', 10, 7),
('Academia', 80.00, '2023-07-25', 'despesa', 1, 6),
('Conta de luz', 120.00, '2023-07-15', 'despesa', 2, 1),
('Dividendo de ações', 300.00, '2023-07-10', 'receita', 3, 7),
('Roupas', 150.00, '2023-07-05', 'despesa', 4, 3),
('Salário', 2600.00, '2023-06-25', 'receita', 5, 7),
('Restaurante', 45.50, '2023-06-20', 'despesa', 6, 2),
('Manutenção do carro', 200.00, '2023-06-10', 'despesa', 7, 3),
('Presente de Natal', 100.00, '2023-06-05', 'despesa', 8, 9),
('Conta de telefone', 50.00, '2023-05-25', 'despesa', 9, 1),
('Salário', 2700.00, '2023-05-15', 'receita', 10, 7),
('Investimento em ações', 500.00, '2023-05-10', 'receita', 1, 7),
('Aluguel', 850.00, '2023-05-01', 'despesa', 2, 1),
('Férias', 1500.00, '2023-04-20', 'despesa', 3, 8),
('Presente de aniversário', 60.00, '2023-04-15', 'despesa', 4, 9),
('Gasolina', 80.00, '2023-04-10', 'despesa', 5, 3),
('Educação', 450.00, '2023-04-05', 'despesa', 6, 4),
('Salário', 2900.00, '2023-03-25', 'receita', 7, 7),
('Compra de eletrônicos', 350.00, '2023-03-20', 'despesa', 8, 2),
('Presente de formatura', 70.00, '2023-03-15', 'despesa', 9, 9),
('Conta de água', 70.00, '2023-03-10', 'despesa', 10, 1);