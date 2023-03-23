import React, { useState, useEffect } from 'react'
import NavBar from '../Components/NavBar'
import '../Styles/HomeStyles.css'

function Home() {

  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/members").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  return (
    <div>
      <NavBar/>
      <div className='HannouncementsContainer'>
        <div className='HannouncementsTitle'>
          Announcements
        </div>
        <div className='Hannouncements'>
          Progress report 3 due 3/16/23
        </div>
      </div>
      <div className='HpagesContainer'>
        <div className='HpageBox'>
          <div className='HpagesTitle'>
            Employees
          </div>
          <div className='Hpages'>
              Employees table goes here
          </div>
        </div>
        <div className='HpageBox'>
          <div className='HpagesTitle'>
            Example Data
          </div>
          <div className='Hpages'>
            <div>
      {(typeof data.members === 'undefined') ? (
        <p>Loading...</p>
      ) : (
        data.members.map((member, i) => (
          <p key={i}>{member}</p>
        )) 
      )}

    </div>
          </div>
        </div>

      </div>
    </div>
  )
}

export default Home