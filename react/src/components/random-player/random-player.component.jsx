import './random-player.styles.css'
import React, { useState, useEffect } from 'react'

const RandomPlayer = () => {

    const[player, setPlayer] = useState()    

    const getPlayer = () => {
        fetch('http://localhost:5000/random', {
            method: 'GET',
            headers: {
            'Content-Type': 'application/json'
            }
        })
        .then((response) => response.json())
        .then((data) => {setPlayer(data); return})
    }

    return (
        <div className='random-player-container' >
            <button onClick={getPlayer}>Random Player Generator</button>
                {player ? 
            <div className='player-container' style={{border: `5px solid ${player.teamColor1}`, 
    outline: `5px solid ${player.teamColor2}`}} >
                <div className='player-info' >
                    <img src={player.headshot} width={300} />
                    <div className='player-text' >
                        <div className='text' >
                            <h1>{player.name}</h1>
                        </div>
                        <div className='text team'>
                            <h1>{player.teamAbbr}</h1>
                        </div>
                    </div>
                </div>
                <div className='player-stats' >
                    <div className='per-game-stats'>
                        <div className='text'>
                            <h1>{player.ppg}</h1>
                        </div>
                        <div className='text'>
                            <h1>{player.rpg}</h1>
                        </div>
                        <div className='text'>
                            <h1>{player.apg}</h1>
                        </div>
                    </div>
                    <div className='percentages'>
                        <div className='text'>
                            <h1>{player.fgp}</h1>
                        </div>
                        <div className='text'>
                            <h1>{player.threep}</h1>
                        </div>
                        <div className='text'>
                            <h1>{player.ftp}</h1>
                        </div>
                    </div>
                </div>
            </div> : null }
        </div>
    )
}

export default RandomPlayer