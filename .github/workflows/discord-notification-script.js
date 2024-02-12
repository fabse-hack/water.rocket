const { Client } = require('discord.js');
const client = new Client();

client.once('ready', () => {
    console.log('Bot is ready!');
});

client.login(process.env.BOT_KEY);

client.on('message', async message => {
    if (message.content === '!watchCommits') {
        message.channel.send('Ich werde jetzt Commits überwachen.');
    }
});

client.on('commit', async (commit) => {
    const channel = client.channels.cache.find(ch => ch.name === 'rocketscience');
    channel.send(`Es wurde ein neuer Commit gemacht: ${commit.message}`);
});
