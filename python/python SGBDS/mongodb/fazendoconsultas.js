//Fazendo consultas

//Esse comando mostra todos os resultados dentro da coleção 'clientes'
use('Aula')
db.clientes.find()

//aplicando filtro para trazer tudo onde nome = Clodoaldo
use('Aula')
db.clientes.find({nomes:'Clodoaldo'})

//Filtro que contenha esses dois valores
use('Aula')
db.clientes.find({nomes:{$in:['Isabelle','Clodoaldo']}})

//Filtro que contenha esses dois valores com operador 'like'
//Usando '//i' que funciona como o like
//Se eu usar apenas o '//', é como se fosse o like
//Usando o 'i', ele ignora maiusculo e minusculo, não diferenciando
use('Aula')
db.clientes.find({nomes:{$in:[/isabelle/i,/clodoaldo/i]}})

//Filtrando tudo que for diferente de:
use('Aula')
db.clientes.find({nomes:{$ne:'Clodoaldo'}})

//Filtrando cliente com idade de 26 anos
use('Aula')
db.clientes.find({idade:{$gt:26}})

//Filtrando idade menor ou igual a 26
use('Aula')
db.clientes.find({idade:{$lte:26}})

//Fazendo uma consulta com idade maior que
//Além disso, filtrando algumas colunas
use('Aula')
db.clientes.find(
    {idade:{$gt:26}},
    {sexo:0, email:0, tel:0})

//Filtrando clientes com sexo feminino e idade maior que 16
use('Aula')
db.clientes.find({sexo:'feminina', idade:{$gt:26}})

//contando a quantidade do sexo feminino
use('Aula')
db.clientes.aggregate([
    {$match: {sexo:/feminina/i}},
    {$group: {_id: '$sexo', total:{$sum: 1}}}
])

//contando a quantidade do sexo masculino
use('Aula')
db.clientes.aggregate([
    {$match: {sexo: 'masculino'}},
    {$group: {
      _id:'$sexo', total:{$sum: 1}}}
])

//Pegando idade média por sexo
use('Aula')
db.clientes.aggregate([
    {
        $group: {
          _id: {sexo: '$sexo'},
          media: {
            $avg: '$idade'
          }
        }   
    }
])

//filtrando a quantidade de pessoas acima de 26 anos
use('Aula')

db.clientes.aggregate([
    {$match: {idade:{$gt:26}}},
    {$group: {
        _id: null,
        quantidade: {$sum:1}
        }
    }
])


/*
Igual a: $eq
Diferende de: $ne
Maior que: $gt
Maior ou igual a: $gte
Menor que: $lt
Menor ou igual a: $lte
Dentro de: $in
Não dentro de: %nin
Existe: $exists
*/

