
import * as readline from 'node:readline/promises';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let personas = [];

while (true) {
    let nombre = await rl.question('Ingrese el nombre de la persona (o escriba "finalizar" para terminar): ');
    if (nombre.toLowerCase() === 'finalizar')
        break; 

let edad = parseInt(await rl.question ("Ingrese la edad de la persona:"));
let nota = parseFloat(await rl.question ("Ingrese la nota de la persona:"));

personas.push([nombre, edad, nota]);

}

console.log("Lista de personas:" , personas);

rl.close



