import GameCards from './components/game-cards/game-cards.components'
import './App.css'
import Title from './components/title/title.component'
import React, { useState, useEffect } from 'react'
import { BrowserRouter as Router, Route, Link, Routes } from "react-router-dom";
import RandomPlayer from './components/random-player/random-player.component';

function App() {

  return (
    <div>
      <Router>
        <div className='navigation' >
          <div className='links'>
            <div className='link'>
              <Link to="/">Home</Link>
            </div>
            <div className='link'>
              <Link to="/random">Random</Link>
            </div>
          </div>
        </div>
        <Title/>
        <div>
          <Routes>
            <Route path="/" element={<GameCards />} />
            <Route path="/random" element={<RandomPlayer />} />
          </Routes>
        </div>
      </Router>
    </div>
  )
}

export default App
