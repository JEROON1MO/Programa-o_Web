/*
* Curso de Engenharia de Software - UniEVANGÉLICA 
* Disciplina de Programação Web 
* Dev: jERÔNIMO NETO
* 06/06/2024
*/

const express = require('express');
const app = express();
app.use(express.json());

let cars = [];

// Recuperar a lista de carros
app.get('/api/cars', (req, res) => {
    res.json(cars);
});

// Criar um novo carro
app.post('/api/cars', (req, res) => {
    const newCar = req.body;
    cars.push(newCar);
    res.status(201).json(newCar);
});

// Recuperar informações de um carro específico por ID
app.get('/api/cars/:car_id', (req, res) => {
    const carId = req.params.car_id;
    const car = cars.find(car => car.id === carId);
    if (!car) return res.status(404).send('Carro não encontrado.');
    res.json(car);
});

// Atualizar informações de um carro específico por ID
app.put('/api/cars/:car_id', (req, res) => {
    const carId = req.params.car_id;
    const updatedCar = req.body;
    const index = cars.findIndex(car => car.id === carId);
    if (index === -1) return res.status(404).send('Carro não encontrado.');
    cars[index] = { ...cars[index], ...updatedCar };
    res.json(cars[index]);
});

// Excluir um carro específico por ID
app.delete('/api/cars/:car_id', (req, res) => {
    const carId = req.params.car_id;
    const index = cars.findIndex(car => car.id === carId);
    if (index === -1) return res.status(404).send('Carro não encontrado.');
    const deletedCar = cars.splice(index, 1);
    res.json(deletedCar);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server is running on port ${PORT}`));
