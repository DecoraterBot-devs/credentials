# credentials

This repository is for creating the credentials database for DecoraterBot.

## Creating the database

- edit ``Data/Credentials.sql`` to use your own bot token.
  - Note: Do not commit and push this file to GitHub as then it would automatically invalidate your token.
  - Note: Never push it to private GitHub repositories either because if your GitHub account becomes compromised, they will also compromise your bot.
  - Note: if you need to git pull and recreate the database, stash your bot's token somewhere where it will not be lost and then pull (ensure that all uncommited changes are removed first).
- Save the file and create the database file (using sqlite3) from the files in this repository.
  - On Windows run ``py -m create_db`` to create the database.
  - On macOS and Linux run ``python3 -m create_db`` (or ``python3.11`` if you prefer to use Python 3.11).
