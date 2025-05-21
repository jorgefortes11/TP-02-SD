
# TP02 – Sistemas Distribuídos: Lista de Tarefas

Este projeto implementa uma lista de tarefas com duas versões:

- Modo 1: Usando sockets (Python)
- Modo 2: Usando API RESTful (Node.js + Express)

---

## Modo 1 – Sockets (Python)

1. Abrir a pasta socket
2. No terminal 1: iniciar o servidor
   python servidor.py
3. No terminal 2: iniciar o cliente
   python cliente.py
4. No cliente, usar o menu:
   - 1: Adicionar tarefa
   - 2: Listar tarefas
   - 3: Remover tarefa
   - 0: Sair

Se for usar em dois computadores:
- No servidor: HOST = '0.0.0.0'
- No cliente: usar o IP local do servidor

---

## Modo 2 – API RESTful (Node.js)

1. Abrir a pasta rest
2. Instalar dependências:
   npm install
3. Iniciar o servidor:
   node app.js

A API ficará disponível em: http://localhost:3000

Pode-se usar Postman ou Insomnia para testar os endpoints:
- GET    /tarefas         → listar tarefas
- POST   /tarefas         → adicionar tarefa
- PUT    /tarefas/:id     → atualizar tarefa
- DELETE /tarefas/:id     → remover tarefa

Exemplo de corpo JSON para POST/PUT:
{
  "descricao": "Nova tarefa"
}
"""