# Assetto Corsa Competizione Server Discord Bot

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This project aims to provide a Discord bot for managing a remote Assetto Corsa Competizione server. The bot will allow server administrators to easily control various aspects of the server directly from their Discord server.

## References

https://gist.github.com/AbstractUmbra/a9c188797ae194e592efe05fa129c57f

https://gist.github.com/lykn/a2b68cb790d6dad8ecff75b2aa450f23

## Features

- Start, stop, and restart the Assetto Corsa Competizione server remotely.
- Change server settings such as track, weather, and race duration.
- Manage race sessions, including qualifying and race start times.
- Monitor server status and display live race results.

## Installation

> [!NOTE]
> To allow traffic in and out on your flask server, you need to run the following:
> ``` 
> sudo iptables -I INPUT 6 -m state --state NEW -p tcp --dport 5000 -j ACCEPT
> sudo netfilter-persistent save
> ```

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Configure the bot token and server settings in the `config.json` file.
4. Start the bot by running the module in python with `python -m <module name>`.

## Usage

Once the bot is running and connected to your Discord server, you can use various commands to manage the Assetto Corsa Competizione server. Refer to the bot's help command for a list of available commands and their usage.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
