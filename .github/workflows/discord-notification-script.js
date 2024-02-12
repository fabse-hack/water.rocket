const { Client } = require('discord.js');

const client = new Client();

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.login(process.env.BOT_KEY); // Verwende das Environment-Variable BOT_KEY

// Hier kannst du deine Bot-Logik hinzufügen

client.on('message', message => {
  if (message.content === '!ping') {
    message.channel.send('Pong!');
  }
});
