import React, { useState, useEffect } from 'react'
import NavBar from '../Components/NavBar'
import '../Styles/HomeStyles.css'

function Home() {

  
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
            Inventory
          </div>
          <div className='Hpages'>
            Inventory table goes here
          </div>
        </div>

      </div>
    </div>
  )
}

export default Home