# Softball Management App

A web application for managing recreational slow pitch softball leagues, teams, players, and game statistics.

## Features (Planned)
- Team and player management
- Season tracking
- Game scheduling and scoring
- Player statistics tracking
- Support for substitute players
- User authentication and roles

## Database Schema

The database schema is designed to handle:
- Multiple seasons and leagues
- Teams with seasonal rosters
- Player statistics per game
- Substitute/fill-in players
- Game scheduling and results

View the full schema: 
<img width="824" height="593" alt="SCR-20251201-oepk" src="https://github.com/user-attachments/assets/5b8eb143-f0cc-45c6-9c2c-98004a4bfc98" />

## Tech Stack (Planned)
- **Frontend**: SvelteKit
- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL
- **Authentication**: JWT

## Database Tables
- `users` - User authentication and roles
- `teams` - Team information
- `seasons` - League seasons
- `team_seasons` - Team rosters per season
- `players` - Player profiles and roster assignments
- `substitute_players` - Fill-in players
- `games` - Game scheduling and results
- `player_game_stats` - Individual player performance

## Status
🚧 Currently in development - Database schema design complete
