const { Client } = require('discord.js');

const client = new Client();
const githubRepo = 'https://github.com/fabse-hack/water.rocket/';

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', async message => {
  if (message.content === '!watchCommits') {
    message.channel.send('Ich werde jetzt Commits überwachen.');

    const channel = client.channels.cache.find(ch => ch.name === 'rocketscience');

    setInterval(() => {
      channel.send(`Es wurde ein neuer Commit in ${githubRepo} gemacht!`);
    }, 60000);
  }
});

client.login(process.env.BOT_KEY);
