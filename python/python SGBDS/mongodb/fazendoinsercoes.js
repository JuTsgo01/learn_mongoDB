//primeira inserção de dados - Método mais longo

use("Aula")

db.getCollection("clientes").insertOne({
    "nomes":"Clodoaldo",
    "idade":"18",
    "sexo":"masculino",
    "email":"clodoaldo@hotmail.com",
    "tel":"16996455897"
})


//Segundo método - Método mais curto

use("Aula")

db.clientes.insertOne({
    "nomes":"Isabelle",
    "idade":"26",
    "sexo":"feminina",
    "email":"isabelle@hotmail.com",
    "tel":"16997459887"
})

//Usando o insertMany para inserir varias collections

use("Aula")
db.clientes.insertMany([
    {
        "nomes":"Eliza",
        "idade":"45",
        "sexo":"feminina",
        "email":"Eliza@hotmail.com",
        "tel":"16997459888"
    },
    {
        "nomes":"Elisvaldo",
        "idade":"52",
        "sexo":"masculino",
        "email":"Elisvaldo@hotmail.com",
        "tel":"16997459889"
    },
    {
        "nomes":"Francisval",
        "idade":"50",
        "sexo":"masculino",
        "email":"Francisval@hotmail.com",
        "tel":"16997459890"
}
])
