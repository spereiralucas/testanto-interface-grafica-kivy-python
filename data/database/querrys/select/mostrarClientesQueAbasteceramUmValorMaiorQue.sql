SELECT CLIENTE.nomeCliente, CLIENTE.CPF
	FROM CLIENTE, ABASTECIMENTO
		WHERE ABASTECIMENTO.valorAbast < 100;