import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import '../Styles/LoginStyles.css'

function Login() {

  return (
    <div>
      <div className='Logintitle'>
        Managely
      </div>
      <form className='Logincontainer'>
        <input type='text' placeholder='email' className='Loginitem' id='email'/>
        <input type='password' placeholder='password' className='Loginitem' id='password'/>
        <Link to='/Home'>
          <button placeholder='submit' className='LoginsubmitButton' id='button'>
            Submit
          </button>
        </Link>
        <a className='LoginforgotP' href='/'>
          Forgot Password?
        </a>
      </form>
    </div>
  )
}

export default Login