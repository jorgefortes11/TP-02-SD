const tarefas = require('../models/tarefas');

exports.listar = (req, res) => {
  res.json(tarefas.getAll());
};

exports.adicionar = (req, res) => {
  const nova = req.body.descricao;
  const id = tarefas.add(nova);
  res.status(201).json({ id });
};

exports.atualizar = (req, res) => {
  const id = parseInt(req.params.id);
  const nova = req.body.descricao;
  const ok = tarefas.update(id, nova);
  res.json({ sucesso: ok });
};

exports.remover = (req, res) => {
  const id = parseInt(req.params.id);
  const ok = tarefas.remove(id);
  res.json({ sucesso: ok });
};
