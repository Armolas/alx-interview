#!/usr/bin/node
const request = require('request');

const fetchJson = (url) => {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (err, res, body) => {
      if (err) {
        reject(err);
      } else if (res.statusCode !== 200) {
        reject(new Error(`Request failed with status code ${res.statusCode}`));
      } else {
        resolve(body);
      }
    });
  });
};

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';

const fetchMovieCharacters = async (movieId) => {
  try {
    const movieData = await fetchJson(`${baseUrl}${movieId}/`);
    const characterPromises = movieData.characters.map(url => fetchJson(url));
    const characters = await Promise.all(characterPromises);
    characters.forEach(character => console.log(character.name));
  } catch (err) {
    console.error('Error fetching data:', err);
  }
};

fetchMovieCharacters(movieId);
