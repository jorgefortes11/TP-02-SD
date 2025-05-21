const express = require('express');
const router = express.Router();
const controller = require('../controllers/tarefasController');

router.get('/', controller.listar);       
router.post('/', controller.adicionar); 
router.put('/:id', controller.atualizar); 
router.delete('/:id', controller.remover); 

module.exports = router;
