SELECT CLIENTE.nomeCliente, CLIENTE.CPF,
		CARRO.placaCarro, CARRO.modeloCarro,
		POSTO.idPosto, POSTO.nomePosto, POSTO.enderecoPosto,
		ABASTECIMENTO.dataAbast, ABASTECIMENTO.valorAbast
	FROM CLIENTE, CARRO, POSTO, ABASTECIMENTO
		WHERE CLIENTE.CPF = ABASTECIMENTO.CPF
			and CLIENTE.CPF = CARRO.CPF
				and CLIENTE.CPF = 41912348896; 