#!/usr/bin/node
const request = require("request");
movie_id = process.argv[2]
request(
  "https://swapi-api.alx-tools.com/api/films/" + movie_id + "/",
  async function (_, _, body) {
    characters = JSON.parse(body).characters;
    for (char of characters) {
      await new Promise((resolve, reject) => {
        request(char, function (err, res, content) {
          console.log(JSON.parse(content).name);
          resolve();
        })
      })
    }
  }
);
