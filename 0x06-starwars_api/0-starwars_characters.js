#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}`;

request(url, { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }

  const characters = body.characters;
  let i = 0;

  function fetchCharacter() {
    if (i < characters.length) {
      request(characters[i], { json: true }, (err, res, character) => {
        if (!err) {
          console.log(character.name);
          i++;
          fetchCharacter();
        } else {
          console.log(err);
        }
      });
    }
  }

  fetchCharacter();
});
