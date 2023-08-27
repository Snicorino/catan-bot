# catan-bot

## vision

### Gamestate class
Data:
- Resource Cards in deck / in players hands
- Special Cards in deck / in players hands
- Player Score (hidden and public)
- Generated Board state 
- Settlements/Cities/Roads/Robber


Methods:
- Player
    - Draw Special Card
    - Roll Resource -> Give players Resource Cards
    - Place Settlements/Cities/Move Robber -> Steal Card
    - Discard Cards
    - Trade (with bank or player, ports)
- RNG Method for dice Roll
- print/format method to inspect game state visually
