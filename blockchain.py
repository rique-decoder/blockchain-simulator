"""
Criar uma Blockchain

Enunciado Prático: Implemente uma estrutura básica de Blockchain em Python (ou C++) contendo uma classe Block e uma classe Blockchain. O bloco deve conter os seguintes atributos: index, timestamp, data (transações ou mensagens), previous_hash e hash.

Requisitos:

    Escreva uma função de hash (ex: SHA-256) que calcule o hash do bloco concatenando seus atributos.

    Implemente o mecanismo de Genesis Block (o primeiro bloco da cadeia).

    Adicione um método para validar a integridade da cadeia (verificar se o previous_hash bate com o hash real do bloco anterior e se nenhum dado foi adulterado).
"""

import hashlib
from datetime import datetime



class Block():
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        message = "".join(map(str, [self.index, self.timestamp, self.data, self.previous_hash])).encode()


        return hashlib.sha256(message).hexdigest()



class Blockchain():
    """A blockchain é uma lista normal de blocos, ou seja, [bloco 01, bloco 02]"""
    def __init__(self):
        self.chain = []
        self.genesis = Block(0, datetime.now(), "genesis block", 0)
        self.chain.append(self.genesis)

    def add_block(self, data):
        new_block = Block(self.chain[-1].index + 1, datetime.now(), data, self.chain[-1].hash)
        self.chain.append(new_block)

    def is_chain_valid(self):        

        #Verificando se a cadeia quebrou
        for iblock in range(1, len(self.chain)):
            cur = self.chain[iblock]
            prev = self.chain[iblock - 1]

            if cur.hash != cur.calculate_hash():
                return False

            if cur.previous_hash != prev.hash:
                return False

        return True


# Teste da Blockchain

henriquecoin = Blockchain()
henriquecoin.add_block("transacao-01")
henriquecoin.add_block("transacao-02")
henriquecoin.add_block("transacao-03")
henriquecoin.add_block("transacao-04")
henriquecoin.add_block("transacao-05")

print("Cadeia íntegra é válida?", henriquecoin.is_chain_valid())  # deve ser True

# Teste 1: adulterando o 'data' de um bloco
henriquecoin.chain[3].data = "henriquecoin-roubado"
print("Após adulterar 'data', cadeia é válida?", henriquecoin.is_chain_valid())  # deve ser False
# assert henriquecoin.is_chain_valid()

# desfaz a adulteração pra próximo teste não ficar bagunçado
henriquecoin.chain[3].data = "transacao-04"
# assert henriquecoin.is_chain_valid()

# Teste 2: adulterando o 'previous_hash' de um bloco
henriquecoin.chain[3].previous_hash = "0"
print("Após adulterar 'previous_hash', cadeia é válida?", henriquecoin.is_chain_valid())  # deve ser False
# assert henriquecoin.is_chain_valid()


"""
Descomente os codigos do assert e veja que realmente da erro.
"""
