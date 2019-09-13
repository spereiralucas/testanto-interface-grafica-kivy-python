SELECT CLIENTE.nomeCliente, count(ABASTECIMENTO.CPF)
	FROM CLIENTE, ABASTECIMENTO
		WHERE CLIENTE.CPF = ABASTECIMENTO.CPF
			GROUP BY CLIENTE.nomeCliente;