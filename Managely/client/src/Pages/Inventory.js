import React, { useState, useEffect } from 'react'
import NavBar from '../Components/NavBar'
import '../Styles/InventoryStyles.css'

function Inventory() {

  
  return (
    <div>
      <NavBar/>
      <div className='inventoryContainer'>
        <div className='inventoryTitle'>
          Inventory
        </div>
        <div className='inventory'>
          Inventory Table Goes Here
        </div>
      </div>
      <div className='IButtoncontainer'>
        <a className='IButtonitem' href='/'>
          Add
        </a>
        <a className='IButtonitem' href='/'>
          Edit
        </a>
        <a className='IButtonitem' href='/'>
          Delete
        </a>
        <div className='IButtonitem'>
          Generate Report
        </div>
      </div>
    </div>
  )
}

export default Inventory