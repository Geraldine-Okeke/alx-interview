#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Request failed with status code ${response.statusCode}`);
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.error(error);
        return;
      }

      if (response.statusCode === 200) {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      }
    });
  });
});
