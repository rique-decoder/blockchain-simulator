Este repositório contém uma implementação educacional de uma blockchain em Python.

O projeto demonstra os conceitos fundamentais de uma cadeia de blocos:

- Criação do bloco inicial, chamado **Genesis Block**
- Armazenamento de índice, data, dados e hash anterior
- Geração de hashes SHA-256 para cada bloco
- Encadeamento dos blocos por meio do campo `previous_hash`
- Validação da integridade da cadeia
- Detecção de dados ou hashes adulterados

## Como funciona

A classe `Block` representa um bloco da blockchain e contém:

- `index`: posição do bloco na cadeia
- `timestamp`: data e hora de criação
- `data`: conteúdo ou transação armazenada
- `previous_hash`: hash do bloco anterior
- `hash`: hash calculado a partir dos dados do bloco

A classe `Blockchain` cria o bloco gênesis e permite adicionar novos blocos encadeados ao bloco anterior.

A integridade é verificada pelo método `is_chain_valid()`, que confirma:

1. Se o hash armazenado corresponde ao conteúdo atual do bloco.
2. Se o `previous_hash` corresponde ao hash real do bloco anterior.

## Requisitos

- Python 3

Não há bibliotecas externas necessárias.

## Executando o projeto

Clone o repositório:

```bash
git clone https://github.com/rique-decoder/blockchain-simulator.git
cd blockchain-simulator
```

Execute o simulador:

```bash
python blockchain.py
```

O arquivo de exemplo cria uma blockchain chamada `henriquecoin` e adiciona cinco transações fictícias.

## Testando a integridade

O código contém testes comentados que demonstram como adulterar os dados ou o hash anterior de um bloco. Ao descomentar essas partes, é possível verificar como o método de validação identifica a alteração da cadeia.

## Licença

Este projeto está disponível sob a licença MIT.