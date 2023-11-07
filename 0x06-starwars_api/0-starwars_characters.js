#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2]; // Get the Movie ID from the command-line arguments
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;


request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const film = JSON.parse(body);
    for (let i = 0; i < film.characters.length; i++) {
      request(film.characters[i], function (error, response, body) {
        if (!error && response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    }
  }
});
