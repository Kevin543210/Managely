import React, { useState, useEffect } from 'react'
import NavBar from '../Components/NavBar'
import '../Styles/EmployeesStyles.css'

function Employees() {

  
  return (
    <div>
      <NavBar/>
      <div className='employeesContainer'>
        <div className='employeesTitle'>
          Empoyees
        </div>
        <div className='employees'>
          Employees Table Goes Here
        </div>
      </div>
      <div className='EButtoncontainer'>
        <a className='EButtonitem' href='/'>
          Add
        </a>
        <a className='EButtonitem' href='/'>
          Edit
        </a>
        <a className='EButtonitem' href='/'>
          Delete
        </a>
        <div className='EButtonitem'>
          Generate Report
        </div>
      </div>
    </div>
  )
}

export default Employees