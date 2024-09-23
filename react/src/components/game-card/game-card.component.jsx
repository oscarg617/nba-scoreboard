import './game-card.styles.css'

const GameCard = ({ game }) => {
  const { poRoundDesc, seriesGameNumber, seriesText, homeTeam, homeScore, awayTeam, awayScore, quarter, status, statusColor, time, homeColor1, homeColor2, awayColor1, awayColor2} = game;
  return (
    <div className={`game-card-container ${homeTeam}-${awayTeam}`}>
      <div className="series-info">
        <h3>{poRoundDesc}</h3>
        <h3>{seriesGameNumber}</h3>
        <h3>{seriesText}</h3>
      </div>
      <div className={`teams-container`}>
        <div className={`team-container ${homeTeam}`}>
            <h2 style={{color: `${homeColor1}`, WebkitTextStroke: `1px ${homeColor2}`}}>{homeTeam}</h2>
            <h3>{homeScore}</h3>
        </div>
        <div className={`team-container ${awayTeam}`}>
            <h2 style={{color: `${awayColor1}`, WebkitTextStroke: `1px ${awayColor2}`}}>{awayTeam}</h2>
            <h3>{awayScore}</h3>
        </div>
      </div>
      <div className={`game-info ${homeTeam}-${awayTeam}`}>
        <div className={`quarter ${homeTeam}-${awayTeam}`}>
            <h4>{quarter}</h4>
        </div>
        <div className={`status ${homeTeam}-${awayTeam}`}>
            <h4 style={{color: `${statusColor}`}} >{status}</h4>
        </div>
        <div className={`time ${homeTeam}-${awayTeam}`}>
            <h4>{time}</h4>
        </div>
      </div>
    </div>
  )
}

export default GameCard