const express = require('express');
const app = express();
const tarefasRoutes = require('./routes/tarefas');

app.use(express.json()); 

app.use('/tarefas', tarefasRoutes); 

app.listen(3000, () => {
  console.log('Servidor a correr na porta 3000');
});
