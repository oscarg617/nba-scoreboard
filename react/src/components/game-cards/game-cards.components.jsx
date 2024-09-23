import './game-cards.styles.css'
import GameCard from '../game-card/game-card.component'
import React, { useState, useEffect } from 'react'

const GameCards = () => {

    const[games, setGames] = useState([])

    useEffect(() => {
        function getGames() {
            fetch('http://localhost:5000/today', {
                method: 'GET',
                headers: {
                'Content-Type': 'application/json'
                }
            })
            .then((response) => response.json())
            .then((data) => setGames(data))
        }
        
        getGames()
        const interval = setInterval(() => getGames(), 30000)
        return () => {
        clearInterval(interval);
        }
    }, [])

  return (
    <div className={`game-cards-container`}>
        {games != null ? 
            games.map(game => (
                <GameCard game={game}/>
            )) : 
        <div> <h1>No Games Today</h1> </div>}
    </div> 
  )
}

export default GameCards