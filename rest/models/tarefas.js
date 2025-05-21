let lista = [];

exports.getAll = () => lista;

exports.add = (desc) => {
  lista.push(desc);
  return lista.length - 1;
};

exports.update = (id, desc) => {
  if (id >= 0 && id < lista.length) {
    lista[id] = desc;
    return true;
  }
  return false;
};

exports.remove = (id) => {
  if (id >= 0 && id < lista.length) {
    lista.splice(id, 1);
    return true;
  }
  return false;
};
